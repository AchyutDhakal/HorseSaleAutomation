from utils.test_runner import create_driver
from pages.public_portal import PublicPortal
import allure
import pytest
from data.test_data import VALID_PUBLIC_PORTAL, VALID_DATA
from pages.login_page import LoginPage
from pages.register_entry import RegisterEntry
from selenium.webdriver.common.by import By
from utils.assertions import assert_true

class TestPublicPortal:
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://horse-sale.vercel.app/")

        self.public_portal = PublicPortal(self.driver)
        self.login_page = LoginPage(self.driver)
        self.register_entry = RegisterEntry(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Testing registering a horse entry through public portal")
    @pytest.mark.parametrize("valid_entry", VALID_PUBLIC_PORTAL)
    @pytest.mark.parametrize("login_data", VALID_DATA)
    def test_valid_horse_entry(self, valid_entry, login_data):
        with allure.step("Filling up the form"):
            self.public_portal.register_entry(valid_entry["email_address"],valid_entry["mobile_number"], valid_entry["first_name"], valid_entry["last_name"], valid_entry["address"], valid_entry["town"], valid_entry["postcode"], valid_entry["eq_number"], valid_entry["horse_name"], valid_entry["reg_number"], valid_entry["additional_performance"], valid_entry["date_of_birth"])


        with allure.step("Asserting entry finalization"):
            entry_status = self.public_portal.get_element_text(self.public_portal.ENTRY_STATUS)
            assert_true((entry_status == "Success"), "The entry status is not success","finalize_entry",self.public_portal)

        with allure.step("Logging in to the admin portal"):
            self.driver.get("https://horse-sale-app.vercel.app/login")
            self.login_page.login(login_data["email"], login_data["password"])

        with allure.step("Going the sales event"):
            self.register_entry.click_element(self.register_entry.SALES)
            print(f"//span[normalize-space()='{self.public_portal.event_text}']")
            EVENT_NAME = (By.XPATH,f"//span[normalize-space()='{self.public_portal.event_text}']")
            self.public_portal.click_element(EVENT_NAME)
            self.public_portal.click_element(self.register_entry.OVERVIEW_DROPDOWN)
            self.public_portal.click_element(self.register_entry.PRESALE)
            self.public_portal.click_element(self.public_portal.ENTRY)
        
        with allure.step("Assertion against the horse name"):
            horse_name = self.public_portal.get_element_text(self.public_portal.HORSE_NAME_ADMIN)
            assert_true((valid_entry["horse_name"] == horse_name),"The horse names don't match", "Valid_public_entry",self.public_portal)



        