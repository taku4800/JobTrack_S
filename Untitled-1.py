# coding: shift_jis
import pyocr
from PIL import Image
import pyocr.tesseract

pyocr.tesseract.TESSERACT_CMD=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]
print(tool.get_name())

image=Image.open("aaa.jpg")
# 画像からテキストを抽出する
text = tool.image_to_string(image,lang="jpn")

# 抽出したテキストを出力する
print(text)
      
print("hellow")