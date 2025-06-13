from turtle import setup
from dataclasses import dataclass
from selenium.webdriver.common.by import By
from Python_BDD_Framwork.utils.web.userAction import UserAction
from Python_BDD_Framwork.utils.file.TOML_Handler import TOML_Handler

@dataclass
class LoginPageElm:
    userName = (By.CSS_SELECTOR,"input#user-name.input_error.form_input")
    PassWord = (By.CSS_SELECTOR,"input#password.input_error.form_input")
    loginBtn = (By.XPATH,"//input[@id='login-button']")


class PerformLogin(UserAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.tomlData = TOML_Handler('Python_BDD_Framwork\\config\\config.toml')
        self.crentials = self.tomlData.load()
        print(self.crentials)
        
