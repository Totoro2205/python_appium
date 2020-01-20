

from python_appium.src.pages.base_page import BasePage
from appium import webdriver

app_package_name = "com.splendapps.splendo:id/"
text_view = "//android.widget.TextView"
task_name = app_package_name + "task_name"

class NewTask(BasePage):

    def fill_task_input(self):
        __task_input = app_package_name + "edtTaskName"
        driver.find_element_by_id(__task_input).send_keys("test task")

    def add_due_date(self):
        __due_date = app_package_name + "edtDueD"
        driver.find_element_by_id(__due_date).click()

    def click_done_button(self):
        __done_button = "android:id/button1"
        driver.find_element_by_id(__done_button).click()

    def add_due_time(self):
        __due_time = app_package_name + "edtDueT"
        driver.find_element_by_id(__due_time).click()

    def click_repeat_button(self):
        __repeat_button = app_package_name + "spinnerRepeat"
        driver.find_element_by_id(__repeat_button).click()

    def click_repeat_button_once_week(self):
        __repeat_button_once_a_week = text_view + "[@text='Once a Week']"
        driver.find_element_by_xpath(__repeat_button_once_a_week).click()

    def click_add_to_list_button(self):
        __add_to_list_button = app_package_name + "spinnerLists"
        driver.find_element_by_id(__add_to_list_button).click()

    def add_to_personal_list_button(self):
        __add_to_list_button_personal = text_view + "[@text='Personal']"
        driver.find_element_by_xpath(__add_to_list_button_personal).click()

    def save_task(self):
        __save_task = app_package_name + "action_save_task"
        driver.find_element_by_accessibility_id(__save_task).click()