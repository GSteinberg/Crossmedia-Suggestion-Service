from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import shutil
import urllib
import os, ssl

def get_info(song, artist):
	# Using Chrome to access web
	bpm_driver = webdriver.Chrome()
	song_driver = webdriver.Chrome()

	# Open the website
	bpm_driver.get('https://getsongbpm.com/')
	song_driver.get('https://www.allmusic.com/')

	# Select the search box
	bpm_search_box = bpm_driver.find_element_by_name('search_db')
	song_search_box = song_driver.find_element_by_name('term')

	# Send search information
	bpm_search_box.send_keys(song)
	song_search_box.send_keys(song)

	# Find submit button
	bpm_submit_button = bpm_driver.find_element_by_css_selector(".fa.fa-search")
	song_submit_button = song_driver.find_element_by_class_name('site-search-button')

	# Click submit
	bpm_submit_button.click()
	song_submit_button.click()

	# Click correct search result
	artist_idx = 0
	bpm_artist_results = bpm_driver.find_elements_by_class_name('blur')
	for i, val in enumerate(bpm_artist_results):
		if val.text == artist:
			artist_idx = i
	bpm_song_results = bpm_driver.find_elements_by_xpath('//*[@href]')
	for i, val in enumerate(bpm_song_results):
		if song.lower().replace(' ', '-') in val.get_attribute('href'):
			bpm_song_results[i].click()
			break
	# ------------------------------------------------------------------------
	song_results = song_driver.find_elements_by_xpath('//*[@href]')
	for i, val in enumerate(song_results):
		if artist.lower().replace(' ', '-') in val.get_attribute('href'):
			song_results[i-1].click()
			break
			
	# Get energy info
	progress_bars = bpm_driver.find_elements_by_class_name('progress-bar')
	for bar in progress_bars:
		if bar.text == "Energy":
			energy = bar.get_attribute('style').strip("width: %;")
	if 0 <= int(energy) <= 45:
		energy = "low"
	elif 45 < int(energy) <= 70:
		energy = "med"
	else:
		energy = "high"
		
	# Get year
	song_year = song_driver.find_element_by_class_name('song-release-year-text').text

	# Get album cover
	album_cover = song_driver.find_element_by_class_name('lazy')
	album_cover.click()
	# Get src text
	image = song_driver.find_element_by_class_name("media-gallery-image")
	img_src = image.get_attribute("src")

	if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None): 
		ssl._create_default_https_context = ssl._create_unverified_context
	
	print(img_src)
	
	urllib.request.urlretrieve(img_src, "album_cover.jpg")
	
	return [song_year, energy]

def main():
	song, artist = "Space Oddity, David Bowie".split(", ")
	print(get_info(song, artist))

main()

"""
 and i-31 == artist_idx
"""