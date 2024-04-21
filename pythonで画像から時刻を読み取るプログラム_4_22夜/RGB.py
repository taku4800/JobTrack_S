import cv2
import numpy as np

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

cv2.imshow("Result BGR", resultBGR)
cv2.imshow("Result mask", maskBGR)

cv2.waitKey(0)
cv2.destroyAllWindows()