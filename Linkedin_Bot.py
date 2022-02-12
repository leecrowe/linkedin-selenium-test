from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import constants as _constants

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.linkedin.com')
time.sleep(2)

#LOG IN

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

username.send_keys(_constants.EMAIL)
password.send_keys(_constants.PASS)
time.sleep(2)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()

#ADDING CONTACTS

driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH")
time.sleep(2)

all_buttons = driver.find_elements("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(2)
