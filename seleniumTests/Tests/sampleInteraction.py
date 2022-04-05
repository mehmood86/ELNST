from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
import os
import sys
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
        home_page = MainFrame(self.driver)
        try:
            home_page.click_my_data_button('tree-id-My Data') # must be changed with existing sample data ID
            home_page.click_sample_link()
        except:
            home_page.click_my_data_button('tree-id-qqqq')
            home_page.click_sample_link()

    def test_0000_analyses_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_analyses_tab()

    def test_0001_open_spectra_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_analyses_tab()

        spectra = self.driver.find_element_by_xpath('//*[@id="editable-analysis-list-heading-1980"]/div/div[2]/div[1]/button[2]')
        if spectra.is_enabled():
            home_page.click_spectra_editor_button()
            time.sleep(1)
            home_page.click_spectra_close_button()
            time.sleep(1)

    def test_open_spectra_tab_in_sample_activated(self):
        # login as admin and then activate chemspectra for a user and then test it
        pass

    def test_0002_qc_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_qc_tab()

    '''
    #deprecated
    def test_0003_literature_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        try:
            home_page.click_literature_tab()
        except NoSuchElementException:
            home_page.click_references_tab()
    '''

    def test_0004_results_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_results_tab()

    def test_0005_properties_tab_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_properties_tab()

    def test_0006_edit_molecule_in_sample(self):
        home_page = MainFrame(self.driver)
        home_page.click_sample_edit_molecule_button()
        time.sleep(1)
        home_page.click_sample_edit_molecule_close_button()
        time.sleep(1)

    def test_0007_enter_name_in_sample(self):
        home_page = MainFrame(self.driver)
        time_string = time.strftime("%Y%m%d-%H%M%S")
        home_page.enter_sample_name("TestSampleName" + time_string)
        home_page.save_sample()
        time.sleep(2)
        assert time_string in home_page.get_sample_name_from_label()

    def test_0008_enter_temperatures_in_sample(self):
        home_page = MainFrame(self.driver)
        boiling_temperature = time.strftime("%M%S")
        melting_temperature = time.strftime("%S%M")
        home_page.enter_boiling_temperature(boiling_temperature)
        home_page.enter_melting_temperature(melting_temperature)
        home_page.save_sample()
        time.sleep(2)
        home_page.click_sample_link()
        assert boiling_temperature in home_page.get_boiling_temperature()
        assert melting_temperature in home_page.get_melting_temperature()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    LoginTest.URL = os.environ.get('URL', LoginTest.URL)
    unittest.main()