import numpy as np
import cv2

theta = np.radians(-45)
c, s = np.cos(theta), np.sin(theta)
R = np.eye(3)
R[0][0] = c
R[0][2] = s
R[2][2] = c
R[2][0] = -s

K = np.asarray([[  2.79090673e+03,   0.00000000e+00,   1.31897282e+03],
               [  0.00000000e+00,   2.82053910e+03,   1.55192556e+03],
               [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]])
               
H = K * R * np.linalg.inv(K)

targetSize = (8500,4000)

img = cv2.imread('result.jpg')

res = cv2.warpPerspective(img, H, targetSize)

cv2.imwrite('resultRotated.jpg', res)