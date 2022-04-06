from selenium.webdriver.common.by import By
from seleniumTests.POM.locators import AdminPageLocators as APL
from definitions import USER_FILE_PATH

class AdminPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_user_data(self, email, password, firstname, lastname, abbreviation):
        self.driver.find_element(By.ID, APL.email_textbox_id).send_keys(email)
        self.driver.find_element(By.ID, APL.password_textbox_id).send_keys(password)
        self.driver.find_element(By.ID, APL.passwordconfirmation_textbox_id).send_keys(password)
        self.driver.find_element(By.ID, APL.firstname_textbox_id).send_keys(firstname)
        self.driver.find_element(By.ID, APL.lastname_textbox_id).send_keys(lastname)
        self.driver.find_element(By.ID, APL.abbreviation_textbox_id).send_keys(abbreviation)

    def login_with(self, email, password):
        self.driver.find_element(By.XPATH, APL.login_field).send_keys(email)
        self.driver.find_element(By.XPATH, APL.password_field).send_keys(password)
        self.driver.find_element(By.XPATH, APL.login_btn).click()

    def logout_then_login(self, email, password):
        self.driver.find_element(By.XPATH, APL.login_field).send_keys(email)
        self.driver.find_element(By.XPATH, APL.password_field).send_keys(password)
        self.driver.find_element(By.XPATH, APL.logout_then_login).click()

    def click_user_management_link(self):
        self.driver.find_element(By.LINK_TEXT, APL.usermanagement_link_text).click()

    def click_add_user_button(self):
        self.driver.find_element(By.CLASS_NAME, APL.add_user_button_classname).click()

    def click_create(self):
        self.driver.find_element(By.XPATH, APL.create_button_xpath).click()

    def click_create_old(self):
        self.driver.find_element(By.XPATH, APL.create_button_old_xpath).click()

    def click_close(self):
        self.driver.find_element(By.CLASS_NAME, APL.close_button_classname).click()

    def click_add_multiple_user_tab(self):
        self.driver.find_element(By.XPATH, APL.multiple_users_tab).click()

    def get_locked_status(self):
        return self.driver.find_element(By.XPATH, APL.locked_status).get_attribute("class")

    def click_lock(self):
        self.driver.find_element(By.XPATH, APL.firt_user_lock).click()

    def get_error_msg(self):
        return self.driver.find_element(By.XPATH, APL.error_box).get_attribute("textContent")

    def upload_users_file(self):
        user_file_input = self.driver.find_element(By.XPATH, APL.user_file_input)
        user_file_input.send_keys(USER_FILE_PATH) # read file from testFiles directory