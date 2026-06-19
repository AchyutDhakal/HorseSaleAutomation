from utils.test_runner import create_driver
from config import BASE_URL
from pages.login_page import LoginPage
from pages.add_vendor import AddVendor
import allure
import pytest
from data.add_vendor_data import VENDOR_DATA, INVALID_VENDOR_DATA
from data.login_data import VALID_DATA
import time
from utils.assertions import assert_equal, assert_true
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
            self.add_vendor.click_element(self.add_vendor.VENDOR)
            self.add_vendor.wait.until(
                lambda d: d.find_element(*self.add_vendor.MOBILE_NUMBER).text not in ['-', '', None]
            )
            actual_mobile_number = self.add_vendor.get_element_text(self.add_vendor.MOBILE_NUMBER)
            expected_mobile_number = "+353"+" "+f"{vendor_data['mobileNumber']}"
            assert_equal(actual_mobile_number, expected_mobile_number, "The mobile numbers doesn't match","valid_add_vendor",self.add_vendor)


    @allure.title("Testing the invalid vendor details")
    @pytest.mark.parametrize("invalid_vendor",INVALID_VENDOR_DATA)
    @pytest.mark.parametrize("login_data",VALID_DATA)
    def test_invalid_vendor(self, invalid_vendor, login_data):
        with allure.step("Logging in to the application"):
            self.login_page.login(login_data["email"], login_data["password"])

        with allure.step("Navigating to Horse registration form and selecting dropdowns"):
            self.add_vendor.invalid_vendor(invalid_vendor["formal_title"], invalid_vendor["county"], invalid_vendor["country"], invalid_vendor["flat_farmer"], invalid_vendor["pps_number"], invalid_vendor["vat_farmer"], invalid_vendor["vat_number"])

        with allure.step("Filling up the input fields of the form"):
            self.add_vendor.fill_form_dynamically(invalid_vendor)

        with allure.step("Clicking the submit button"):
            self.add_vendor.click_element(self.add_vendor.CREATE_VENDOR_BUTTON)

        with allure.step("Assertion"):
            assert_true(self.add_vendor.is_element_present(self.add_vendor.FORM_ERROR_MESSAGE),"invalid vendor details allowed", "invalid_vendor_crm", self.add_vendor)