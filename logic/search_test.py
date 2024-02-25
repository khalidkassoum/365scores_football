from selenium.webdriver.common.by import By
from infra.base_page import BasePage


class do_search(BasePage):

    search_input = "main - header - module - mobile - input"

    def __init__(self, driver):
        super().__init__(driver)
        self.init_page()

    def init_page(self):

        self.search_INPUT = self.driver.find_element(By.CLASS_NAME, "main-header-module-mobile-input")


    def fill_txt_in_search(self):
        self.search_INPUT.send_keys("barcelona")

    def enter_search(self):
        self.search_INPUT.submit()

    def search_flow(self):
        self.fill_txt_in_search()
        self.enter_search()

    # def fill_password_input(self, password):
    #     self.user_input.sendKey(password)
    #
    # def click_on_submit_button(self):
    #     self.submit_button.click()
    #
    # def profile_name_is_visibale(self,name):
    #     self.profile_name = self.driver.find_element(By.XPATH, f"//div[text()='{name}")
    #     return self.profile_name.isDisplayd()
    #
    # def login_flow(self,username,password):
    #     self.fill_username_input(username)
    #     self.fill_password_input(password)
    #     self.click_on_submit_button()