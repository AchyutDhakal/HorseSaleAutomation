from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL = (By.XPATH,"//input[@placeholder='you@example.com']")
    PASSWORD = (By.XPATH,"//input[@type='password']")
    SIGNIN = (By.XPATH,"//button[@type='submit']")
    LOGOUT_BUTTON = (By.XPATH,"//span[normalize-space()='Logout']")

    def __init__(self,driver):
        super().__init__(driver)

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_signin(self):
        self.click_element(self.SIGNIN)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin()

