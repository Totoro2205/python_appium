from appium import webdriver
import pytest
from pytest import mark


@mark.usefixtures('driver')
class BasePage:

    def __init__(self, driver):
        self.driver = driver




