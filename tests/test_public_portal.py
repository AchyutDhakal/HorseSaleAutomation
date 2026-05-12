from utils.test_runner import create_driver
from pages.public_portal import PublicPortal
import allure
import pytest
from data.public_entry_data import VALID_PUBLIC_PORTAL
from data.login_data import VALID_DATA
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
        with allure.step("Navigating to the entry form and Filling up email, phone number and the vendor details"):
            self.public_portal.fill_vendor_details(valid_entry["email_address"],valid_entry["mobile_number"], valid_entry["firstName"], valid_entry["lastName"], valid_entry["address.addressLine1"], valid_entry["address.townCity"], valid_entry["address.postcode"], valid_entry["equinePremisesNumber"])
    
        with allure.step("Clicking on upload documents later"):
            self.public_portal.click_element(self.public_portal.DOCUMENT_LATER)

        with allure.step("Filling up horse details"):
            self.public_portal.fill_form_dynamically(valid_entry)
            self.public_portal.click_element(self.public_portal.NEXT_STEP_BUTTON)
            self.public_portal.click_element(self.public_portal.NEXT_STEP_BUTTON)

        with allure.step("Filling up card details and clicking privacy policy checkboxes"):
            self.public_portal.fill_card_details()            

        with allure.step("Asserting entry finalization"):
            entry_status = self.public_portal.get_element_text(self.public_portal.ENTRY_STATUS)
            assert_true((entry_status == "Success"), "The entry status is not success","finalize_entry",self.public_portal)

        with allure.step("Logging in to the admin portal"):
            self.driver.get("https://horse-sale-app.vercel.app/login")
            self.login_page.login(login_data["email"], login_data["password"])

        with allure.step("Going the sales event"):
            self.public_portal.navigate_to_admin_sales()
        
        with allure.step("Assertion against the horse name"):
            horse_name = self.public_portal.get_element_text(self.public_portal.HORSE_NAME_ADMIN)
            assert_true((valid_entry["horses[0].horse.horseName"] == horse_name),"The horse names don't match", "Valid_public_entry",self.public_portal)



        