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

class LoginTest(unittest.TestCase):
    
    URL = "http://localhost:4000/home"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        #cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(cls.URL)
        cls.driver.implicitly_wait(10)
        top_frame = TopFrame(cls.driver)
        top_frame.enter_username("test.user@provider.edu")
        top_frame.enter_password("asdasdasd")
        top_frame.click_login()

    @classmethod
    def setUp(cls):
        home_page = MainFrame(cls.driver)
        home_page.click_my_data_button()
        home_page.click_sample_link()
    
    def test_0001_Stereo_Abs_values_reflection(self):
        home_page = MainFrame(self.driver)
        home_page.click_properties_tab()

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
    
    def test_0002_Stereo_rel_values_reflection(self):
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
        
    def test_003_Change_Density(self):
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
        home_page.sample_analysis_dataset_upload()

    @classmethod
    def tearDown(cls):
        time.sleep(5)
        home_page = MainFrame(cls.driver)
        home_page.click_sample_close_button()

    @classmethod
    def tearDownClass(cls):
        top_frame = TopFrame(cls.driver)
        top_frame.click_logout()
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    LoginTest.URL = os.environ.get('URL', LoginTest.URL)
    unittest.main()