from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

class RegisterEntry(BasePage):
    OVERVIEW_DROPDOWN = (By.XPATH,"(//span[normalize-space()='Overview'])[1]")
    PRESALE = (By.XPATH, "//span[normalize-space()='Pre-Sale']")
    ADD_GENERAL_ENTRY = (By.XPATH,"//span[normalize-space()='Add General entry']")
    REG_NUM = (By.XPATH,"//input[@name='horse.registrationNumber']")
    HEIGHT_DROPDOWN = (By.XPATH,"//span[normalize-space()='Select height…']")
    HEIGHT = (By.XPATH,"//span[normalize-space()='12.2h - 128cm']")
    HORSE_NAME =(By.XPATH,"//input[@name='HorseName']")
    CLASS_DROPDOWN = (By.XPATH,"//select[@name='Class']/parent::div")
    CLASS = (By.XPATH,"//span[normalize-space()='Class OH']")
    DATE_OF_BIRTH = (By.XPATH,"//input[@name='DateOfBirth']")
    ADDITIONAL_PERFORMANCE_DETAILS = (By.XPATH,"//input[@name='AdditionalPerformanceDetails']")
    CONFIRM_REGISTRATION = (By.XPATH,"//button[@type='submit' and contains(@class,'bg-[#2D3839]')]")
    ENTRY = (By.XPATH,"//tbody/tr[1]")
    ENTRY_HORSE_NAME = (By.XPATH, "//h3[contains(@class,'font-bold') and contains(@class,'truncate')]")
    ERROR_CONTAINER = (By.XPATH,"//div[contains(@class,'bg-red-50') and contains(@class,'border-red-200')]")
    ERROR_MESSAGE = (By.XPATH,"//div[contains(@class,'bg-red-50')]//li")
    CONSIGNOR_YES = (By.XPATH, "//label[contains(text(),'Consignor')]/..//button[normalize-space()='Yes']")
    CONSIGNOR_NO = (By.XPATH, "//label[contains(text(),'Consignor')]/..//button[normalize-space()='No']")
    CONSIGNOR_NAME = (By.XPATH,"//input[@placeholder = 'e.g. John Smith']")
    CONSIGNOR_MOBILE = (By.XPATH,"//input[@placeholder = '87 123 4567']")
    SALES = (By.XPATH,"//span[normalize-space()='Sales']")
    EVENT_NAME = (By.XPATH,"(//tbody/tr[1]//span[contains(@class,'font-semibold') and contains(@class,'text-[#142D14]') and contains(@class,'truncate')])[1]")
    OPEN_GENERAL = (By.XPATH,"//span[normalize-space()='Open general entries']")
    OPEN_PRESALE = (By.XPATH,"//button[normalize-space()='Open Pre-Sale']")


    def __init__(self,driver):
        super().__init__(driver)


    def register_entry(self, reg_num, horse_name, date_of_birth, additional_info, consignor_name, consignor_mobile, consignor):
        self.click_element(self.SALES)
        # self.get_element_text(self.EVENT_NAME)
        self.wait.until(EC.presence_of_element_located(self.EVENT_NAME))
        self.wait.until(EC.element_to_be_clickable(self.EVENT_NAME))
        self.wait.until(EC.visibility_of_element_located(self.EVENT_NAME))
        # time.sleep(5)
        self.click_element(self.ENTRY)
        self.wait.until(EC.element_to_be_clickable(self.OVERVIEW_DROPDOWN))
        self.click_element(self.OVERVIEW_DROPDOWN)
        self.click_element(self.PRESALE)

        if self.is_element_visible(self.OPEN_PRESALE):
            self.click_element(self.OPEN_PRESALE)

        if self.is_element_visible(self.OPEN_GENERAL):
            self.click_element(self.OPEN_GENERAL)

        self.click_element(self.ADD_GENERAL_ENTRY)

        vendor_name = self.get_name_by_index("vendorId")
        self.select_custom_dropdown("vendorId", vendor_name)
        self.select_custom_dropdown("sectionCategory", self.get_name_by_index("sectionCategory"))

        if consignor == 'Yes':
            self.click_element(self.CONSIGNOR_YES)
            self.wait.until(EC.element_to_be_clickable(self.CONSIGNOR_NAME))
            self.enter_text(self.CONSIGNOR_NAME, consignor_name)
            self.enter_text(self.CONSIGNOR_MOBILE,consignor_mobile)

        else:
            self.click_element(self.CONSIGNOR_NO)


        self.enter_text(self.REG_NUM, reg_num)
        self.select_custom_dropdown("horse.sex",self.get_name_by_index("horse.sex"))
        self.select_custom_dropdown("horse.colour",self.get_name_by_index("horse.colour"))
        self.select_custom_dropdown("horse.height",self.get_name_by_index("horse.height"))
        self.enter_text(self.HORSE_NAME, horse_name)
        # self.select_custom_dropdown("Class",self.get_name_by_index("Class"))
        # self.select_custom_dropdown("HwsdStatus", self.get_name_by_index("HwsdStatus"))
        # self.select_custom_dropdown("CountryOfOrigin",self.get_name_by_index("CountryOfOrigin"))

        # if date_of_birth is not None:
        #     self.enter_date(self.DATE_OF_BIRTH,date_of_birth)
        

        self.select_custom_dropdown("StageOfTraining",self.get_name_by_index("StageOfTraining"))
        self.select_custom_dropdown("StageOfLunging", self.get_name_by_index("StageOfLunging"))
        # self.enter_text(self.ADDITIONAL_PERFORMANCE_DETAILS, additional_info)
        self.click_element(self.CONFIRM_REGISTRATION)
        





