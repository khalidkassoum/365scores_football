import json
import time
import os
from selenium import webdriver
import concurrent.futures
from logic.logic_page import LogicPage


class BrowserWrapper:

    def get_caps(self):
        chrome_cap = webdriver.ChromeOptions()
        chrome_cap.capabilities['platformName'] = 'windows'
        fireFox_cap = webdriver.FirefoxOptions()
        fireFox_cap.capabilities['platformName'] = 'windows'
        edge_cap = webdriver.EdgeOptions()
        edge_cap.capabilities['platformName'] = 'windows'
        self.cap_list = [chrome_cap, fireFox_cap, edge_cap]
        return self.cap_list
    def get_driver(self, option):

        hub_url="http://localhost:4444/wd/hub"
        url="https://www.365scores.com/he"
        # Grid=False
        # if Grid:
        #   driver = webdriver.Remote(command_executor=hub_url, options=option)
        #   driver.get(url)
        #   return driver
        #
        # else:
        #     driver=webdriver.Chrome()
        #     driver.get(url)
        #     return driver
        driver = webdriver.Remote(command_executor=hub_url, options=option)
        driver.get(url)
        return driver


