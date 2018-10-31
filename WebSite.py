import selenium 
from selenium import webdriver
import time



def Maps(Postcode):
	# Using Chrome to access web
	driver = webdriver.Chrome(executable_path=r'C:\Users\Kieran\Desktop\A.L.L Project\ChatBot\DiscordBot-master/chromedriver.exe')

	# Open the website
	driver.get("https://www.google.com/maps")
	Search_box = driver.find_element_by_id('searchboxinput')
	Search_box.send_keys(Postcode)
	Search_button = driver.find_element_by_id('searchbox-searchbutton')
	Search_button.click()
	time.sleep(3)
	msg = driver.current_url
	return msg
