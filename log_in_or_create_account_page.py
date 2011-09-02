#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): Dave Hunt <dhunt@mozilla.com>
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****

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
