
from dataclasses import dataclass
import time
from selenium.webdriver.common.by import By
from Python_BDD_Framwork.utils.web.userAction import UserAction
from Python_BDD_Framwork.utils.file.CSV_Handler import CSV_Handler


@dataclass
class Homepage:
    addCartBtn = (By.CLASS_NAME,"button#add-to-cart")
    backToHomeBtn = (By.CSS_SELECTOR,'button#back-to-products')
    allItems = (By.CSS_SELECTOR,"div.inventory_item_name")
    cartIcon = (By.CSS_SELECTOR,"span.shopping_cart_badge")

class PerformAddToCart(UserAction):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.dataObj = CSV_Handler("Python_BDD_Framwork\\TestData\\testData_Ecom.csv")
        self.testdata = self.dataObj.read_csv_dict()

    def searchItem(self):
        time.sleep(3)
        allElms = self.getAllElements(Homepage.allItems)
        for elm in allElms:
            if elm.text.strip() == self.testdata[0]["ItemDetails"]:
                elm.click()
                break

    def perfromAddToCart(self):
        time.sleep(2)
        #self.click(Homepage.addCartBtn)
        totalItem = self.getText(Homepage.cartIcon)
        assert int(totalItem) == 1, "system is not able to add items into cart"

    def backToHome(self):

        self.click(Homepage.backToHomeBtn)


