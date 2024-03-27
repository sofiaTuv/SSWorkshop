from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PAGE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.PAGE_URL)

    def wait_until(self, path):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(path))
        return self.browser.find_element(*path)

    def alert_is_present(self):
        return WebDriverWait(self.browser, 5).until(EC.alert_is_present())
