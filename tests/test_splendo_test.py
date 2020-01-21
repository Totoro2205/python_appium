from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from python_appium.src.pages.add_first_task import AddFirstTask
from python_appium.src.pages.new_task import NewTask, task_name


class Test_Splendo:

    def test_simple_test(self, driver):
        a = 0
        driver.drag_and_drop(driver.find_element_by_xpath("//*[contains(@text,'Sort order')]"),
                             driver.find_element_by_xpath("//*[contains(@text,'Remove Ads')]"))
        self.add_first_task_page = AddFirstTask(driver)
        self.add_first_task_page.click_at_add_first_task_button()
        self.add_new_task = NewTask(driver)
        self.add_new_task.fill_task_input()
        self.add_new_task.add_due_date()
        self.add_new_task.click_done_button()
        self.add_new_task.add_due_time()
        self.add_new_task.click_done_button()
        self.add_new_task.click_repeat_button()
        self.add_new_task.click_repeat_button_once_week()
        self.add_new_task.click_add_to_list_button()
        self.add_new_task.add_to_personal_list_button()
        self.add_new_task.save_task()
        wait = WebDriverWait(driver, 30)
        wait.until(EC.presence_of_element_located((MobileBy.ID, task_name)))
        assert driver.find_element_by_id(task_name).is_displayed()

