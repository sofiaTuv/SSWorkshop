import allure
from helper import Helper
from page.methods_page import MethodsPage


@allure.tag('web')
@allure.title('Создание клиента (Add Customer)')
class TestAddCustomer:
    def test_add_customer(self, browser):
        with allure.step("Открытие главной страницы"):
            page = MethodsPage(browser)
            page.open()

        with allure.step("Открытие страницы регистрации 'Add customer'"):
            page.click_button_add_customer()

        with allure.step("Создание почтового индекса нового клиента"):
            postcode = Helper.generate_code()
            page.enter_postcode(postcode)

        with allure.step("Создание имени"):
            fname = Helper.generate_name(postcode)
            page.enter_first_name(fname)

        with allure.step("Создание фамилии"):
            lname = Helper.generate_last_name()
            page.enter_last_name(lname)

        with allure.step("Проверка успешной регистрации"):
            page.click_add_button()
            assert page.alert_visible_message() == 'Customer added successfully with customer id :'
            page.accept_alert()
