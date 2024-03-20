from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from helper import generate_code, generate_name, generate_last_name

URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'

browser = webdriver.Chrome()
browser.get(URL)
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@ng-class="btnClass1"]')))
button.click()


postcode = generate_code()
postCode = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH,'//input[@ng-model="postCd"]'))).send_keys(postcode)

fname = generate_name(postcode)
firstName = browser.find_element(By.XPATH,'//input[@ng-model="fName"]').send_keys(fname)

lname = generate_last_name()
lastName = browser.find_element(By.XPATH, '//input[@ng-model="lName"]').send_keys(lname)



