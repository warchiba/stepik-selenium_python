from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
	link = "http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)

	num1_element = browser.find_element_by_css_selector("#num1")
	num1 = int(num1_element.text)

	num2_element = browser.find_element_by_css_selector("#num2")
	num2 = int(num2_element.text)

	result = num1 + num2

	select = Select(browser.find_element_by_css_selector("#dropdown"))
	select.select_by_visible_text(str(result))

	submit_button = browser.find_element_by_css_selector("[type='submit']")
	submit_button.click()
finally:
	time.sleep(10)
	browser.quit()
