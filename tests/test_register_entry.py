from utils.test_runner import create_driver
from pages.login_page import LoginPage
from pages.create_sales_page import CreateSalesPage
from pages.register_entry import RegisterEntry
import allure
import pytest
from data.test_data import VALID_DATA, ENTRY_DATA, INVALID_ENTRY_DATA
from utils.assertions import assert_true, assert_false
import time
from config import BASE_URL
from selenium.webdriver.common.by import By

class TestRegisterEntry:
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get(BASE_URL)

        self.login_page = LoginPage(self.driver)
        self.create_sales_page = CreateSalesPage(self.driver)
        self.register_entry = RegisterEntry(self.driver)

    def teardown_method(self):
        self.driver.quit()


    @allure.title("Testing the process of registering a new general entry through admin portal")
    @pytest.mark.parametrize("entry_data", ENTRY_DATA)
    @pytest.mark.parametrize("login_data", VALID_DATA)
    def test_register_entry(self, entry_data, login_data):
        with allure.step("Logging in to the application"):
            self.login_page.login(login_data["email"], login_data["password"])

        with allure.step("Registering a new entry"):
            self.register_entry.register_entry(entry_data["reg_num"], entry_data["horse_name"], entry_data["date_of_birth"], entry_data["additional_info"], entry_data["consignor_name"], entry_data["consignor_mobile"],entry_data["consignor"] )

        with allure.step("Assertion"):
            assert_false(self.register_entry.is_element_present(self.register_entry.ERROR_CONTAINER),"Error messages are displayed","valid_register_entry", self.register_entry)


    @allure.title("Testing the process of registering a new general entry through admin portal using invalid data")
    @pytest.mark.parametrize("entry_data", INVALID_ENTRY_DATA)
    @pytest.mark.parametrize("login_data", VALID_DATA)
    def test_invalid_register_entry(self, entry_data, login_data):
        with allure.step("Logging in to the application"):
            self.login_page.login(login_data["email"], login_data["password"])

        with allure.step("Registering a new entry"):
            self.register_entry.register_entry(entry_data["reg_num"], entry_data["horse_name"], entry_data["date_of_birth"], entry_data["additional_info"], entry_data["consignor_name"], entry_data["consignor_mobile"],entry_data["consignor"] )

        with allure.step("Assertion"):
            time.sleep(5)
            assert_true(self.register_entry.is_element_visible(self.register_entry.ERROR_CONTAINER),"Assertion failed as  the entry was registered for invalid data","Invalid_entry", self.register_entry)