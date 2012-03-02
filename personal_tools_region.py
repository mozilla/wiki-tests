#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class PersonalToolsRegion(Page):

    _log_in_or_create_account_link_locator = (By.CSS_SELECTOR, '#pt-login a')
    _log_out_link_locator = (By.CSS_SELECTOR, '#pt-logout a')

    @property
    def is_log_in_or_create_account_visible(self):
        return self.is_element_visible(self._log_in_or_create_account_link_locator)

    def click_log_in_or_create_account(self):
        self.selenium.find_element(*self._log_in_or_create_account_link_locator).click()

    @property
    def is_log_out_visible(self):
        return self.is_element_visible(self._log_out_link_locator)

    def click_log_out(self):
        self.selenium.find_element(*self._log_out_link_locator).click()
