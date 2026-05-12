from utils.test_runner import create_driver
from pages.login_page import LoginPage
import pytest
from data.login_data import VALID_DATA, INVALID_DATA
import allure
import time
from utils.assertions import assert_true,assert_false

class TestLogin:
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://horse-sale-app.vercel.app/login")

        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("valid_data", VALID_DATA)
    @allure.title("Testing the login of app with valid data")
    def test_valid_login(self, valid_data):
        with allure.step("Filling up the login form"):
            self.login_page.enter_email(valid_data["email"])
            self.login_page.enter_password(valid_data["password"])

        with allure.step("Clicking login button"):
            self.login_page.click_signin()

        with allure.step("Assertion"):
            assert_true(self.login_page.is_element_clickable(self.login_page.LOGOUT_BUTTON), "logout button not present","valid_login",self.login_page)

    @pytest.mark.parametrize("invalid_data", INVALID_DATA)
    @allure.title("Testing the login of app with invalid data")
    def test_invalid_login(self,invalid_data):
        with allure.step("Filling up the login form"):
            self.login_page.enter_email(invalid_data["email"])
            self.login_page.enter_password(invalid_data["password"])

        with allure.step("Clicking login button"):
            self.login_page.click_signin()

        with allure.step("Assertion"):
            assert_false(self.login_page.is_element_clickable(self.login_page.LOGOUT_BUTTON), "logout button not present","invalid_login",self.login_page)