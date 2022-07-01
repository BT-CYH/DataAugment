import cv2
import imutils

img_path = "C:/Users/Administrator/Desktop/pose/origin/181.png"
save_path = "C:/Users/Administrator/Desktop/pose/rotate/1811.png"
image = cv2.imread(img_path)
#rotated = imutils.rotate(image, 25)
#cv2.imwrite(save_path, rotated)
rotated_round = imutils.rotate_bound(image, -20)
cv2.imwrite(save_path, rotated_round)
