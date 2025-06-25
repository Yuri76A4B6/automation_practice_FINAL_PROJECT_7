import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Payment_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS

    finish_button = "//button[@id='finish']"

    # Getters

    def get_finish_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    # ACTIONS

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Нажата кнопка для завершения оплаты")

    # METHODS

    def payment(self):
        with allure.step("Payment"):
            Logger.add_start_step(method="payment")
            self.get_current_url()
            self.click_finish_button()
            Logger.add_end_step(url=self.driver.current_url, method="payment")
