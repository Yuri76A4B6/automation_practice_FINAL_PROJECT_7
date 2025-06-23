from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Finish_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS


    # Getters


    # ACTIONS


    # METHODS

    def finish(self):
        Logger.add_start_step(method="finish")
        self.get_current_url()
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method="finish")