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
    CLOSE_PRESALE = (By.XPATH,"//button[normalize-space()='Close Pre-Sale']")
    BREEDING_YES = (By.XPATH,"//label[contains(text(),'Is breeding recorded?')]/..//button[normalize-space()='Yes']")
    DISEASE_TEST = (By.XPATH,"//label[contains(text(),'Has this Connemara been tested for Hoof Wall Separation Disease?')]/..//button[normalize-space()='Yes']")
    STATUS = (By.XPATH,"//div[contains(@class,'items-start') and contains(@class,'flex-wrap')]/span")


    def __init__(self,driver):
        super().__init__(driver)


    def register_entry(self):
        self.click_element(self.SALES)
        self.wait.until(EC.presence_of_element_located(self.EVENT_NAME))
        self.wait.until(EC.element_to_be_clickable(self.EVENT_NAME))
        self.wait.until(EC.visibility_of_element_located(self.EVENT_NAME))
        self.click_element(self.ENTRY)

        status = self.get_element_text(self.STATUS).lower()
        if status == "draft":
            self.take_screenshot("draft_event")
            raise AssertionError("The event is in draft")

        self.wait.until(EC.element_to_be_clickable(self.OVERVIEW_DROPDOWN))
        self.click_element(self.OVERVIEW_DROPDOWN)
        self.click_element(self.PRESALE)

        if self.is_element_visible(self.CLOSE_PRESALE):
            pass
        else:
            self.click_element(self.OPEN_PRESALE)


        if self.is_element_clickable(self.ADD_GENERAL_ENTRY):
            pass
        else:
            self.click_element(self.OPEN_GENERAL)

        # self.wait_and_click_add_general_entry()
        time.sleep(1)
        self.click_element(self.ADD_GENERAL_ENTRY)



       
        





