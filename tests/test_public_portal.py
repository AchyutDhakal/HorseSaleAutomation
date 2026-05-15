from utils.test_runner import create_driver
from pages.public_portal import PublicPortal
import allure
import pytest
from data.public_entry_data import VALID_PUBLIC_PORTAL, INVALID_EMAIL_ADDRESS, INVALID_MOBILE_NUMBER
from data.login_data import VALID_DATA
from pages.login_page import LoginPage
from pages.register_entry import RegisterEntry
from utils.assertions import assert_true, assert_false
import time


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
        with allure.step("Navigating to the sales events"):
            self.public_portal.navigate_to_sales()
            self.public_portal.click_element(self.public_portal.CONTINUE_BUTTON)

        with allure.step("Fill up email_address"):
            self.public_portal.fill_email(entry_data["email_address"])
            self.public_portal.click_element(self.public_portal.CONTINUE_BUTTON)

        with allure.step("Fill up otp"):
            self.public_portal.fill_otp()

        with allure.step("Fill up mobile number"):
            self.public_portal.fill_mobile_number(entry_data["mobile_number"])
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
            self.public_portal.fill_card_details(entry_data["card_name"])            

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

    @allure.title("Testing invalid email address")
    @pytest.mark.parametrize("invalid_email",INVALID_EMAIL_ADDRESS)
    def test_invalid_email(self, invalid_email):
        with allure.step("Navigate to sales"):
            self.public_portal.navigate_to_sales()

        with allure.step("Fill up email address"):
            self.public_portal.fill_email(invalid_email["email_address"])

        with allure.step("Assertion"):
            if (self.public_portal.is_element_clickable(self.public_portal.CONTINUE_BUTTON)):
                self.public_portal.click_element(self.public_portal.CONTINUE_BUTTON)
                assert_false(self.public_portal.is_element_present(self.public_portal.  VERIFY_CODE_BUTTON),"Invalid email address allowed","invalid_email",self.public_portal)

            else:
                assert_false(self.public_portal.is_element_clickable(self.public_portal.CONTINUE_BUTTON),"Invalid email address allowed","invalid_email",self.public_portal)


    @allure.title("Testing invalid mobile number")
    @pytest.mark.parametrize("valid_data", VALID_PUBLIC_PORTAL)
    @pytest.mark.parametrize("invalid_mobile", INVALID_MOBILE_NUMBER)
    def test_invalid_mobile_number(self, valid_data, invalid_mobile):
        with allure.step("Navigating to the sales"):
            self.public_portal.navigate_to_sales()

        with allure.step("Filling up email"):
            self.public_portal.fill_email(valid_data["email_address"])
            self.public_portal.click_element(self.public_portal.CONTINUE_BUTTON)

        with allure.step("Filing up otp"):
            self.public_portal.fill_otp()

        with allure.step("Filling up mobile number"):
            self.public_portal.fill_mobile_number(invalid_mobile["mobile_number"])

        with allure.step("Assertion"):
            pass


