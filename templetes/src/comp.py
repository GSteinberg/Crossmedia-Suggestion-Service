from skimage.measure import compare_ssim
from scipy.misc import imread
import numpy as np
import os
 
img1 = imread('cover.jpg')
similar_img = []
for img in os.listdir('/home/yma73/Desktop/hackathon/images/'):
	name = img
	img2 = imread(img)
	img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
 
#print(img2.shape)
#print(img1.shape)
	ssim = compare_ssim(img1, img2, multichannel=True)
	similar_img.append((name,ssim))
#print(len(similar_img))
sorted(similar_img,key=lambda l:l[1],reverse=True)
print(similar_img[1])