from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Splendo:

    def test_simple_test(self):

        desired_caps = {
            "deviceName": "Nexus_5_android_8",
            "platformName": "Android",
            "version": "8.0",
            "app": "/Users/apiliuk/Downloads/vitaliy/python_appium/app/splendo.apk",
            "realDevice": False
        }

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        inputA = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "inputA"))
        )
        inputA.send_keys("10")

        driver.quit()
