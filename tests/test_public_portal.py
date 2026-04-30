from utils.test_runner import create_driver
from pages.public_portal import PublicPortal
import allure
import pytest
from data.test_data import VALID_PUBLIC_PORTAL

class TestPublicPortal:
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://horse-sale.vercel.app/")

        self.public_portal = PublicPortal(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Testing registering a horse entry through public portal")
    @pytest.mark.parametrize("valid_entry", VALID_PUBLIC_PORTAL)
    def test_valid_horse_entry(self, valid_entry):
        with allure.step("Filling up the form"):
            self.public_portal.register_entry(valid_entry["email_address"],valid_entry["mobile_number"], valid_entry["first_name"], valid_entry["last_name"], valid_entry["address"], valid_entry["town"], valid_entry["postcode"], valid_entry["eq_number"], valid_entry["horse_name"], valid_entry["reg_number"], valid_entry["additional_performance"])

