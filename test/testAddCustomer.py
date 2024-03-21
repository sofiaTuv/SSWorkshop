from helper import Helper
from page.methods_page import MethodsPage


URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'


class TestAddCustomer:
    def test_add_customer(self, browser):
        page = MethodsPage(browser)
        browser.get(URL)
        page.click_button()

        postcode = Helper.generate_code()

        page.enter_postcode(postcode)

        fname = Helper.generate_name(postcode)
        page.enter_first_name(fname)

        lname = Helper.generate_last_name()
        page.enter_last_name(lname)

        page.click_add_button()
