import concurrent
import json
import time
import unittest
from selenium import webdriver
from self import self

from logic.live_score import LiveScoreTestCase
from logic.logic_page import LogicPage
from infra.browser_wrapper import BrowserWrapper
from logic.search_test import do_search


class GridTest(unittest.TestCase):

    def setUp(self):
      self.browser=BrowserWrapper()
      self.cap_list = self.browser.get_caps()

    def test_run_grid_serial(self,test_execute):
        for cap in self.cap_list:
            driver = self.browser.get_driver(cap)
            test_execute(driver)
            print("one only")

    def test_run_grid_parallel(self, test_execute):

        with concurrent.futures.ThreadPoolExecutor(max_workers=len(self.cap_list)) as executer:
            drivers = [self.browser.get_driver(cap) for cap in self.cap_list]
            executer.map(test_execute,drivers)


    def test_run_test(self): #STARTING THE TEST FROM HERE !!!!!!!!!!!!!
         print("start test: ")
         grid =True
         if grid:
          self.test_run_grid_parallel(self.test_live_score)
         else:
            self.test_run_grid_serial(self.test_live_score)


    def test_navigation_to_football(self,driver):
        self._navigate_foot=LogicPage(driver)
        self._navigate_foot.navigate_to_football(driver)
        assert "Football" in driver.page_source

    def test_search_functionality(self,driver):
        self.serach_func=do_search(driver)
        self.serach_func.search_flow()
        assert "barcelona" in driver.current_url, "Search did not redirect to the expected URL"


    def test_home_page_load(self,driver):
        new_load=LogicPage(driver)
        new_driver=new_load.home_page_load()
        assert "https://www.365scores.com/he" in new_driver.current_url

    def test_live_score(self,driver):
        live_score_test = LiveScoreTestCase(driver)
        live_score_test.assertlive_score_test()