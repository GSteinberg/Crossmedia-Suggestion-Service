from skimage.measure import compare_ssim
from scipy.misc import imread
import numpy as np
import os
import csv

def similarity(cover):
    img1 = imread(cover)
    similar_img = []
    for img in os.listdir('/home/yma73/Desktop/hackathon/images/'):
        name = img
        img2 = imread(img)
        img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))

        ssim = compare_ssim(img1, img2, multichannel=True)
        similar_img.append((name,ssim))

        sorted(similar_img,key=lambda l:l[1],reverse=True)
        return similar_img[1]

def process_data(data):
  
	with open ('C:/Users/my/Desktop/hack/static/art_database.csv','r', encoding='UTF-8') as a_csv:
		paints = csv.reader(a_csv, delimiter=',')
		song, artist = data.split(", ")
		song_year, song_mood = get_info(song, artist)
		sel_by_mood = []
		sel_by_year = []
		for p in paints:
			if p[2] == song_mood:
				sel_by_mood.append(p)
			#if int(p[1]) <= song_year + 10 and int(p[1]) >= song_year - 10:
			#	sel_by_year.append(p)

       # sel_by_cover = similarity(song_cover)


		imagenames = {}
		imagenames = set()
		for i in sel_by_mood:
			#for j in sel_by_year:
			#	imagenames.add(j[0])
			imagenames.add(i[0])
		return imagenames
