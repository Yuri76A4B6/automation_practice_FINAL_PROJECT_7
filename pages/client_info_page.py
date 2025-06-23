from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilites.logger import Logger


class Client_info_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #LOCATORS
    info_user_name = "//input[@id='first-name']"
    info_last_name = "//input[@id='last-name']"
    info_zip = "//input[@id='postal-code']"
    info_continue_button = "//input[@id='continue']"
    # Getters

    def get_info_user_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.info_user_name)))

    def get_info_last_name(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.info_last_name)))

    def get_info_zip(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.info_zip)))

    def get_info_continue_button(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.info_continue_button)))
    # ACTIONS

    def input_info_user_name(self, first_name):
        self.get_info_user_name().send_keys(first_name)
        print("Введено имя пользователя")

    def input_info_last_name(self, last_name):
        self.get_info_last_name().send_keys(last_name)
        print("Введена фамилия пользователя")

    def input_info_zip(self, zip_):
        self.get_info_zip().send_keys(zip_)
        print("Введен индекс ZIP")

    def click_info_continue_button(self):
        self.get_info_continue_button().click()
        print("Нажата кнопка Continue")

    # METHODS

    def input_information(self):
        Logger.add_start_step(method="input_information")
        self.get_current_url()
        self.input_info_user_name("Rulon")
        self.input_info_last_name("Oboev")
        self.input_info_zip("123456")
        self.click_info_continue_button()
        Logger.add_end_step(url=self.driver.current_url, method="input_information")