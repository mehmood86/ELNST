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
        self.driver.find_element_by_xpath('//*[@id="user_login"]').send_keys(self.admin.email)
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.admin.password)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/button').click()
        self.driver.find_element_by_link_text("User Management").click()
        time.sleep(1)

    def test_add_users(self):
        for i in range(1,6):
            user = UserType(
                email = "chemo_user_000"+str(i)+"@chemotion.edu",
                password = "chemo_user_000$"+str(i)+"@chemotion.edu",
                firstname = "instance_user_"+str(i),
                lastname = "000"+str(i),
                abbreviation = "iu"+str(i)
            )
            admin_page = AdminPage(self.driver)
            admin_page.click_user_management_link()
            admin_page.click_add_user_button()
            admin_page.enter_user_data(user.email, user.password, user.firstname, user.lastname, user.abbreviation)
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]').click()
            admin_page.click_close()
            time.sleep(1)
        assert "Chemotion" in self.driver.title

    def test_locked_user_login(self):
        # locked account credentials
        locked="False"
        email="chemotion_user_0001@chemotion.edu"
        password="chemotion_user_0001@chemotion.edu"
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        lock_elem =self.driver.find_element_by_xpath('//*[@id="AdminHome"]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/button[4]/i')
        locked = lock_elem.get_attribute("class")

        if locked != "fa fa-unlock":
            elem=self.driver.find_element_by_xpath('//*[@id="AdminHome"]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/button[4]')
            elem.click()
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()

        top_frame = TopFrame(self.driver)
        top_frame.click_logout()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="user_login"]').send_keys(email)
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/button').click()
        error_msg= self.driver.find_element_by_xpath('/html/body/div/div/div[2]').get_attribute("textContent")
        self.assertIn ("Your account is locked.", error_msg)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    LoginTest.URL = os.environ.get('URL', LoginTest.URL)
    unittest.main()