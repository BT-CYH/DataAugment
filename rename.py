import os
import sys
import cv2

#input_path = "E:/leetcode/Data-Augment-master/img_new/"
#output_path = "E:/leetcode/Data-Augment-master/img_final/"

input_path = "C:/Users/Administrator/Desktop/dlc2/image/"
output_path = "C:/Users/Administrator/Desktop/dlc2/new/"

file_name = os.listdir(input_path)


count = 250
for file in file_name:
    name = file.split('.')[0]
    img0 = cv2.imread(input_path + file)
    #img1 = cv2.cvtColor(img0, cv2.COLOR_RGB2GRAY)
    #cv2.imwrite(output_path + file, img1)
    img1 = cv2.resize(img0, (853, 853))
    #img2 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(output_path + str(count) +".jpg", img1)
    #os.rename(input_path+file, output_path + str(count) +".jpg")
    count += 1