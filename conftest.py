import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

@pytest.fixture(scope="function")
def driver():
        desired_caps = {
            "deviceName": "Pixel 2 API 26",
            "platformName": "Android",
            "version": "8.0",
            "app": "/Users/vitaliisotnichenko/Testing/Python_Automation/Python_Mentor/Github/python_appium/python_appium/app/splendo.apk",
            "realDevice": False,
            "newCommandTimeout": '0'
        }
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        yield driver
        driver.quit()