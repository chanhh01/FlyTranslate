# FlyTranslate

Final Year Project (FYP) for Asia Pacific University done by Chan Hiang Hao.


Problem Statement:
![Problem Statements](https://github.com/chanhh01/FlyTranslate/assets/84566394/8cd8002e-e494-4862-8194-4e2df3a84d50)


Main deliverables:
1. Scan device screen and extract text using OCR, used [EasyOCR](https://github.com/JaidedAI/EasyOCR).
2. Translate extracted text using [deep translator](https://github.com/nidhaloff/deep-translator).
3. Overlay translated text into CV2 window with processed image.

Other reference:
[Snipping tool for cropping screen boundary inspired by](https://github.com/harupy/snipping-tool/tree/master) [harupy](https://github.com/harupy)

Documented details (Documents and Video):
(True existing emails are displayed in this document, kindly refrain from contacting the email addresses shown within the document, thank you.)

[Link to document (Containing screenshots of user manual) >> CLICK HERE](https://cloudmails-my.sharepoint.com/:w:/g/personal/tp055637_mail_apu_edu_my/EbJZWb5KOJpOgm-Q9kTi2LgB5Wb13L3raIebHM2vqShQUw?e=aMBvq0)

[Download link if the link above didnt work >> CLICK HERE](https://github.com/chanhh01/FlyTranslate/files/12816943/FYP_Doc.docx)

[DEMO VIDEO >> CLICK HERE](https://cloudmails-my.sharepoint.com/:v:/g/personal/tp055637_mail_apu_edu_my/Ea9vvdbh9AxOrAAxSbwfrooBs_vc8oqWrl1Hik9kdvcgAA?e=SrM0bC)

General limitations of FlyTranslate:
1. Libraries are used instead of models (Model building for multi-lingual translation is very difficult)
2. Inability to detect source language automatically (EasyOCR separates recognition models with different font families. Cannot be selected all together)
3. Cannot extract text written vertically (Most OCR libraries limited to extract texts horizontally)
4. Inability to overlay text directly on top of device screen (Requires advanced expertise on pywin32, the scarce pywin32 documentation makes this nigh impossible)
5. Below average speed for core feature (Too many important functions lined up and iterated - unable to process parallelly)


Future enhancements in mind:
1. Find a way to pipeline processes on cloud - utilize higher computational speed to reduce core feature processing time, addressing limitation number 5.
2. Crowdsource open-source community - to build multi-language OCR that is capable of addressing limitation number 2 and 3.
3. Perform extensive research / receive professional training on developing win32 related functions using python to address limitation number 4.


To try it out yourself:
1. Download the project folder.
2. Make sure you have MySQL installed.
3. Execute db_schema_for_fyp.sql in MySQL (you may modify the database name).
4. Import language_list.sql in MySQL and make sure to select the chosen database name.
5. Modify [mysql_config.py](https://github.com/chanhh01/FlyTranslate/blob/master/mysql_config.py) to connect to your database.
6. Modify [repository/email_repo.py](https://github.com/chanhh01/FlyTranslate/blob/master/repository/email_repo.py) to change email sender and email password credentials. [Kindly follow this tutorial to set up a new email for this context](https://www.youtube.com/watch?v=zxFXnLEmnb4).
7. Run main.py.
