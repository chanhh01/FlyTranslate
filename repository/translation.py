from deep_translator import GoogleTranslator

translator = None


def initiateTranslator(source_lang_code, target_lang_code):
    global translator

    if not translator:
        translator = GoogleTranslator(source=source_lang_code, target=target_lang_code)
    else:
        translator.source = source_lang_code
        translator.target = target_lang_code


def startTranslate(input_text):
    output_text = translator.translate(text=input_text)
    return output_text
