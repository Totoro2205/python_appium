from appium import webdriver
from python_appium.src.pages.base_page import BasePage


class AddFirstTask(BasePage):
    def click_at_add_first_task_button(self):
        __add_first_task_button = "Add First Task"
        driver.find_element_by_accessibility_id(__add_first_task_button).click()
