from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Splendo:

    def test_simple_test(self):
        desired_caps = {
            "deviceName": "Nexus_5_android_8",
            "platformName": "Android",
            "version": "8.0",
            "app": "/Users/apiliuk/Downloads/vitaliy/python_appium/app/splendo.apk",
            "realDevice": False,
            "newCommandTimeout": '0'
        }

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # Web Elements
        app_package_name = "com.splendapps.splendo:id/"
        text_view = "//android.widget.TextView"

        add_first_task_button = "Add First Task"
        task_input = app_package_name + "edtTaskName"
        due_date = app_package_name + "edtDueD"
        due_time = app_package_name + "edtDueT"
        save_task = app_package_name + "action_save_task"
        done_button = "android:id/button1"
        repeat_button = app_package_name + "spinnerRepeat"
        repeat_button_once_a_week = text_view + "[@text='Once a Week']"
        add_to_list_button = app_package_name + "spinnerLists"
        add_to_list_button_personal = text_view + "[@text='Personal']"
        task_name = app_package_name + "task_name"

        wait = WebDriverWait(driver, 30)
        driver.find_element_by_accessibility_id(add_first_task_button).click()
        driver.find_element_by_id(task_input).send_keys("test task")
        driver.find_element_by_id(due_date).click()
        driver.find_element_by_id(done_button).click()
        driver.find_element_by_id(due_time).click()
        driver.find_element_by_id(done_button).click()
        driver.find_element_by_id(repeat_button).click()
        driver.find_element_by_xpath(repeat_button_once_a_week).click()
        driver.find_element_by_id(add_to_list_button).click()
        driver.find_element_by_xpath(add_to_list_button_personal).click()
        driver.find_element_by_id(save_task).click()

        wait.until(EC.presence_of_element_located((MobileBy.ID, task_name)))

        assert driver.find_element_by_id(task_name).is_displayed()

        driver.quit()
