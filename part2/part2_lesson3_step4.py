from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/alert_accept.html"
	browser.get(link)

	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()

	alert = browser.switch_to.alert
	alert.accept()

	x = int(browser.find_element_by_css_selector("#input_value").text)
	y = math.log(abs(12 * math.sin(x)))

	answer = browser.find_element_by_css_selector("#answer")
	answer.send_keys(str(y))

	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
finally:
	time.sleep(10)
	browser.quit()
