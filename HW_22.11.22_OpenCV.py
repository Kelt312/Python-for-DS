import cv2 as cv
import numpy as np
from glob import glob

'''img = cv.imread('C:/Users\Kelt\Pictures/Saved Pictures/1.jpg', 0) #читаем картинку
cv.imshow('gray', img) #окошко с картинкой
cv.waitKey(0) #эникей для закрытия окошка, как в паскале)))
cv.imwrite('2.png', img)'''

for img_name in glob('*.jpg'):
    img = cv.imread(img_name)
    img_name = img_name.replace("jpg", "png")
    cv.imwrite(img_name, img)