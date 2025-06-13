from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ecWait = 30

class UserAction:

    def __init__(self, driver:WebDriver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)

    def refreshPage(self):
        self.driver.refresh()

    def sendKeys(self, byLocator, txt:str):
        elm = WebDriverWait(self.driver, ecWait).until(EC.visibility_of_element_located(byLocator)).send_keys(txt)

    def click(self, byLocator):
        elm = WebDriverWait(self.driver, ecWait).until(EC.visibility_of_element_located(byLocator))
        elm.click()

    def getTitle(self):
        return self.driver.title
    
    def getText(self, byLocator):
        elm = WebDriverWait(self.driver, ecWait).until(EC.visibility_of_element_located(byLocator))
        return elm.text