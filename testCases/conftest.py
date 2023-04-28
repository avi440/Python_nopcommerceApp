import os.path
import time
from datetime import datetime


import self
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import logging

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

# browser = ReadConfig.getBrowser()
# @pytest.hookimpl(hookwrapper=True)
# @pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        #all ways add the url to reports
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            # file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = str(int(round(time.time()*1000)))+".png"
            destinationFile = os.path.join(report_directory,file_name)
            # driver.save_screenshot(".\\Reports\\testcases\\"+file_name)
            # driver.save_screenshot(destinationFile)
            # driver.get_screenshot_as_file(destinationFile)
            feature_request = item.funcargs['request']
            driver = feature_request.getfixturevalue('browser')
            # driver.save_screenshot(destinationFile)
            # _capture_screenshot(destinationFile,driver)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"'\
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
            report.extra = extra


# @pytest.fixture(autouse=True)
def _capture_screenshot(name,driver):
    yield
    # _driver.get_screenshot_as_file(name)

def pytest_html_report_title(report):
    report.title = "Automation Report"



@pytest.fixture()
# @pytest.fixture(scope='session', autouse=True)
def setupdriver(request,browser):
    _driver = None
    if browser == "chrome":
    # driver = webdriver.Chrome(ChromeDriverManager().install())
        _driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # logger.info("Lunching the chrome browser")
        # return driver
    elif browser == "ie":
        _driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        # logger.info("Lunching the ie browser")
        # return driver
    else:
        _driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
       # logger.info("Lunching the firefox browser")
       #  return driver
    request.cls.driver= _driver
    yield request.cls.driver


def pytest_addoption(parser):     #it will give the value form CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):    # it will return the browser value to setup method
    return request.config.getoption("--browser")



##########pytest html reports ##############
#it is hook for Adding environment info to HTML reports
def pytest_configure(config):
    config._metadata['project Name']='nop commerce'
    config._metadata['Modul Name'] = 'Customers'
    config._metadata['Tester'] = 'Avinash'


#it is hook for deleting/mofify envionment info HTML Reports
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)




# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# def getDriver():
#     return setupdriver
# driver = getDriver()

# @pytest.mark.hookwrapper
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# @pytest.hookimpl(hookwrapper=True)




