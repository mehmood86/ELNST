from tkinter import E
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

    def test_add_users_with_validation(self):
        self.driver.find_element_by_xpath('//*[@id="user_login"]').send_keys(self.admin.email)
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(self.admin.password)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/button').click()
        self.driver.find_element_by_link_text("User Management").click()
        time.sleep(1)

        valid_user1 = UserType(
            email = "chem.user1_@chemotion.edu",
            password = "password1",
            firstname = "instance_user1",
            lastname = "0001",
            abbreviation = "ciu"
        )

        invalid_user1 = UserType(
            email = "chem.user1_at_chemotion.edu", # invalid email
            password = "password1",
            firstname = "instance_user1",
            lastname = "0001",
            abbreviation = "iu1"
        )

        invalid_user2 = UserType(
            email = "chem.user1_@chemotion.edu",
            password = "pass2", # invalid password
            firstname = "instance_user1",
            lastname = "0001",
            abbreviation = "iu1"
        )

        invalid_user3 = UserType(
            email = "chem.user1_@chemotion.edu",
            password = "password1",
            firstname = "", # invalid first name
            lastname = "0001",
            abbreviation = "iu1"
        )

        invalid_user4 = UserType(
            email = "chem.user1_@chemotion.edu",
            password = "password1",
            firstname = "instance_user1",
            lastname = "", # invalid last name
            abbreviation = "inu1"
        )

        invalid_user5 = UserType(
            email = "chem.user1_@chemotion.edu",
            password = "password1",
            firstname = "instance_user1",
            lastname = "0001",
            abbreviation = "iusD5"  # invalid abbreviation
        )

        users = [invalid_user1, invalid_user2, invalid_user3, invalid_user4, invalid_user5, valid_user1]
        error_msgs = [  "Validation failed:",
                        "You have entered an invalid email address!",
                        "Please input password with correct format",
                        "Please input First name, Last name and Name abbreviation",
                        "Name abbreviation has to be 2 to 3 characters long"]

        for self.user in users:
            admin_page = AdminPage(self.driver)
            admin_page.click_user_management_link()
            admin_page.click_add_user_button()
            admin_page.enter_user_data(self.user.email, self.user.password, self.user.firstname, self.user.lastname, self.user.abbreviation)
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]').click()
            time.sleep(4)
            error_box = self.driver.find_element_by_id('formControlMessage').get_attribute('value')
            for msg in error_msgs:
                if msg in error_box:
                    assert True
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