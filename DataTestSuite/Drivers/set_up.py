import os
import pathlib
import sys
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sys import platform


# import org.openqa.selenium.chrome.ChromeOptions;

@pytest.fixture
def fixed_driver():
    options = Options()
    # options.add_argument("--start-maximized")
    # options.headless = True
    # options.add_argument("--headless")
    # options.add_argument("--disable-logging")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--log-level=3")
    # options.add_argument('--disable-dev-shm-usage')

    # Check OS and use correct driver
    if platform == "linux" or platform == "linux2":
        options.add_argument("--headless")
        options.add_argument("--window-size=5120,1440")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        b = webdriver.Chrome("C:/Users/CoreDevOps/PycharmProjects/DataTesting/DataTestSuite/Drivers/chromedriver.exe", options=options)
    else:

        #options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=5120,1440")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-logging")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")

        b = webdriver.Chrome("C:/Users/Administrator/Documents/GitHub/DataTesting/DataTestSuite/Drivers/chromedriver.exe", options=options)
        #C:\Users\Administrator\Documents\GitHub\DataTesting\DataTestSuite\Drivers\chromedriver.exe
        b.maximize_window()

    yield b



