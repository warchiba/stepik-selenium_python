from selenium import webdriver
import time
import math


def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


try:
	link = "http://suninjuly.github.io/get_attribute.html"
	browser = webdriver.Chrome()
	browser.get(link)

	treasure = browser.find_element_by_css_selector("#treasure")
	x = treasure.get_attribute("valuex")
	y = calc(x)

	element = browser.find_element_by_css_selector("#answer")
	element.send_keys(y)

	checkbox = browser.find_element_by_css_selector("#robotCheckbox")
	checkbox.click()

	radiobutton = browser.find_element_by_css_selector("#robotsRule")
	radiobutton.click()

	submit_button = browser.find_element_by_css_selector("[type='submit']")
	submit_button.click()
finally:
	time.sleep(10)
	browser.quit()
