from selenium import webdriver
import time
import math

try:
	browser = webdriver.Chrome()
	link = "http://SunInJuly.github.io/execute_script.html"
	browser.get(link)

	x = int(browser.find_element_by_css_selector("#input_value").text)
	y = math.log(abs(12 * math.sin(x)))

	answer = browser.find_element_by_css_selector("#answer")
	answer.send_keys(str(y))

	robotCheckbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
	robotCheckbox.click()

	robotRules = browser.find_element_by_css_selector("#robotsRule")
	robotRules.click()

	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
finally:
	time.sleep(10)
	browser.quit()
