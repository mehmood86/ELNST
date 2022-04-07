from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import unittest
import time
import os
import sys
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(file_path)

from seleniumTests.POM.adminPage import AdminPage
from seleniumTests.POM.topFrame import TopFrame
from seleniumTests.POM.userType import UserType

class LoginTest(unittest.TestCase):

    URL = "http://localhost:4000/home"

    admin = UserType()

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)
        admin_page = AdminPage(self.driver)
        admin_page.login_with(self.admin.email, self.admin.password)
        admin_page.click_user_management_link()
        time.sleep(1)

    def test_add_users(self):
        for i in range(1,3):
            user = UserType(
                email = "chemo_user_000"+str(i)+"@chemotion.edu",
                password = "chemo_user_000"+str(i)+"@chemotion.edu",
                firstname = "instance_user_"+str(i),
                lastname = "000"+str(i),
                abbreviation = "iu"+str(i)
            )
            admin_page = AdminPage(self.driver)
            admin_page.click_user_management_link()
            admin_page.click_add_user_button()
            admin_page.enter_user_data(user.email, user.password, user.firstname, user.lastname, user.abbreviation)
            time.sleep(2)

            #start - temp block
            try:
                # developement branch 5 (latest)pass
                create_user_btn = self.driver.find_element_by_xpath('//*[@id="createUserTabs-pane-singleUser"]/form/div[8]/div/button')
                create_user_btn.click()
            except:
                create_user_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]')
                create_user_btn.click()
            #end - temp block

            admin_page.click_close()
            time.sleep(1)
        assert "Chemotion" in self.driver.title

    def test_add_multiple_users_from_file(self):
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        admin_page.click_add_user_button()
        admin_page.click_add_multiple_user_tab()
        admin_page.upload_users_file()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="createUserTabs-pane-multiUser"]/form/div[3]/button').click()
        assert "Chemotion" in self.driver.title

    def test_locked_user_login(self):
        # locked account credentials
        locked="False"
        user_email="chemo_user_0001@chemotion.edu"
        user_password="chemo_user_0001@chemotion.edu"
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        locked = admin_page.get_locked_status()

        if locked != "fa fa-unlock":
            admin_page.click_lock()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()

        top_frame = TopFrame(self.driver)
        top_frame.click_logout()
        time.sleep(2)
        admin_page.login_with(user_email, user_password)
        error_msg = admin_page.get_error_msg()
        self.assertIn ("Your account is locked.", error_msg)
        time.sleep(2)

    def test_unlocked_user_login(self):
        # locked account credentials
        locked="False"
        user_email="chemo_user_0001@chemotion.edu"
        user_password="chemo_user_0001@chemotion.edu"
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        locked = admin_page.get_locked_status()

        if locked != "fa fa-lock":
            admin_page.click_lock()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()

        top_frame = TopFrame(self.driver)
        top_frame.click_logout()
        time.sleep(2)
        admin_page.login_with(user_email, user_password)
        self.assertIn ("Chemotion", self.driver.title)
        time.sleep(2)

    #msg='Row 1: Failed to create user; Validation failed: Email has already been taken, Name abbreviation is already in use..'

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    LoginTest.URL = os.environ.get('URL', LoginTest.URL)
    unittest.main()