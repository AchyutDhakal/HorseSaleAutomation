from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CreateSalesPage(BasePage):
    SALES_BUTTON = (By.XPATH,"//span[normalize-space()='Sales']")
    CREATE_SALE = (By.XPATH,"//span[normalize-space()='Create Sale']")
    EVENT_NAME = (By.XPATH, "//input[@name='name']")
    DATE = (By.NAME, "startDateTimeUtc")
    CREATE_SALE_BUTTON =(By.XPATH, "//button[contains(@class,'bg-[#2D3839]') and .//span[normalize-space()='CREATE SALE']]")
    SALE_SCHEDULE =(By.XPATH,"//p[normalize-space()='Sale schedule']")
    EDIT_ICON = (By.XPATH,"//button[.//*[name()='path' and contains(@d,'M17 3')]]")
    CATEGORIES_DROPDOWN = (By.XPATH,"//span[normalize-space()='Select categories in priority order']")
    CHECKBOX1 = (By.XPATH,"//span[normalize-space()='Foal']")
    CHECKBOX2 = (By.XPATH,"(//span[normalize-space()='Ponies'])[2]")
    CHECKBOX3 = (By.XPATH,"//span[normalize-space()='Yearling']")
    CHECKBOX4 = (By.XPATH,"//span[normalize-space()='TwoYo']")
    CHECKBOX5 = (By.XPATH,"//span[normalize-space()='ThreeYo']")
    CHECKBOX6 = (By.XPATH,"//span[normalize-space()='FourYo']")
    CHECKBOX7 = (By.XPATH,"//span[normalize-space()='FiveYoPlus']")
    CHECKBOX8 = (By.XPATH,"(//span[normalize-space()='Broodmare'])[2]")
    CHECKBOX9 = (By.XPATH,"//span[normalize-space()='BroodmareWithFoal']")

    MAX_LOT_NUMBERS =(By.XPATH, "//input[@name='maxNumberOfLots']")
    MAX_STABLES = (By.XPATH, "//input[@name='maxNumberOfStables']")
    SAVE_SCHEDULE =(By.XPATH,"//button[normalize-space()='Save Schedule']")
    INITIALIZE_SALE =(By.XPATH, "//span[normalize-space()='Initialize Sale']")
    POPUP_DISMISS_BUTTON = (By.XPATH, "//button[normalize-space()='OK']")
    POPUP_OVERLAY = (By.CSS_SELECTOR, "div.absolute.inset-0")
    EVENT_TITLE = (By.XPATH, "//h1[contains(@class,'tracking-tight') and contains(@class,'text-zinc-900')]")

    def __init__(self, driver):
        super().__init__(driver)


    def dismiss_popup_if_present(self):
        try:
            dismiss_btn = self.wait.until(
                EC.element_to_be_clickable(self.POPUP_DISMISS_BUTTON)
            )
            dismiss_btn.click()
            self.wait.WebDriverWait(self.driver, 5).until(
               EC.invisibility_of_element_located(self.POPUP_OVERLAY)
            )
        except TimeoutException:
            pass 

    def create_sales_event(self, event_name, date, max_lot, max_stables):
        self.dismiss_popup_if_present()
        self.click_element(self.SALES_BUTTON)
        self.click_element(self.CREATE_SALE)
        self.enter_text(self.EVENT_NAME,event_name)
        self.enter_date(self.DATE, date)
        self.click_element(self.CREATE_SALE_BUTTON)
        self.click_element(self.SALE_SCHEDULE)
        self.click_element(self.EDIT_ICON)
        self.click_element(self.CATEGORIES_DROPDOWN)
        self.click_element(self.CHECKBOX1)
        self.click_element(self.CHECKBOX2)
        self.click_element(self.CHECKBOX3)
        self.click_element(self.CHECKBOX4)
        self.click_element(self.CHECKBOX5)
        self.click_element(self.CHECKBOX6)
        self.click_element(self.CHECKBOX7)
        self.click_element(self.CHECKBOX8)
        self.click_element(self.CHECKBOX9)
        self.enter_text(self.MAX_LOT_NUMBERS,max_lot)
        self.enter_text(self.MAX_STABLES, max_stables)
        self.click_element(self.SAVE_SCHEDULE)
        self.click_element(self.INITIALIZE_SALE)
        self.wait.until(EC.presence_of_element_located(self.EVENT_TITLE))
