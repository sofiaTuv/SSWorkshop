from page.base_page import BasePage
from page.paths import Paths


class MethodsPage(BasePage, Paths):
    def click_button(self):
        self.wait_until(self.BUTTON).click()

    def enter_postcode(self, text):
        self.wait_until(self.POSTCODE).send_keys(text)

    def enter_first_name(self, text):
        self.wait_until(self.FIRST_NAME).send_keys(text)

    def enter_last_name(self, text):
        self.wait_until(self.LAST_NAME).send_keys(text)

    def click_add_button(self):
        self.wait_until(self.ADD_BUTTON).click()
