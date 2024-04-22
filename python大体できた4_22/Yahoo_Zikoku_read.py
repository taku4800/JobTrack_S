#目標：画像の時刻と駅名のところが背景灰色なので、そこを読み取るのがカギ？
#今のところ、時刻がある写真の左を切り取って、OCRで数数:数数の文字列を読み取るのが精一杯
#./image/IMG_2968 2.PNGにYahoo乗り換えのスクショを入れて、output.csvに時刻を横並びに出すプログラム
import csv
import re

import pyocr #OCR画像を文字として
from PIL import Image,ImageOps
import pyocr.tesseract

#与えられた画像と場所からトリミング
def imagecut(image,square):
    #print(square)
    toumei_crop = image.split()[-1].getbbox()#透明じゃない部分
    alpha_image= image.crop(toumei_crop)#透明な部分が邪魔だから切り抜き
    cutimage= alpha_image.crop(square)
    cutimage = ImageOps.invert(cutimage.convert('RGB'))#色を逆転する 清水のがダークモードで白字だったので黒字になる
    cutimage = cutimage.convert('L')#白黒にする
    """
    lamdaは無名関数、ifの前に書かれているものが、読み込まれる(ややこしい)
    値が230以下は0になる
    x<230のときx=0で黒、それ以外は白にする。
    x<250とかにすれば、時刻と駅名の灰色背景の部分が黒になるので、場所を特定できるかも
    """
    cutimage= cutimage.point(lambda x: 0 if x < 210 else 255)   
    
    # 画像の表示
    cutimage.show()
    return cutimage


# CSVファイルのパス
csv_file_path = "output.csv"

#OCRの準備
pyocr.tesseract.TESSERACT_CMD=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]
#print(tool.get_name())

image=Image.open("./image/a.PNG")#画像を読み取るのにcs2とimage.openがあるので注意！
image = imagecut(image,(0, 200, 120, image.size[1]-100))




# 画像からテキストを抽出する(まだ日本語とかある状態)
text = tool.image_to_string(image,lang="jpn",builder = pyocr.builders.TextBuilder(tesseract_layout=6))
#print(text)

#0-9:\n以外の文字を空白"”に置き換え　手順1
text_tikan=re.sub('[^0-9:\n]',"",text)
print("\n置換したもの--------\n"+text_tikan)
text_spline = text_tikan.splitlines()
#print(text_spline)

# 正規表現パターン-------------手順2
pattern = r'\b\d{2}:\d{2}\b'
# 置換処理
matches = re.findall(pattern, text_tikan)
# 空白を除いたマッチのリストを作成
# 数字2つ:数字2つ(12:34みたいな時刻)か改行以外のすべての文字列を空白に置き換えるらしい？
matches_cleaned = [match for match in matches if match.strip()]
print(matches_cleaned)



# CSVファイルにテキストデータを書き込む
with open(csv_file_path, mode='w', newline='', encoding='shift_jis') as file:
    writer = csv.writer(file)
    writer.writerow(matches_cleaned)
print("CSVファイルにテキストデータを保存しました。")

