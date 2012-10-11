#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class NavigationRegion(Page):

    _main_page_link_locator = (By.CSS_SELECTOR, '#n-mainpage-description a')
    _comm_portal_link_locator = (By.CSS_SELECTOR, '#n-portal a')
    _moz_news_link_locator = (By.CSS_SELECTOR, '#n-currentevents a')
    _recent_changes_link_locator = (By.CSS_SELECTOR, '#n-recentchanges a')
    _random_page_link_locator = (By.CSS_SELECTOR, '#n-randompage a')
    _help_link_locator = (By.CSS_SELECTOR, '#n-help a')

    @property
    def is_random_page_link_visible(self):
        return self.is_element_visible(self._random_page_link_locator)

    def click_random_page_link(self):
        self.selenium.find_element(*self._random_page_link_locator).click()
