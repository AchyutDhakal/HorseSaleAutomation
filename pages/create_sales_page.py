from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class CreateSalesPage(BasePage):
    SALES_BUTTON = (By.XPATH,"//span[normalize-space()='Sales']")
    CREATE_SALE = (By.XPATH,"//span[normalize-space()='Create Sale']")
    EVENT_NAME = (By.XPATH, "//input[@name='name']")
    DATE = (By.NAME, "startDateTimeUtc")
    CREATE_SALE_BUTTON =(By.XPATH, "//button[contains(@class,'bg-[#2D3839]') and .//span[normalize-space()='CREATE SALE']]")
    SALE_SCHEDULE =(By.XPATH,"//p[normalize-space()='Sale schedule']")
    EDIT_ICON = (By.XPATH,"//button[.//*[name()='path' and contains(@d,'M17 3')]]")
    CATEGORIES_DROPDOWN = (By.XPATH,"//span[normalize-space()='Select categories in priority order']")
    CATEGORIES_OPTIONS = (By.XPATH, "//div[contains(@class,'absolute') and contains(@class,'z-50')]//span[contains(@class,'text-zinc-700')]")
    MAX_LOT_NUMBERS =(By.XPATH, "//input[@name='maxNumberOfLots']")
    MAX_STABLES = (By.XPATH, "//input[@name='maxNumberOfStables']")
    SAVE_SCHEDULE =(By.XPATH,"//button[normalize-space()='Save Schedule']")
    INITIALIZE_SALE =(By.XPATH, "//span[normalize-space()='Initialise Sale']")
    POPUP_DISMISS_BUTTON = (By.XPATH, "//button[normalize-space()='OK']")
    POPUP_OVERLAY = (By.CSS_SELECTOR, "div.absolute.inset-0")
    EVENT_TITLE = (By.XPATH, "//h1[contains(@class,'tracking-tight') and contains(@class,'text-zinc-900')]")
    FINANCIAL = (By.XPATH,"//p[normalize-space()='Financial']")
    ENTRY_FEE_INPUT = (By.XPATH,"//input[contains(@class,'w-[90px]')]/following-sibling::span[normalize-space()='€']/preceding-sibling::input")
    SALE_SETTINGS_TEXT = (By.XPATH,"//p[normalize-space()='Sale Settings']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_financial_and_get_entry_fee(self):
        self.click_element(self.FINANCIAL)

    def create_sales_event(self, event_name, date, max_lot, max_stables, entry_fee):
        self.dismiss_popup_if_present()
        self.click_element(self.SALES_BUTTON)
        self.click_element(self.CREATE_SALE)
        self.enter_text(self.EVENT_NAME,event_name)
        self.enter_date(self.DATE, date)


        self.click_element(self.CREATE_SALE_BUTTON)
        self.click_element(self.FINANCIAL)

        self.wait.until(EC.presence_of_element_located(self.ENTRY_FEE_INPUT))
        self.wait.until(EC.element_to_be_clickable(self.ENTRY_FEE_INPUT))

        entry_fee_el = self.driver.find_element(*self.ENTRY_FEE_INPUT)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", entry_fee_el
        )

        ActionChains(self.driver)\
            .click(entry_fee_el)\
            .key_down(Keys.CONTROL)\
            .send_keys("a")\
            .key_up(Keys.CONTROL)\
            .send_keys(Keys.DELETE)\
            .send_keys(str(entry_fee))\
            .perform()

        # Wait for React to settle then RE-FIND the element
        time.sleep(0.5)
        entry_fee_el = self.driver.find_element(*self.ENTRY_FEE_INPUT)  # ✅ re-find
        actual = entry_fee_el.get_attribute("value")
        print(f"[DEBUG] Entry fee after ActionChains: '{actual}'")

        if actual != str(entry_fee):
            # One retry if value didn't stick
            ActionChains(self.driver)\
                .click(entry_fee_el)\
                .key_down(Keys.CONTROL)\
                .send_keys("a")\
                .key_up(Keys.CONTROL)\
                .send_keys(Keys.DELETE)\
                .send_keys(str(entry_fee))\
                .perform()
            time.sleep(0.5)
            entry_fee_el = self.driver.find_element(*self.ENTRY_FEE_INPUT)
            print(f"[DEBUG] Entry fee after retry: '{entry_fee_el.get_attribute('value')}'")

        self.click_element(self.SALE_SCHEDULE)
        self.click_element(self.EDIT_ICON)

        self.select_all_section_categories(self.CATEGORIES_DROPDOWN, self.CATEGORIES_OPTIONS)
        self.enter_text(self.MAX_LOT_NUMBERS,max_lot)
        self.enter_text(self.MAX_STABLES, max_stables)
        self.click_element(self.SAVE_SCHEDULE)

        self.wait.until(EC.invisibility_of_element_located(self.SAVE_SCHEDULE))
        self.click_element(self.INITIALIZE_SALE)
        self.wait.until(EC.invisibility_of_element_located(self.SALE_SETTINGS_TEXT))

