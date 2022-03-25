from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def test_add_users(self):
        self.driver.find_element_by_xpath('//*[@id="user_login"]').send_keys(self.admin.email)
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.admin.password)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/button').click()
        self.driver.find_element_by_link_text("User Management").click()
        time.sleep(1)
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

    @classmethod
    def tearDown(self):
        time.sleep(2)
        top_frame = TopFrame(self.driver)
        top_frame.click_logout()
        self.driver.quit()

if __name__ == '__main__':
    LoginTest.URL = os.environ.get('URL', LoginTest.URL)
    unittest.main()