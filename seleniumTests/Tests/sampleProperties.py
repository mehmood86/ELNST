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

    def test_Stereo_Abs_values_reflection(self):
        home_page = MainFrame(self.driver)
        home_page.click_properties_tab() #//*[@id="editable-analysis-list-body-310"]

        try:
            home_page.change_stereo_abs_value(str(2))
            home_page.save_sample_btn()
        except:
            home_page.change_stereo_abs_value(str(1))
            home_page.save_sample_btn()
        time.sleep(3)
        '''
            Stereo Abs drop down menu items
            {0:'any', 1:'rac', 2:'meso', 3:'(S)', 4:'(R)', 5:'(Sp)', 6:'(RP)', 7:'(Sa)', 8:'(Ra)' }
        '''
        for value in range(3):
            home_page.change_stereo_abs_value(str(value+1)) # ignore '0:any' case
            time.sleep(1)
            try:
                home_page.save_sample_btn()
                time.sleep(1)
            except NoSuchElementException:
                continue
        assert '(S)' in home_page.get_iupac_span()

    def test_Stereo_rel_values_reflection(self):
        home_page = MainFrame(self.driver)
        home_page.click_properties_tab()

        try:
            home_page.change_stereo_rel_value(str(2))
            home_page.save_sample_btn()
        except:
            home_page.change_stereo_rel_value(str(1))
            home_page.save_sample_btn()
        time.sleep(3)
        '''
            Stereo Abs drop down menu items
            {
                0:'any', 1:'sync', 2:'anti', 3:'p-geminal', 4:'p-ortho',
                5:'p-meta', 6:'p-para', 7:'cis', 8:'trans', 9:'fac', 10:'mer'
            }
        '''
        for value in range(3):
            home_page.change_stereo_rel_value(str(value+1)) # ignore '0:any' case
            time.sleep(1)
            try:
                home_page.save_sample_btn()
                time.sleep(1)
            except NoSuchElementException:
                continue
        assert "p-geminal" in home_page.get_iupac_span()

    def test_Change_Density(self):
        home_page = MainFrame(self.driver)
        home_page.click_properties_tab()

        try:
            home_page.change_density(4)
            time.sleep(1)
            home_page.save_sample_btn()
            assert '4.0000' == home_page.get_density()
        except:
            home_page.change_density(2)
            time.sleep(1)
            home_page.save_sample_btn()
            assert '2.0000' == home_page.get_density()

    def test_dataset_upload(self):
        home_page = MainFrame(self.driver)
        home_page.click_analyses_tab()
        time.sleep(2)
        try:
            home_page.sample_analysis_dataset_upload()
            time.sleep(4)
            home_page.sample_analysis_dataset_upload_btn()
            home_page.upload_file()
            time.sleep(1)
            home_page.close_dialog()
            time.sleep(1)
            home_page.save_sample_btn()
        except:
            self.driver.find_element_by_xpath('//*[@id="SampleDetailsXTab-pane-analyses"]/span/div/p[1]/button').click()
            home_page.sample_analysis_dataset_upload()
            time.sleep(4)
            home_page.sample_analysis_dataset_upload_btn()
            home_page.upload_file()
            time.sleep(1)
            home_page.close_dialog()
            time.sleep(1)
            home_page.save_sample_btn()

    def test_update_dataset(self):
        home_page = MainFrame(self.driver)
        home_page.click_analyses_tab()
        try:
            home_page.sample_analysis_dataset_upload()
            home_page.get_demo_data('new')
            time.sleep(1)
            home_page.update_demo_data("sample_demo", "sample_instrument", "This is a sample dataset")
            time.sleep
            home_page.close_dialog()
            time.sleep(1)
            home_page.save_sample_btn()
            assert home_page.get_element("sample_demo").text == "sample_demo"
        except:
            home_page.sample_analysis_dataset_upload()
            home_page.get_demo_data('sample_demo')
            time.sleep(1)
            home_page.update_demo_data("new", "new_instrument", "This is a new dataset")
            time.sleep
            home_page.close_dialog()
            time.sleep(1)
            home_page.save_sample_btn()
            assert home_page.get_element("new").text == "new"

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    LoginTest.URL = os.environ.get('URL', LoginTest.URL)
    unittest.main()