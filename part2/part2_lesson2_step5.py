from selenium import webdriver
import time

try:
	browser = webdriver.Chrome()
	link = "https://SunInJuly.github.io/execute_script.html"
	browser.get(link)
	button = browser.find_element_by_tag_name("button")
	button.click()
	assert True
finally:
	time.sleep(10)
	browser.quit()
