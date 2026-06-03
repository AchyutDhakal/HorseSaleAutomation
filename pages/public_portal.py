from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.otp_reader import get_otp_from_email
import time
from selenium.webdriver.support import expected_conditions as EC
from config import CARD_NUMBER, EXPIRY_MONTH, EXPIRY_YEAR, CVV

class PublicPortal(BasePage):
    ENTER_HORSE_BUTTON = (By.XPATH,"(//a[normalize-space()='Enter a Horse'])[2]")
    EVENT = (By.XPATH,"//button[.//span[contains(@class,'font-bold') and contains(@class,'text-[14px]')]][1]")
    CONTINUE_BUTTON =(By.XPATH,"//button[normalize-space()='Continue']")
    EMAIL_INPUT = (By.XPATH,"//input[@type='email']")
    VERIFY_CODE_BUTTON = (By.XPATH,"//button[normalize-space()='Verify']")
    MOBILE_NUMBER_INPUT = (By.XPATH,"//input[@placeholder='87 123 4567']")
    NEXT_STEP_BUTTON = (By.XPATH,"//button[normalize-space()='Next step']")
    FORMAL_TITLE_DROPDOWN = (By.XPATH,"//label[.//span[contains(text(),'Formal title')]]//following-sibling::button")
    FORMAL_TITLE = (By.XPATH,"//button[normalize-space()='Mr.']")
    FIRST_NAME_INPUT = (By.XPATH,"//input[@placeholder='First name  ']")
    LAST_NAME_INPUT = (By.XPATH,"//input[@placeholder='Surname  ']")
    ADDRESS_LINE_1_INPUT = (By.XPATH,"//input[@name='address.addressLine1']")
    TOWN_INPUT = (By.XPATH,"//input[@placeholder='Town / City  ']")
    COUNTY_DROPDOWN = (By.XPATH,"//label[.//span[contains(text(),'County')]]//following-sibling::button")
    COUNTY = (By.XPATH,"//button[normalize-space()='Carlow']")
    POSTCODE_INPUT = (By.XPATH,"//input[@placeholder='Eircode / Postcode  ']")
    COUNTRY_DROPDOWN = (By.XPATH,"//label[.//span[contains(text(),'Country')]]//following-sibling::button")
    COUNTRY = (By.XPATH,"//button[normalize-space()='Ireland']")
    EQUINE_PREMISES_NUMBER_INPUT= (By.XPATH,"//input[@placeholder='Equine premises number  ']")
    DOCUMENT_LATER = (By.XPATH, "//button[normalize-space()='I WILL UPLOAD THESE LATER']")
    SECTION_CATEGORY = "horses[0].horse.sectionCategory"
    HORSE_NAME = (By.XPATH,"//input[@name='horses[0].horse.horseName']")
    REG_NUMBER = (By.XPATH,"//input[@name='horses[0].horse.registrationNumber']")
    CLASS = "horses[0].horse.class"
    HWSD_STATUS = "horses[0].horse.hwsdStatus"
    SEX = "horses[0].horse.sex"
    PRIMARY_COLOUR = "horses[0].horse.colour"
    DATE_OF_BIRTH = (By.XPATH,"//input[@name='horses[0].horse.dateOfBirth']")
    COUNTRY_OF_ORIGIN = "horses[0].horse.countryOfOrigin"
    ADDITIONAL_PERFORMANCE_DETAILS_INPUT = (By.XPATH,"//textarea[@name='horses[0].horse.performance.additionalPerformanceDetails']")
    TERMS_AND_CONDITION_CHECKBOX = (By.XPATH,"//span[normalize-space()='I accept the terms and conditions']")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH,"//span[normalize-space()='I accept the privacy policy']")
    CARD_NUMBER_INPUT = (By.XPATH,"//input[@placeholder='XXXX XXXX XXXX XXXX']")
    EXPIRY_MONTH_INPUT = (By.XPATH,"//input[@placeholder='MM']")
    EXPIRY_YEAR_INPUT = (By.XPATH,"//input[@placeholder='YYYY']")
    CVV_INPUT = (By.XPATH,"//input[@placeholder='123']")
    FINALIZE_ENTRY_BUTTON = (By.XPATH,"//button[contains(normalize-space(),'Finalise entry')]")
    OTP_INPUT = (By.ID,"otp")
    EMAIL_OTP_INPUTS = (By.CSS_SELECTOR, "div.justify-between > input[inputmode='numeric']")
    HEIGHT = "horses[0].horse.height"
    AGE = "horses[0].horse.age"
    VERIFY_AND_CONTINUE_BUTTON = (By.ID,"verify-btn")
    PAYMENT_WINDOW_LOCATOR = (By.XPATH,"//iframe")
    RETURN_TO_HOMEPAGE_BUTTON = (By.XPATH,"//a[normalize-space()='Return to Homepage']")
    ENTRY = (By.XPATH,"//table//tbody/tr[1]")
    HORSE_NAME_ADMIN = (By.XPATH,"//table//tbody/tr[1]//td[6]//span[contains(@class,'font-semibold')]")
    POPUP_DISMISS_BUTTON = (By.XPATH, "//button[normalize-space()='No thanks']")
    POPUP_OVERLAY = (By.CSS_SELECTOR, "div.absolute.inset-0")
    ENTRY_STATUS = (By.XPATH,"(//div[.//span[normalize-space()='Entry status']]//span[last()])[2]")
    SEARCH_ENTRY = (By.XPATH,"//input[@placeholder='Search by Name, Lot#, or vendor...']")
    SEARCH_EVENT = (By.XPATH,"//input[@placeholder='Search sales...']")
    OVERVIEW_DROPDOWN = (By.XPATH,"(//span[normalize-space()='Overview'])[1]")
    PRESALE = (By.XPATH, "//span[normalize-space()='Pre-Sale']")
    SALES = (By.XPATH,"//span[normalize-space()='Sales']")
    INVALID_PHONE_ERROR = (By.XPATH,"//p[contains(@class,'text-red-500') and contains(@class,'text-xs') and contains(@class,'font-medium')]")
    CARD_NAME=(By.XPATH,"//input[@placeholder='John Doe']")
    ADDRESS_LINE_2 = (By.NAME,"address.addressLine2")
    BUSINESS_NAME = (By.NAME,"businessName")
    VAT_NUMBER = (By.NAME,"vatRegistrationNumber")
    PPS_NUMBER = (By.NAME,"ppsNumber")
    FLAT_RATED_YES = (By.XPATH,"//input[@name='flat_farm' and @value='yes']")
    VAT_REGISTERED_YES = (By.CSS_SELECTOR,"input[name='vat_farm'][value='yes']")
    COMPLETE_LATER_BUTTON = (By.XPATH,"//button[normalize-space()='Complete Later']")
    DISCLAIMER = (By.XPATH,"//h4[text()='Disclaimer']")



    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_sales(self):
        self.click_element(self.ENTER_HORSE_BUTTON)

        if(self.is_element_clickable(self.EVENT)==False):
            raise ValueError("No sales event available")
        
        else:
            self.event_text = self.get_element_text(self.EVENT).splitlines()[0]
            self.click_element(self.EVENT)
        self.click_element(self.CONTINUE_BUTTON)

    def fill_email(self, email_address):
        self.enter_text(self.EMAIL_INPUT,email_address)

    def fill_otp(self):
        self.enter_otp(self.EMAIL_OTP_INPUTS,get_otp_from_email())
        self.click_element(self.VERIFY_CODE_BUTTON)

    def fill_mobile_number(self, mobile_number):
        self.enter_text(self.MOBILE_NUMBER_INPUT, mobile_number)
        self.click_element(self.NEXT_STEP_BUTTON)

        
    def fill_vendor_details(self, first_name, last_name, address, town, postcode, eq_number, formal_title, county, country):
        if formal_title is not None:
            self.click_element(self.FORMAL_TITLE_DROPDOWN)
            self.click_element(self.FORMAL_TITLE)

        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.ADDRESS_LINE_1_INPUT, address)
        self.enter_text(self.TOWN_INPUT, town)
        if county is not None:
            self.click_element(self.COUNTY_DROPDOWN)
            self.click_element(self.COUNTY)

        self.enter_text(self.POSTCODE_INPUT, postcode)

        if country is not None:
            self.click_element(self.COUNTRY_DROPDOWN)
            self.click_element(self.COUNTRY)
        self.enter_text(self.EQUINE_PREMISES_NUMBER_INPUT, eq_number)


    def fill_card_details(self, card_name):
        self.click_element(self.TERMS_AND_CONDITION_CHECKBOX)
        self.click_element(self.PRIVACY_POLICY_CHECKBOX)
        self.enter_text(self.CARD_NAME, card_name)
        self.enter_text(self.CARD_NUMBER_INPUT, CARD_NUMBER)
        self.enter_text(self.EXPIRY_MONTH_INPUT, EXPIRY_MONTH)
        self.enter_text(self.EXPIRY_YEAR_INPUT, EXPIRY_YEAR)
        self.enter_text(self.CVV_INPUT, CVV)
        self.click_element(self.FINALIZE_ENTRY_BUTTON)
        self.enter_3ds_otp()
        self.wait.until(lambda d: self.is_element_visible(self.RETURN_TO_HOMEPAGE_BUTTON))
            
            
    def navigate_to_admin_sales(self):
        self.click_element(self.SALES)
        self.enter_text(self.SEARCH_EVENT, self.event_text)
        EVENT_NAME = (By.XPATH,f"//span[normalize-space()='{self.event_text}']")
        self.click_element(EVENT_NAME)
        self.click_element(self.OVERVIEW_DROPDOWN)
        self.click_element(self.PRESALE)
        self.click_element(self.ENTRY)

