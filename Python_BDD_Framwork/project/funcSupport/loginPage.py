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
    pageName = (By.XPATH,"//div[contains(text(),'Swag Labs')]")


class PerformLogin(UserAction):

    def __init__(self, driver):
        super().__init__(driver)
        self.tomlData = TOML_Handler('Python_BDD_Framwork\\config\\config.toml')
        self.crentials = self.tomlData.load()
       

    def loginToSauceDemo(self):
        self.get(self.crentials['test']['demoUrl'])
        self.sendKeys(LoginPageElm.userName,self.crentials['test']['userName'])
        self.sendKeys(LoginPageElm.PassWord,self.crentials['test']['passWord'])
        self.click(LoginPageElm.loginBtn)
        txtTitle = self.getTitle()
        assert txtTitle == "Swag Labs", "Website is not correct"
        print("Swag Labs Home page is available")
