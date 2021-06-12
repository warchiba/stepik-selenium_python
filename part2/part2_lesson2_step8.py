from selenium import webdriver
import time
import os

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/file_input.html"
	browser.get(link)

	firstname = browser.find_element_by_css_selector("[name='firstname']")
	firstname.send_keys("Kira")

	lastname = browser.find_element_by_css_selector("[name='lastname']")
	lastname.send_keys("K")

	mail = browser.find_element_by_css_selector("[name='email']")
	mail.send_keys("mail.ru")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'text.txt')

	send_file = browser.find_element_by_css_selector("[type='file']")
	send_file.send_keys(file_path)

	button = browser.find_element_by_css_selector("[type='submit']")
	button.click()
finally:
	time.sleep(3)
	browser.quit()
