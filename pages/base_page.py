from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

class BasePage:
    # OVERLAY = (By.XPATH, "//div[contains(@class,'backdrop-blur-sm') and contains(@class,'opacity-100')]")
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    
    def find_element(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_clickable_element(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def find_visible_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    # def wait_for_overlay_to_disappear(self):
    #     try:
    #         self.wait.until(
    #             EC.invisibility_of_element_located(self.OVERLAY)
    #         )
    #     except TimeoutException:
    #         pass
    
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].value = '';", element)  
        element.click()  
        element.send_keys(text)  

    def click_element(self, locator):
        # self.wait_for_overlay_to_disappear()
        element = self.find_clickable_element(locator)
        # try:
        #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
        # except ElementClickInterceptedException:
        #     # Another element is overlapping — wait briefly and try JS click
        #     self.wait.until(
        #         lambda d: d.execute_script("return document.readyState") == "complete"
        #     )
        #     self.driver.execute_script("arguments[0].click();", element)

    def get_element_text(self,locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_present(self,locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False
        
    def is_element_clickable(self,locator):
        try:
            self.find_clickable_element(locator)
            return True
        except TimeoutException:
            return False
        
    def is_element_visible(self, locator):
        try:
            self.find_visible_element(locator)
            return True
        except TimeoutException:
            return False
        
    def take_screenshot(self, name):
        screenshots_dir = "Screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        timestamp_str = int(time.time())
        file_name = f"{screenshots_dir}/{name}_{timestamp_str}.png"

        self.driver.save_screenshot(file_name)

        allure.attach.file(
            file_name,
            name=name,
            attachment_type = allure.attachment_type.PNG
        )

    def enter_date(self, locator, date):
        element = self.find_element(locator)
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        date_parts = date.split("-")  
        formatted = date_parts[1] + date_parts[2] + date_parts[0]  
        element.send_keys(formatted)
        element.send_keys(Keys.TAB)

    def select_custom_dropdown(self, name, text):
        select_locator = (By.NAME, name)
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_element(By.NAME, name).find_elements(By.TAG_NAME, "option")) > 1
        )
        
        select_el = self.find_element(select_locator)
        value = self.driver.execute_script("""
            var select = arguments[0];
            var text = arguments[1];
            for (var i = 0; i < select.options.length; i++) {
                if (select.options[i].text.trim() === text.trim()) {
                    return select.options[i].value;
                }
            }
            return null;
        """, select_el, text)

        if value is None:
            # Print available options to help debug mismatches
            options = self.driver.execute_script("""
                return Array.from(arguments[0].options).map(o => o.text.trim());
            """, select_el)
            raise ValueError(f"Option '{text}' not found in '{name}'. Available: {options}")

        self.driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('change', {bubbles: true}));
            arguments[0].dispatchEvent(new Event('input', {bubbles: true}));
        """, select_el, value)


    def get_name_by_index(self, name, index=0):
        self.wait.until(
            lambda d: len(d.find_element(By.NAME, name).find_elements(By.TAG_NAME, "option")) > 1
        )
        select_element = self.find_element((By.NAME, name))
        return self.driver.execute_script("""
            var options = Array.from(arguments[0].options).filter(o => o.value !== '');
            if (options.length === 0) return null;
            return options[arguments[1]].text.trim();
        """, select_element, index)
    
    def enter_otp(self, locator, otp):
        otp_inputs = self.driver.find_elements(*locator)
        for i, digit in enumerate(str(otp)):
            otp_inputs[i].click()
            otp_inputs[i].send_keys(digit)