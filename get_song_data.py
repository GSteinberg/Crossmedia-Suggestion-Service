from bs4 import BeautifulSoup
from selenium import webdriver

song, artist = "Space Oddity, David Bowie".split(", ")

# Using Chrome to access web
#bpm_driver = webdriver.Chrome()
song_driver = webdriver.Chrome()

# Open the website
#bpm_driver.get('https://getsongbpm.com/')
song_driver.get('https://www.allmusic.com/')

# Select the search box
#bpm_search_box = bpm_driver.find_element_by_name('search_db')
song_search_box = song_driver.find_element_by_name('term')

# Send search information
#bpm_search_box.send_keys(song)
song_search_box.send_keys(song)

# Find submit button
#bpm_submit_button = bpm_driver.find_element_by_css_selector(".fa.fa-search")
song_submit_button = song_driver.find_element_by_class_name('site-search-button')

# Click submit
#bpm_submit_button.click()
song_submit_button.click()

# Click correct search result
#TODO for bpm
results = song_driver.find_elements_by_xpath('//*[@href]')
for i, val in enumerate(results):
	if artist.lower().replace(' ', '-') in val.get_attribute('href'):
		results[i-1].click()
		break
		
# Get energy info

		
# Get year
song_year = song_driver.find_element_by_class_name('song-release-year-text').text

# Get album cover
album_cover = song_driver.find_element_by_class_name('lazy')
album_cover.click()
album_cover = song_driver.find_element_by_class_name('media-gall')



























"""
# Find search results
#bpm_results_artist = bpm_driver.find_elements_by_partial_link_text(artist)
#bpm_results_song = bpm_driver.find_elements_by_partial_link_text(song)
song_results_artist = song_driver.find_elements_by_partial_link_text(artist)
song_results_song = song_driver.find_elements_by_partial_link_text(song)
print(song_results_song)

# If song doesn't exist
if len(song_results_artist) == 0 or len(song_results_song) == 0 or \
   len(bpm_results_artist) == 0 or len(bpm_results_song) == 0:
   print("Sorry! We can't find a song by that artist")

# Click song link
#bpm_results_song.click()
#song_results_song.click()
   

results = song_driver.find_elements_by_xpath('//*[@href]')

for i, val in enumerate(results):
	if val.get_attribute('class') == 'performers':
		if val.text.split('by ')[1:] == [artist]:
			print(results[i-1].get_attribute('href'))
			
	
#bpm_search_result1 = bpm_driver.find_elements_by_css_selector()
#bpm_search_result2 = bpm_driver.find_elements_by_css_selector(artist)
song_search_result1 = song_driver.find_element_by_css_selector('div.title')
song_search_result2 = song_driver.find_elements_by_css_selector('div.performers')

# If song doesn't exist

if len(bpm_search_result1) == 0 or len(bpm_search_result2) == 0 or \
   len(song_search_result1) == 0 or len(song_search_result2) == 0:
	print("Sorry! We can't find a song by that artist")
	#exit()

	#bpm_search_results = bpm_driver.find_elements_by_class_name('search_results')
song_search_results = song_driver.find_elements_by_class_name('search-results')
"""