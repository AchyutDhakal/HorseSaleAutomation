from utils.test_runner import create_driver
from pages.public_portal import PublicPortal
import allure
import pytest
from data.public_entry_data import VALID_PUBLIC_PORTAL, INVALID_PUBLIC_PORTAL
from data.login_data import VALID_DATA
from pages.login_page import LoginPage
from pages.register_entry import RegisterEntry
from utils.assertions import assert_true, assert_false


class TestPublicPortal:
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://horse-sale.vercel.app/")

        self.public_portal = PublicPortal(self.driver)
        self.login_page = LoginPage(self.driver)
        self.register_entry = RegisterEntry(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Testing registering a horse entry through public portal using valid data")
    @pytest.mark.parametrize("entry_data", VALID_PUBLIC_PORTAL)
    @pytest.mark.parametrize("login_data", VALID_DATA)
    def test_valid_horse_entry(self, entry_data, login_data):
        with allure.step("Navigating to the entry form"):
            self.public_portal.navigate_to_entry_form(entry_data["email_address"],entry_data["mobile_number"])
            self.public_portal.click_element(self.public_portal.CONTINUE_BUTTON)

        with allure.step("Filling up vendor details"):
            self.public_portal.fill_vendor_details(entry_data["firstName"], entry_data["lastName"], entry_data["address.addressLine1"], entry_data["address.townCity"], entry_data["address.postcode"], entry_data["equinePremisesNumber"], entry_data["formal_title"], entry_data["county"], entry_data["country"])
            self.public_portal.click_element(self.public_portal.NEXT_STEP_BUTTON)

    
        with allure.step("Clicking on upload documents later"):
            self.public_portal.click_element(self.public_portal.DOCUMENT_LATER)

        with allure.step("Filling up horse details"):
            self.public_portal.fill_form_dynamically(entry_data)
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
            assert_true((entry_data["horses[0].horse.horseName"] == horse_name),"The horse names don't match", "Valid_public_entry",self.public_portal)


    @allure.title("Testing registering a horse entry through public portal using invalid data")
    @pytest.mark.parametrize("entry_data",INVALID_PUBLIC_PORTAL)
    def test_invalid_horse_entry(self, entry_data):
        with allure.step("Navigating to the entry form"):
            self.public_portal.navigate_to_entry_form(entry_data["email_address"],entry_data["mobile_number"])

        with allure.step("Asserting mobile number"):
            if(len(entry_data["mobile_number"]) == 0):
                self.public_portal.click_element(self.public_portal.CONTINUE_BUTTON)

            if self.public_portal.is_element_visible(self.public_portal.INVALID_PHONE_ERROR):
                assert_true(self.public_portal.is_element_visible(self.public_portal.INVALID_PHONE_ERROR),"Invalid mobile number allowed","invalid_mobile_number",self.public_portal)
                return
            else:
                self.public_portal.click_element(self.public_portal.CONTINUE_BUTTON)

        with allure.step("Filling up vendor details"):
            self.public_portal.fill_vendor_details(entry_data["firstName"], entry_data["lastName"], entry_data["address.addressLine1"], entry_data["address.townCity"], entry_data["address.postcode"], entry_data["equinePremisesNumber"], entry_data["formal_title"], entry_data["county"], entry_data["country"])

        with allure.step("Assert vendor details"):
            if self.public_portal.is_element_clickable(self.public_portal.NEXT_STEP_BUTTON):
                assert_false(self.public_portal.is_element_clickable(self.public_portal.NEXT_STEP_BUTTON),"Invalid vendor details allowed","invalid_vendor_details", self.public_portal)
                self.public_portal.click_element(self.public_portal.NEXT_STEP_BUTTON)
                return

   
        with allure.step("Clicking on upload documents later"):
            self.public_portal.click_element(self.public_portal.DOCUMENT_LATER)

        with allure.step("Filling up horse details"):
            self.public_portal.fill_form_dynamically(entry_data)
            self.public_portal.click_element(self.public_portal.NEXT_STEP_BUTTON)
            self.public_portal.click_element(self.public_portal.NEXT_STEP_BUTTON)

        with allure.step("Filling up card details and clicking privacy policy checkboxes"):
            self.public_portal.fill_card_details()            

        with allure.step("Asserting entry finalization"):
            entry_status = self.public_portal.get_element_text(self.public_portal.ENTRY_STATUS)
            assert_true((entry_status == "Success"), "The entry status is not success","finalize_entry",self.public_portal)


        