from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AddVendor(BasePage):
    VENDORS_BUTTON = (By.XPATH,"//span[normalize-space()='Sales']")
    ADD_NEW_VENDOR_BUTTON = (By.XPATH,"//span[normalize-space()='Add New Vendor']")
    EMAIL_INPUT = (By.XPATH,"//input[@name='email']")
    MOBILE_NUMBER_INPUT = (By.XPATH,"//input[@name='mobileNumber']")
    