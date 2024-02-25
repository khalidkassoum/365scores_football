from selenium.webdriver.common.by import By
from infra.base_page import BasePage

class LiveScoreTestCase(BasePage):
    LIVE_SCORE = (By.CSS_SELECTOR, "div.switch-button-content")

    def verify_live_score_element_displayed(self):
        live_score_element = self.driver.find_element(*self.LIVE_SCORE)
        return live_score_element.is_displayed()

    def assertlive_score_test(self):
        assert self.verify_live_score_element_displayed(), "Live score section not displayed."