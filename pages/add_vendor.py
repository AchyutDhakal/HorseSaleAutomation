from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AddVendor(BasePage):
    VENDORS_BUTTON = (By.XPATH,"//span[normalize-space()='Vendors']")
    ADD_NEW_VENDOR_BUTTON = (By.XPATH,"//span[normalize-space()='Add New Vendor']")
    EMAIL_INPUT = (By.XPATH,"//input[@name='email']")
    MOBILE_NUMBER_INPUT = (By.XPATH,"//input[@name='mobileNumber']")
    FORMAL_TITLE_DROPDOWN = (By.XPATH,"//span[normalize-space()='Select title']")
    FORMAL_TITLE = (By.XPATH,"//span[normalize-space()='Mr']")
    FIRST_NAME_INPUT = (By.NAME,"firstName")
    LAST_NAME_INPUT = (By.NAME,"lastName")
    ADDRESS_LINE_1_INPUT = (By.NAME,"addressLine1")
    TOWN_INPUT = (By.NAME,"townCity")
    COUNTY_DROPDOWN = (By.XPATH,"//span[normalize-space()='Select county']")
    COUNTY = (By.XPATH,"//span[normalize-space()='Antrim']")
    POSTCODE_INPUT = (By.NAME,"postcode")
    COUNTRY_DROPDOWN = (By.XPATH,"//span[normalize-space()='Select country']")
    COUNTRY = (By.XPATH,"//span[normalize-space()='Ireland']")
    EQUINE_PREMISES_NUMBER_INPUT = (By.NAME,"equinePremisesNumber")
    FLAT_RATED_FARMER_NO = (By.XPATH,"(//label[normalize-space()='No'])[1]")
    VAT_REGISTERED_FARMER_NO = (By.XPATH,"(//label[normalize-space()='No'])[2]")
    CREATE_VENDOR_BUTTON = (By.XPATH,"//span[normalize-space()='Create Vendor Record']")
    EMAIL_ADDRESS = (By.XPATH,"//div[contains(@class,'text-[#7A7A7A]') and contains(@class,'min-w-0')]")
    SEARCH_BAR = (By.XPATH,"//input[@placeholder='Search Vendors...']")
    VENDOR = (By.XPATH,"//tbody/tr[1]")
    MOBILE_NUMBER = (By.XPATH,"//span[contains(normalize-space(),'Mobile Number')]/ancestor::div[contains(@class,'min-w-0')][1]//div[contains(@class,'bg-[#FAFAFA]') and contains(@class,'rounded-xl')]")

    def __init__(self, driver):
        super().__init__(driver)

    def add_vendor(self):
        self.click_element(self.VENDORS_BUTTON)
        self.click_element(self.ADD_NEW_VENDOR_BUTTON)
        self.click_element(self.FORMAL_TITLE_DROPDOWN)
        self.click_element(self.FORMAL_TITLE)
        self.click_element(self.COUNTY_DROPDOWN)
        self.click_element(self.COUNTY)
        self.click_element(self.COUNTRY_DROPDOWN)
        self.click_element(self.COUNTRY)
        self.click_element(self.FLAT_RATED_FARMER_NO)
        self.click_element(self.VAT_REGISTERED_FARMER_NO)



    