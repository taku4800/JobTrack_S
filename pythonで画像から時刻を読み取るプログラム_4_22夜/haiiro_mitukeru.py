import cv2
import numpy as np

# 画像を読み込む
image = cv2.imread('b.jpg')

# 画像をHSV形式に変換する
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 灰色の範囲を定義する（H: 0-180, S: 0-255, V: 0-255）
lower_gray = np.array([0, 0, 100], dtype=np.uint8)
upper_gray = np.array([0, 255, 100], dtype=np.uint8)

# 画像内の灰色の部分をマスクする
mask = cv2.inRange(hsv_image, lower_gray, upper_gray)

# 輪郭を見つける
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 輪郭を描画する
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 結果を表示する
cv2.imshow('Gray Areas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
