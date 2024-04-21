#目標：画像の時刻と駅名のところが背景灰色なので、そこを読み取るのがカギ？
#今のところ、時刻がある写真の左を切り取って、OCRで数数:数数の文字列を読み取るのが精一杯
import csv
import re

import pyocr #OCR画像を文字として
from PIL import Image,ImageOps
import pyocr.tesseract

# CSVファイルのパス
csv_file_path = "output.csv"

pyocr.tesseract.TESSERACT_CMD=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]
print(tool.get_name())

image=Image.open("b.jpg")#画像を読み取るのにcs2とimage.openがあるので注意！
print(image.size[1])
image = image.crop((0, 0, 180, image.size[1]-70))
#image_gray = image.convert('L')#白黒にする
image = ImageOps.invert(image.convert('RGB'))#色を逆転する

# 画像からテキストを抽出する
text = tool.image_to_string(image,lang="jpn",builder = pyocr.builders.TextBuilder(tesseract_layout=6))

# 画像の表示
image.show()

print(text)

text_tikan=re.sub('[^0-9:\n]',"",text)#0-9:\n以外の文字を空白"”に置き換え
print("\n置換したもの---------------------------------\n"+text_tikan)

text_spline = text_tikan.splitlines()
#print(text_spline)

# 正規表現パターン
pattern = r'\b\d{2}:\d{2}\b'

# 置換処理
matches = re.findall(pattern, text_tikan)

# 空白を除いたマッチのリストを作成
matches_cleaned = [match for match in matches if match.strip()]

print(matches_cleaned)

# 数字2つ:数字2つか改行以外のすべての文字列を空白に置き換える正規表現パターン


# CSVファイルにテキストデータを書き込む
with open(csv_file_path, mode='w', newline='', encoding='shift_jis') as file:
    writer = csv.writer(file)
    writer.writerows(text)


print("CSVファイルにテキストデータを保存しました。")