#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class PersonalToolsRegion(Page):

    _log_in_or_create_account_link_locator = (By.CSS_SELECTOR, '#pt-login a')
    _log_out_link_locator = (By.CSS_SELECTOR, '#pt-logout a')
    _user_page_link_locator = (By.CSS_SELECTOR, '#pt-userpage a')
    _my_talk_page_link_locator = (By.CSS_SELECTOR, '#pt-mytalk a')
    _my_prefs_page_link_locator = (By.CSS_SELECTOR, '#pt-preferences a')
    _my_watchlist_page_link_locator = (By.CSS_SELECTOR, '#pt-0 a')
    _semantic_wl_page_link_locator = (By.CSS_SELECTOR, '#pt-1 a')
    _my_contribs_page_link_locator = (By.CSS_SELECTOR, '#pt-mycontris a')

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

    @property
    def is_user_page_visible(self):
        return self.is_element_visible(self._user_page_link_locator)

    def click_user_page(self):
        self.selenium.find_element(*self._user_page_link_locator).click()

    @property
    def is_my_talk_visible(self):
        return self.is_element_visible(self._my_talk_page_link_locator)

    def click_my_talk(self):
        self.selenium.find_element(*self._my_talk_page_link_locator).click()

    @property
    def is_my_prefs_visible(self):
        return self.is_element_visible(self._my_prefs_page_link_locator)

    def click_my_prefs(self):
        self.selenium.find_element(*self._my_prefs_page_link_locator).click()

    @property
    def is_my_watchlist_visible(self):
        return self.is_element_visible(self._my_watchlist_page_link_locator)

    def click_my_watchlist(self):
        self.selenium.find_element(*self._my_watchlist_page_link_locator).click()

    @property
    def is_semantic_wl_visible(self):
        return self.is_element_visible(self._semantic_wl_page_link_locator)

    def click_semantic_wl(self):
        self.selenium.find_element(*self._semantic_wl_page_link_locator).click()

    @property
    def is_my_contribs_visible(self):
        return self.is_element_visible(self._my_contribs_page_link_locator)

    def click_my_contribs(self):
        self.selenium.find_element(*self._my_contribs_page_link_locator).click()
