#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class LogInOrCreateAccountPage(BasePage):

    _page_title = 'Log in / create account - MozillaWiki'

    _username_locator = (By.ID, 'wpName1')
    _password_locator = (By.ID, 'wpPassword1')
    _confirm_password_locator = (By.ID, 'signup_password_confirm')
    _log_in_locator = (By.ID, 'wpLoginAttempt')
    _create_account_link_locator = (By.CSS_SELECTOR, '#userloginlink a')
    _create_username_locator = (By.ID, 'wpName2')
    _create_password_locator = (By.ID, 'wpPassword2')
    _create_password_retype_locator = (By.ID, 'wpRetype')
    _create_email_locator = (By.ID, 'wpEmail')
    _create_realname_locator = (By.ID, 'wpRealName')
    _create_account_button_locator = (By.ID, 'wpCreateaccount')
    _create_account_error_box_locator = (By.CLASS_NAME, 'errorbox')
    _new_user_created_message = (By.ID, 'page-title')
    _new_user_welcome_message = (By.CSS_SELECTOR, 'h2 .mw-headline')

    def log_in(self, user='default'):
        credentials = self.testsetup.credentials[user]
        self.type_username(credentials['username'])
        self.type_password(credentials['password'])
        self.click_log_in()

    def type_username(self, username):
        username_field = self.selenium.find_element(*self._username_locator)
        username_field.clear()
        username_field.send_keys(username)

    def type_password(self, password):
        password_field = self.selenium.find_element(*self._password_locator)
        password_field.clear()
        password_field.send_keys(password)

    def click_log_in(self):
        self.selenium.find_element(*self._log_in_locator).click()

    def click_create_account_link(self):
        self.selenium.find_element(*self._create_account_link_locator).click()

    def create_user(self, username, password, retype_pwd, email, realname):
        self.type_new_username(username)
        self.type_new_password(password)
        self.retype_new_password(retype_pwd)
        self.type_new_email(email)
        self.type_realname(realname)
        self.click_create_account_button()

    def type_new_username(self, username):
        new_username_field = self.selenium.find_element(*self._create_username_locator)
        new_username_field.clear()
        new_username_field.send_keys(username)

    def type_new_password(self, password):
        new_password_field = self.selenium.find_element(*self._create_password_locator)
        new_password_field.clear()
        new_password_field.send_keys(password)

    def retype_new_password(self, password):
        new_password_retype_field = self.selenium.find_element(*self._create_password_retype_locator)
        new_password_retype_field.send_keys(password)

    def type_new_email(self, email):
        new_email_field = self.selenium.find_element(*self._create_email_locator)
        new_email_field.send_keys(email)

    def type_realname(self, realname):
        realname_field = self.selenium.find_element(*self._create_realname_locator)
        realname_field.send_keys(realname)

    def click_create_account_button(self):
        self.selenium.find_element(*self._create_account_button_locator).click()

    @property
    def is_error_message_present(self):
        return self.is_element_present(*self._create_account_error_box_locator)

    @property
    def get_error_message_text(self):
        return self.selenium.find_element(*self._create_account_error_box_locator).text

    @property
    def get_user_created_message(self):
        return self.selenium.find_element(*self._new_user_created_message).text

    @property
    def get_user_welcome_message(self):
        return self.selenium.find_element(*self._new_user_welcome_message).text
