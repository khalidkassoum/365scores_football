from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url_driver(self):
        return self.driver.current_url

