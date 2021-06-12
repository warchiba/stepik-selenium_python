from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
	browser = webdriver.Chrome()
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser.get(link)

	button = browser.find_element_by_id("book")
	WebDriverWait(browser, 15).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100")
	)
	button.click()

	x = int(browser.find_element_by_css_selector("#input_value").text)
	y = math.log(abs(12 * math.sin(x)))

	answer = browser.find_element_by_css_selector("#answer")
	answer.send_keys(str(y))

	button = browser.find_element_by_css_selector("#solve")
	button.click()
finally:
	time.sleep(10)
	browser.quit()
