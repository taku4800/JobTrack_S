# coding: shift_jis
import pyocr
from PIL import Image
import pyocr.tesseract

pyocr.tesseract.TESSERACT_CMD=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]
print(tool.get_name())

image=Image.open("aaa.jpg")
# �摜����e�L�X�g�𒊏o����
text = tool.image_to_string(image,lang="jpn")

# ���o�����e�L�X�g���o�͂���
print(text)
      
print("hellow")