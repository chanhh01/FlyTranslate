import easyocr
import os
from repository import translation, messagebox_repo
import cv2
import mysql_config
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import textwrap
import datetime
import pytz

conn = mysql_config.setup_mysql()


def initialize_OCR_Reader(source_lang_code):
    global reader

    lang = get_OCR_lang_code(source_lang_code)
    print(lang)
    reader = easyocr.Reader(lang, gpu=True)


def startOCR(img, source_lang_code, target_lang_code, opt, font_size, to_save_log, paragraph):
    font_path = get_required_font_style_for_target(target_lang_code)

    results = reader.readtext(img, paragraph=paragraph)
    translation.initiateTranslator(source_lang_code, target_lang_code)
    # the result structure = [(tuple1), (tuple2)]
    # tuple1 = ([top_left, top_right, bottom_right, bottom_left], extracted_text, confident_level)

    file_path = None

    increase_width = check_language_to_decide_max_text_width(target_lang_code)

    if to_save_log == 1:
        file_path = retrieve_existing_or_create_new_log_file()

    if opt == 'overlay':
        for result in results:
            top_left_coord = tuple(result[0][0])
            bottom_right_coord = tuple(result[0][2])
            extracted_text = result[1]
            translated_text = translation.startTranslate(extracted_text)

            if to_save_log == 1:
                save_to_txt_file(source_lang_code, extracted_text, target_lang_code, translated_text, file_path)

            if translated_text is not None:
                img = overlayText(img, top_left_coord, bottom_right_coord, translated_text, font_path, font_size, increase_width)

    elif opt == 'rewrite':
        for result in results:
            top_left_coord = tuple(result[0][0])
            bottom_right_coord = tuple(result[0][2])
            extracted_text = result[1]
            translated_text = translation.startTranslate(extracted_text)

            if to_save_log == 1:
                save_to_txt_file(source_lang_code, extracted_text, target_lang_code,  translated_text, file_path)

            if translated_text is not None:
                img = rewriteText(img, top_left_coord, bottom_right_coord, translated_text, font_path, font_size, increase_width)

    return img


def retrieve_existing_or_create_new_log_file():
    timezone = pytz.timezone('Asia/Shanghai')
    current_date = datetime.datetime.now(pytz.utc).astimezone(timezone)
    current_date_string = current_date.strftime("%Y-%m-%d")

    parent_path = os.getcwd()
    file_path = os.path.abspath(os.path.join(parent_path, 'log_files'))

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    files = os.listdir(file_path)

    for file_name in files:
        file_date_string = file_name.split("_", 1)[0]

        if file_date_string == current_date_string:
            log_file_path = os.path.join(file_path, file_name)
            return log_file_path

    new_file_name = f"{current_date_string}_translation-log.txt"
    log_file_path = os.path.join(file_path, new_file_name)
    with open(log_file_path, 'w') as new_file:
        pass  # Create an empty file
    return log_file_path


def save_to_txt_file(source_lang_code, extracted_text, target_lang_code, translated_text, file_path):
    timezone = pytz.timezone('Asia/Shanghai')
    current_date = datetime.datetime.now(pytz.utc).astimezone(timezone)
    time = current_date.strftime("%H:%M:%S")

    append_line = f"[{time}] ({source_lang_code}) {extracted_text} >> ({target_lang_code}) {translated_text}"

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(append_line + '\n')


def overlayText(img, top_left_coord, bottom_right_coord, translated_text, font_path, font_size, increased_width):
    x1, y1 = (int(top_left_coord[0]), int(top_left_coord[1]))
    x2, y2 = (int(bottom_right_coord[0]), int(bottom_right_coord[1]))

    box_width = x2 - x1
    max_text_width = box_width / int(font_size)

    if increased_width:
        max_text_width *= 2.5
        max_text_width = int(max_text_width)

    if max_text_width > 0:
        wrapper = textwrap.TextWrapper(width=int(max_text_width))
        img = cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        if font_path is None:
            font = ImageFont.truetype("arial.ttf", int(font_size))
        else:
            font = ImageFont.truetype(font_path, int(font_size))

        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        new_img = ImageDraw.Draw(img_pil)
        wrapped_text = wrapper.fill(text=translated_text)
        new_img.text((x1, y1 - 50), wrapped_text, font=font, fill=(0, 255, 0, 0), stroke_width=2,
                     stroke_fill=(0, 0, 0))
        img_with_text = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        return img_with_text
    else:
        return img


# inspired by https://towardsdatascience.com/remove-text-from-images-using-cv2-and-keras-ocr-24e7612ae4f4
def rewriteText(img, top_left_coord, bottom_right_coord, translated_text, font_path, font_size, increased_width):
    x1, y1 = (int(top_left_coord[0]), int(top_left_coord[1]))
    x2, y2 = (int(bottom_right_coord[0]), int(bottom_right_coord[1]))

    box_width = x2 - x1
    max_text_width = box_width / int(font_size)

    if increased_width:
        max_text_width *= 2.5
        max_text_width = int(max_text_width)

    if max_text_width > 0:
        wrapper = textwrap.TextWrapper(width=int(max_text_width))

        mask = np.zeros(img.shape[:2], dtype=np.uint8)
        # instead of using cv2.line, cv2.rectangle is used to define a more clear boundary to erase texts only if possible
        cv2.rectangle(mask, (x1, y1), (x2, y2), (255, 255, 255), thickness=-1)
        img = cv2.inpaint(img, mask, inpaintRadius=10, flags=cv2.INPAINT_TELEA)

        if font_path is None:
            font = ImageFont.truetype("arial.ttf", int(font_size))
        else:
            font = ImageFont.truetype(font_path, int(font_size))

        img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        new_img = ImageDraw.Draw(img_pil)
        wrapped_text = wrapper.fill(text=translated_text)
        new_img.text((x1, y1), wrapped_text, font=font, fill=(0, 255, 0, 0), stroke_width=2,
                     stroke_fill=(0, 0, 0))
        img_with_text = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        return img_with_text
    else:
        return img


def check_language_to_decide_max_text_width(lang_code):
    target = ['ja', 'ko', 'zh-CN', 'zh-TW']

    # this is because languages such as chinese, korean and japanese are written
    # in independent letters (each letter means something), therefore they take up
    # less text width compared to other languages such as english or spanish.
    # False = no need to expand original max_text_width. Else, 2x the original max_text_width
    for res in target:
        if lang_code == res:
            return False

    return True


def get_OCR_lang_code(source_lang_code):
    try:
        query = "SELECT lang_code_for_ocr FROM languages WHERE lang_code = %s"
        cursor = conn.cursor()
        val = (source_lang_code,)
        cursor.execute(query, val)

        lang_code = cursor.fetchone()
        cursor.close()

        if lang_code is None:
            messagebox_repo.messagebox("OCR language code error",
                                       f"Source language with code of {source_lang_code} is not supported by OCR.",
                                       "warning", "ok")
            return ['en']
        else:
            if lang_code[0] != 'en':
                return [lang_code[0], 'en']
            else:
                return [lang_code[0]]
    except Exception as e:
        messagebox_repo.messagebox("OCR language code error", f"{e}", "warning", "ok")
        return ['en']


def get_required_font_style_for_target(target_lang_code):
    try:
        query = "SELECT display_lang_font_dir FROM languages WHERE lang_code = %s"
        cursor = conn.cursor()
        val = (target_lang_code,)
        cursor.execute(query, val)

        res = cursor.fetchone()
        cursor.close()

        if res is None:
            messagebox_repo.messagebox("Font style retrieval error",
                                       "Target language is not found in system.", "warning", "ok")
            return None
        else:
            font_style_name = res[0]

            if font_style_name is not None:
                parent_path = os.getcwd()
                font_dir = os.path.abspath(os.path.join(parent_path, 'font_styles'))
                font_style_dir = os.path.abspath(os.path.join(font_dir, font_style_name))
                return font_style_dir
            else:
                return None
    except Exception as e:
        messagebox_repo.messagebox("Font style retrieval error",
                                   f"{e}", "warning", "ok")
        return None
