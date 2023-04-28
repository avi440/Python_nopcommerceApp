# import os
# import time
#
# import pytest
# import self
#
#
# @pytest.mark.usefixtures("setupdriver")
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call':
#         # all ways add the url to reports
#         extra.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             report_directory = os.path.dirname(item.config.option.htmlpath)
#             # file_name = report.nodeid.replace("::", "_") + ".png"
#             file_name = str(int(round(time.time() * 1000))) + ".png"
#             destinationFile = os.path.join(report_directory, file_name)
#             # driver.save_screenshot(".\\Reports\\testcases\\"+file_name)
#             # driver.save_screenshot(destinationFile)
#             # driver.get_screenshot_as_file(destinationFile) -----
#             _capture_screenshot(destinationFile)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#             report.extra = extra
#
#
# def _capture_screenshot(name):
#     self.driver.get_screenshot_as_file(name)
#
#
# def pytest_html_report_title(report):
#     report.title = "Automation Report"
