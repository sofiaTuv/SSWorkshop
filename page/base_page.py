from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def wait_until(self, path):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(path))
        return self.browser.find_element(*path)
