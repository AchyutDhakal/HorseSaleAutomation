from utils.test_runner import create_driver
from config import BASE_URL
from pages.login_page import LoginPage
from pages.add_vendor import AddVendor
import allure 
import pytest
from data.add_vendor_data import VENDOR_DATA
from data.login_data import VALID_DATA
import time
from utils.assertions import assert_equal
from selenium.webdriver.support import expected_conditions as EC

class TestAddVendor:
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get(BASE_URL)

        self.login_page = LoginPage(self.driver)
        self.add_vendor = AddVendor(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Testing the registration of vendor with valid data")
    @pytest.mark.parametrize("login_data",VALID_DATA)
    @pytest.mark.parametrize("vendor_data",VENDOR_DATA)
    def test_add_vendor(self, login_data, vendor_data):
        with allure.step("Logging in to the application"):
            self.login_page.login(login_data["email"], login_data["password"])

        with allure.step("Navigating to Horse registration form and selecting dropdowns"):
            self.add_vendor.add_vendor()

        with allure.step("Filling up the input fields of the form"):
            self.add_vendor.fill_form_dynamically(vendor_data)

        with allure.step("Clicking the submit button"):
            self.add_vendor.click_element(self.add_vendor.CREATE_VENDOR_BUTTON)

        with allure.step("Assertion against the email address"):
            self.add_vendor.wait.until(EC.element_to_be_clickable(self.add_vendor.ADD_NEW_VENDOR_BUTTON))
            self.add_vendor.wait.until(EC.invisibility_of_element_located(self.add_vendor.EMAIL_INPUT))
            self.add_vendor.enter_text(self.add_vendor.SEARCH_BAR,vendor_data["email"])
            email = self.add_vendor.get_element_text(self.add_vendor.EMAIL_ADDRESS)
            assert_equal(email,vendor_data["email"], "The email address does not match","add_vendor",self.add_vendor)
