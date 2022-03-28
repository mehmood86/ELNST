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

class UserValidation(unittest.TestCase):

    URL = "http://localhost:4000/home"

    admin = UserType()

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

    def test_user_with_invalid_email(self):
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        admin_page.click_add_user_button()
        admin_page.enter_user_data(self.invalid_user1.email,
            self.invalid_user1.password,
            self.invalid_user1.firstname,
            self.invalid_user1.lastname,
            self.invalid_user1.abbreviation)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]').click()
        time.sleep(4)
        error_box = self.driver.find_element_by_id('formControlMessage').get_attribute('value')
        self.assertIn ("You have entered an invalid email address!", error_box)

    def test_user_with_invalid_password(self):
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        admin_page.click_add_user_button()
        admin_page.enter_user_data(self.invalid_user2.email,
            self.invalid_user2.password,
            self.invalid_user2.firstname,
            self.invalid_user2.lastname,
            self.invalid_user2.abbreviation)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]').click()
        time.sleep(4)
        error_box = self.driver.find_element_by_id('formControlMessage').get_attribute('value')
        self.assertIn ("Password is too short", error_box)

    def test_user_with_invalid_firstname(self):
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        admin_page.click_add_user_button()
        admin_page.enter_user_data(self.invalid_user3.email,
            self.invalid_user3.password,
            self.invalid_user3.firstname,
            self.invalid_user3.lastname,
            self.invalid_user3.abbreviation)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]').click()
        time.sleep(4)
        error_box = self.driver.find_element_by_id('formControlMessage').get_attribute('value')
        self.assertIn ("Please input First name, Last name and Name abbreviation", error_box)

    def test_user_with_invalid_lastname(self):
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        admin_page.click_add_user_button()
        admin_page.enter_user_data(self.invalid_user4.email,
            self.invalid_user4.password,
            self.invalid_user4.firstname,
            self.invalid_user4.lastname,
            self.invalid_user4.abbreviation)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]').click()
        time.sleep(4)
        error_box = self.driver.find_element_by_id('formControlMessage').get_attribute('value')
        self.assertIn ("Please input First name, Last name and Name abbreviation", error_box)

    def test_user_with_invalid_abbreviation(self):
        admin_page = AdminPage(self.driver)
        admin_page.click_user_management_link()
        admin_page.click_add_user_button()
        admin_page.enter_user_data(self.invalid_user5.email,
            self.invalid_user5.password,
            self.invalid_user5.firstname,
            self.invalid_user5.lastname,
            self.invalid_user5.abbreviation)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[9]/div/button[1]').click()
        time.sleep(4)
        error_box = self.driver.find_element_by_id('formControlMessage').get_attribute('value')
        self.assertIn ("Name abbreviation has to be 2 to 3 characters long", error_box)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    UserValidation.URL = os.environ.get('URL', UserValidation.URL)
    unittest.main()