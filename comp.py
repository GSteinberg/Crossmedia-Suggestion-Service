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

	ssim = compare_ssim(img1, img2, multichannel=True)
	similar_img.append((name,ssim))

def process_data(data):
    with open ('art_database.csv') as a_csv:
        paints = csv.reader(a_csv, delimiter=',')


        song_sty = ''
        song_mood = ''

        for m in musics:
            if m[0] == data:
                song_sty = m[1]
                song_mood = m[2]

        sel_by_style = []
        sel_by_mood = []

        for p in paints:
            if p[1] == song_sty:
                sel_by_style.append(p)
            if p[2] == song_mood:
                sel_by_mood.append(p)

    imagenames = []
    for i in sel_by_style:
        for j in sel_by_mood:
            if i[0] == j[0]:
                imagenames.append(i[0])

    return imagenames


sorted(similar_img,key=lambda l:l[1],reverse=True)
print(similar_img[1])
