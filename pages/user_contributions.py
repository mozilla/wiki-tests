#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class ViewUserContributionsPage(BasePage):

    _history_list_locator = (By.ID, 'pagehistory')
    _page_title_locator = (By.ID, 'page-title')
    _breadcrumbs_locator = (By.ID, 'breadcrumbs')
    _contrib_form_locator = (By.CSS_SELECTOR, '.mw-contributions-form')
    _contrib_newbie_option_locator = (By.ID, 'newbie')
    _contrib_user_option_locator = (By.ID, 'user')
    _contrib_ip_username_input_locator = (By.CSS_SELECTOR, '.mw-contributions-form fieldset input[name=target]')
    _contrib_search_button_locator = (By.CSS_SELECTOR, 'input[type=submit][value=Search]')
    _contrib_search_results_locator = (By.CSS_SELECTOR, '#main-content ul li a[title]')

    @property
    def is_page_title_visible(self):
        return self.is_element_visible(self._page_title_locator)

    @property
    def page_title_text(self):
        return self.selenium.find_element(*self._page_title_locator).text

    @property
    def is_breadcrumbs_visible(self):
        return self.is_element_visible(self._breadcrumbs_locator)

    @property
    def is_contrib_form_visible(self):
        return self.is_element_visible(self._contrib_form_locator)

    @property
    def is_contrib_newbie_option_visible(self):
        return self.is_element_visible(self._contrib_newbie_option_locator)

    @property
    def is_contrib_user_option_visible(self):
        return self.is_element_visible(self._contrib_user_option_locator)

    def type_ip_or_username(self):
        ip_username_field = self.selenium.find_element(*self._contrib_ip_username_input_locator)
        ip_username_field.clear()
        ip_username_field.send_keys("gbh")

    def click_search_button(self):
        self.selenium.find_element(*self._contrib_search_button_locator).click()

    @property
    def is_contrib_results_present(self):
        return self.is_element_present(*self._contrib_search_results_locator)
