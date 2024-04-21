import cv2#画像を読み取るのにcs2とimage.openがあるので注意！
import numpy as np
from PIL import Image,ImageOps

img = cv2.imread('b.jpg')

#青を抽出
bgr = [25,25,25]
thresh = 3

#色の閾値
minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

#画像の2値化
maskBGR = cv2.inRange(img,minBGR,maxBGR)
#画像のマスク（合成）
resultBGR = cv2.bitwise_and(img, img, mask = maskBGR)



image = resultBGR
cv2.imshow("aa", resultBGR)

# 画像をグレースケールに変換する
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2値化する
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 輪郭を検出する
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 各輪郭を近似する
for contour in contours:
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    # 近似した輪郭が4つの頂点を持つ場合（四角形として処理）
    if len(approx) == 4:
        # 頂点の座標を取得して表示する
        for point in approx:
            x, y = point.ravel()
            cv2.circle(image, (x, y), 3, (0, 255, 0), -1)
            cv2.putText(image, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)

# 結果を表示する
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()