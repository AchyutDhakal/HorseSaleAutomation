from utils.test_runner import create_driver
from pages.login_page import LoginPage
from pages.create_sales_page import CreateSalesPage
import allure
import pytest
from data.test_data import VALID_DATA,SALES_DATA
from utils.assertions import assert_true, assert_false
import time

class TestCreateSales:
    def setup_method(self):
        self.driver = create_driver()
        self.driver.get("https://horse-sale-app.vercel.app/login")
        
        self.create_sales_page = CreateSalesPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Testing the creation of sales event")
    @pytest.mark.parametrize("valid_data",VALID_DATA)
    @pytest.mark.parametrize("sales_data",SALES_DATA)
    def test_create_sales_event(self, valid_data, sales_data):
        with allure.step("Logging in to the application"):
            self.login_page.login(valid_data["email"], valid_data["password"])

        with allure.step("Creating the sales event"):
            self.create_sales_page.create_sales_event(sales_data["event_name"], sales_data["date"], sales_data["max_lot"], sales_data["max_stables"])

        with allure.step("Assertion"):
            event_text = self.create_sales_page.get_element_text(self.create_sales_page.EVENT_TITLE).lower()
            assert_true(sales_data["event_name"].lower()==event_text,"The name of the event didn't match","sales_event_creation", self.create_sales_page)  
            assert_false(self.create_sales_page.is_element_present(self.create_sales_page.INITIALIZE_SALE),"Initialize sales button still present","sales_event_creation",self.create_sales_page)
        