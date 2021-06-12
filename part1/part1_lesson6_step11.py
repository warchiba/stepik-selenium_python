from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    el = browser.find_element_by_xpath(
        "//div[@class='first_block']/div[1]/label[text()='First name*']")
    el = browser.find_element_by_xpath(
        "//div[@class='first_block']/div[2]/label[text()='Last name*']")
    el = browser.find_element_by_xpath(
        "//div[@class='first_block']/div[3]/label[text()='Email*']")

    elements = browser.find_elements_by_css_selector("input[required]")
    for element in elements:
        element.send_keys("kk")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()