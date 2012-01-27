#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

import base_page


class LogInOrCreateAccountPage(base_page.BasePage):

    _page_title = "Log in / create account - MozillaWiki"

    _username_locator = (By.ID, "wpName1")
    _password_locator = (By.ID, "wpPassword1")
    _confirm_password_locator = (By.ID, "signup_password_confirm")
    _log_in_locator = (By.ID, "wpLoginAttempt")

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
