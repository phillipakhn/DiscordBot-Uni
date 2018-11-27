import selenium 
from selenium import webdriver
import time


'''Function: Runs a chrome browser, inserts the postcode into the search bar, searches and then returns the URL.
Innput: String (Postcode), Output: String (msg)'''
def Maps(Postcode):
	# Using Chrome to access web
	driver = webdriver.Chrome(executable_path=r'C:\Users\Kieran\Desktop\A.L.L Project\ChatBot\DiscordBot-master\Selenium Maps/chromedriver.exe')

	# Open the website
	driver.get("https://www.google.com/maps")
	Search_box = driver.find_element_by_id('searchboxinput') # The search box in Google Maps.
	Search_box.send_keys(Postcode) # Inserts "Postcode" into the seach box
	Search_button = driver.find_element_by_id('searchbox-searchbutton') # The search button in Google Maps
	Search_button.click()
	time.sleep(3) # Waits 3 seconds otherwise it returns None.
	msg = driver.current_url # Sets the Url to "msg"
	return msg



