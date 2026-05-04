from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.otp_reader import get_otp_from_email
import time
from config import CARD_NUMBER, EXPIRY_MONTH, EXPIRY_YEAR, CVV
from selenium.webdriver.support import expected_conditions as EC

class PublicPortal(BasePage):
    ENTER_HORSE_BUTTON = (By.XPATH,"(//a[normalize-space()='Enter a Horse'])[2]")
    EVENT = (By.XPATH,"//button[.//span[contains(@class,'font-bold') and contains(@class,'text-[14px]')]][2]")
    CONTINUE_BUTTON =(By.XPATH,"//button[normalize-space()='Continue']")
    EMAIL_INPUT = (By.XPATH,"//input[@type='email']")
    VERIFY_CODE_BUTTON = (By.XPATH,"//button[normalize-space()='Verify code']")
    MOBILE_NUMBER_INPUT = (By.XPATH,"//input[@placeholder='87 123 4567']")
    NEXT_STEP_BUTTON = (By.XPATH,"//button[normalize-space()='Next step']")
    FORMAL_TITLE_DROPDOWN = (By.XPATH,"//button[.//span[normalize-space()='Please select...']]")
    FORMAL_TITLE = (By.XPATH,"//button[normalize-space()='Mr.']")
    FIRST_NAME_INPUT = (By.XPATH,"//input[@placeholder='First name  ']")
    LAST_NAME_INPUT = (By.XPATH,"//input[@placeholder='Surname  ']")
    ADDRESS_LINE_1_INPUT = (By.XPATH,"//input[@name='address.addressLine1']")
    TOWN_INPUT = (By.XPATH,"//input[@placeholder='Town / City  ']")
    COUNTY_DROPDOWN = (By.XPATH,"(//span[normalize-space()='Please select...'])[1]")
    COUNTY = (By.XPATH,"//button[normalize-space()='Carlow']")
    POSTCODE_INPUT = (By.XPATH,"//input[@placeholder='Eircode / Postcode  ']")
    COUNTRY_DROPDOWN = (By.XPATH,"//span[normalize-space()='Please select...']")
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
    EMAIL_OTP_INPUTS = (By.XPATH, "//input[@inputmode='numeric' and @type='tel']")
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




    def __init__(self, driver):
        super().__init__(driver)

    def register_entry(self, email_address, mobile_number, first_name, last_name, address, town, postcode, eq_number, horse_name, reg_number, additional_performance, date_of_birth):
        self.dismiss_popup_if_present()
        self.click_element(self.ENTER_HORSE_BUTTON)

        if(self.is_element_clickable(self.EVENT)==False):
            raise ValueError("No sales event available")
        
        else:
            self.event_text = self.get_element_text(self.EVENT).splitlines()[0]
            print(self.event_text)
            self.click_element(self.EVENT)

        self.click_element(self.CONTINUE_BUTTON)
        self.enter_text(self.EMAIL_INPUT,email_address)
        self.click_element(self.CONTINUE_BUTTON)
        self.enter_otp(self.EMAIL_OTP_INPUTS,get_otp_from_email())
        self.click_element(self.VERIFY_CODE_BUTTON)
        self.enter_text(self.MOBILE_NUMBER_INPUT, mobile_number)
        self.click_element(self.NEXT_STEP_BUTTON)
        self.click_element(self.CONTINUE_BUTTON)
        self.click_element(self.FORMAL_TITLE_DROPDOWN)
        self.click_element(self.FORMAL_TITLE)
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.ADDRESS_LINE_1_INPUT, address)
        self.enter_text(self.TOWN_INPUT, town)
        self.click_element(self.COUNTY_DROPDOWN)
        self.click_element(self.COUNTY)
        self.enter_text(self.POSTCODE_INPUT, postcode)
        self.click_element(self.COUNTRY_DROPDOWN)
        self.click_element(self.COUNTRY)
        self.enter_text(self.EQUINE_PREMISES_NUMBER_INPUT, eq_number)
        self.click_element(self.NEXT_STEP_BUTTON)
        self.click_element(self.DOCUMENT_LATER)

        self.handle_save_address_popup()
        self.select_custom_dropdown(self.SECTION_CATEGORY, self.get_name_by_index(self.SECTION_CATEGORY))
        self.enter_text(self.HORSE_NAME, horse_name)
        self.enter_text(self.REG_NUMBER, reg_number)
        self.select_custom_dropdown(self.SEX, self.get_name_by_index(self.SEX))
        self.select_custom_dropdown(self.PRIMARY_COLOUR, self.get_name_by_index(self.PRIMARY_COLOUR))
        self.select_custom_dropdown(self.HEIGHT, self.get_name_by_index(self.HEIGHT))
        self.select_custom_dropdown(self.AGE, self.get_name_by_index(self.AGE))
        self.select_custom_dropdown("horses[0].horse.class", self.get_name_by_index("horses[0].horse.class"))
        self.select_custom_dropdown("horses[0].horse.hwsdStatus", self.get_name_by_index("horses[0].horse.hwsdStatus"))
        self.enter_date(self.DATE_OF_BIRTH, date_of_birth)
        self.select_custom_dropdown("horses[0].horse.countryOfOrigin", self.get_name_by_index("horses[0].horse.countryOfOrigin"))
        self.select_custom_dropdown("horses[0].horse.performance.stageOfTraining", self.get_name_by_index("horses[0].horse.performance.stageOfTraining"))
        self.select_custom_dropdown("horses[0].horse.performance.stageOfLunging", self.get_name_by_index("horses[0].horse.performance.stageOfLunging"))
        self.enter_text(self.ADDITIONAL_PERFORMANCE_DETAILS_INPUT, additional_performance)
        self.click_element(self.NEXT_STEP_BUTTON)
        self.click_element(self.NEXT_STEP_BUTTON)
        self.click_element(self.TERMS_AND_CONDITION_CHECKBOX)
        self.click_element(self.PRIVACY_POLICY_CHECKBOX)
        self.enter_text(self.CARD_NUMBER_INPUT, CARD_NUMBER)
        self.enter_text(self.EXPIRY_MONTH_INPUT, EXPIRY_MONTH)
        self.enter_text(self.EXPIRY_YEAR_INPUT, EXPIRY_YEAR)
        self.enter_text(self.CVV_INPUT, CVV)
        self.click_element(self.FINALIZE_ENTRY_BUTTON)
       
        self.enter_3ds_otp()

        self.wait.until(lambda d: self.is_element_visible(self.RETURN_TO_HOMEPAGE_BUTTON))

            
            


