from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import os
import sys

from setuptools import setup
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(file_path)

from seleniumTests.POM.mainFrame import MainFrame
from seleniumTests.POM.topFrame import TopFrame
from seleniumTests.POM.adminPage import AdminPage

class LoginTest(unittest.TestCase):

    URL = "http://localhost:4000/home"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)
        admin_page = AdminPage(self.driver)
        admin_page.login_with("chemo_user_0001@chemotion.edu", "chemo_user_0001@chemotion.edu")
        time.sleep(1)

    def test_0000_import_click(self):
        home_page = MainFrame(self.driver)
        home_page.click_import()
        time.sleep(3)
        title = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/h4')
        self.assertIn('Import Collections from ZIP archive', title.text)
        home_page.click_import_close()

    def test_0001_import_file_select_click(self):
        home_page = MainFrame(self.driver)
        home_page.click_import()
        home_page.enter_path_import_file_select(file_path + "/seleniumTests/Tests/testFiles/demo.zip")
        home_page.click_import_import()
        time.sleep(5)

    def test_0002_export_click(self):
        home_page = MainFrame(self.driver)
        time.sleep(5)
        home_page.click_export()
        title = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[1]/h4')
        self.assertIn('Export Collections as ZIP archive', title.text)
        home_page.click_export_close()
        time.sleep(5)

    def test_0003_export_collection_select_click(self):
        home_page = MainFrame(self.driver)
        self.driver.find_element_by_xpath('//*[@id="export-dropdown"]/span[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/nav/div/ul/div[3]/div[1]/div[1]/ul/li[6]/a').click()
        try:
            home_page.click_export_checkbox()
        except NoSuchElementException:
            home_page.click_export_close()
            time.sleep(20)
            self.driver.refresh()
            home_page.click_export()
            try:
                home_page.click_export_checkbox()
            except NoSuchElementException:
                home_page.click_export_close()
                time.sleep(10)
                self.driver.refresh()
                home_page.click_export()
                home_page.click_export_checkbox()
        home_page.click_export_export()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    LoginTest.URL = os.environ.get('URL', LoginTest.URL)
    unittest.main()