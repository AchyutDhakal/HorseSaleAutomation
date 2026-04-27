from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

class RegisterEntry(BasePage):
    OVERVIEW_DROPDOWN = (By.XPATH,"(//span[normalize-space()='Overview'])[1]")
    PRESALE = (By.XPATH, "//span[normalize-space()='Pre-Sale']")
    ADD_GENERAL_ENTRY = (By.XPATH,"//span[normalize-space()='Add General entry']")
    VENDOR_DROPDOWN = (By.XPATH, "//span[normalize-space()='Select vendor']")
    VENDOR_NAME = (By.XPATH,"//span[normalize-space()='Mr. John Moran']")
    REG_NUM = (By.XPATH,"//input[@name='horse.registrationNumber']")
    SEX_DROPDOWN = (By.XPATH, "//select[@name='horse.sex']/parent::div")
    SEX = (By.XPATH,"//span[normalize-space()='Filly']")
    PRIMARY_COLOUR_DROPDOWN = (By.XPATH, "//span[normalize-space()='Select colour…']")
    PRIMARY_COLOUR = (By.XPATH,"//span[normalize-space()='Gray']")
    HEIGHT_DROPDOWN = (By.XPATH,"//span[normalize-space()='Select height…']")
    HEIGHT = (By.XPATH,"//span[normalize-space()='12.2h - 128cm']")
    HORSE_NAME =(By.XPATH,"//input[@name='HorseName']")
    CLASS_DROPDOWN = (By.XPATH,"//select[@name='Class']/parent::div")
    CLASS = (By.XPATH,"//span[normalize-space()='Class OH']")
    COUNTRY_OF_ORIGIN_DROPDOWN= (By.XPATH,"//select[@name='CountryOfOrigin']/parent::div")
    COUNTRY_OF_ORIGIN = (By.XPATH,"//span[normalize-space()='Ireland']")
    DATE_OF_BIRTH = (By.XPATH,"//input[@name='DateOfBirth']")
    STAGE_OF_TRAINING_DROPDOWN = (By.XPATH,"//select[@name='StageOfTraining']/parent::div")
    STAGE_OF_TRAINING = (By.XPATH,"//span[normalize-space()='Unbroken']")
    STAGE_OF_LUNGING_DROPDOWN = (By.XPATH,"//select[@name='StageOfLunging']/parent::div")
    STAGE_OF_LUNGING = (By.XPATH,"//span[normalize-space()='Not Lunging']")
    ADDITIONAL_PERFORMANCE_DETAILS = (By.XPATH,"//input[@name='AdditionalPerformanceDetails']")
    CONFIRM_REGISTRATION = (By.XPATH,"//button[@type='submit' and contains(@class,'bg-[#2D3839]')]")
    ENTRY = (By.XPATH,"//tbody/tr[1]")
    ENTRY_HORSE_NAME = (By.XPATH, "//h3[contains(@class,'font-bold') and contains(@class,'truncate')]")
    ERROR_CONTAINER = (By.XPATH,"//div[contains(@class,'bg-red-50') and contains(@class,'border-red-200')]")
    ERROR_MESSAGE = (By.XPATH,"//div[contains(@class,'bg-red-50')]//li")


    def __init__(self,driver):
        super().__init__(driver)

    def register_entry(self, reg_num, horse_name, date_of_birth, additional_info, vendor_name, sex, colour, height, class_name, country_of_origin, stage_of_training, stage_of_lunging, hwsd_status):
        self.click_element(self.OVERVIEW_DROPDOWN)
        self.click_element(self.PRESALE)
        self.click_element(self.ADD_GENERAL_ENTRY)
        self.select_custom_dropdown("vendorId", vendor_name)
        self.enter_text(self.REG_NUM, reg_num)
        self.select_custom_dropdown("horse.sex",sex)
        self.select_custom_dropdown("horse.colour",colour)
        self.select_custom_dropdown("horse.height",height)
        self.enter_text(self.HORSE_NAME, horse_name)
        self.select_custom_dropdown("Class",class_name)
        self.select_custom_dropdown("HwsdStatus", hwsd_status)
        self.select_custom_dropdown("CountryOfOrigin",country_of_origin)
        self.enter_date(self.DATE_OF_BIRTH,date_of_birth)
        self.select_custom_dropdown("StageOfTraining",stage_of_training)
        self.select_custom_dropdown("StageOfLunging", stage_of_lunging)
        self.enter_text(self.ADDITIONAL_PERFORMANCE_DETAILS, additional_info)
        self.click_element(self.CONFIRM_REGISTRATION)
        # self.wait.until(EC.invisibility_of_element_located(self.CONFIRM_REGISTRATION))


