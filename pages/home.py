#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class HomePage(BasePage):

    _page_title = 'MozillaWiki'

    _view_source_locator = (By.CSS_SELECTOR, '#ca-viewsource a')

    def go_to_home_page(self):
        self.selenium.get(self.testsetup.base_url + '/')
        self.is_the_current_page

    def click_view_source(self):
        self.selenium.find_element(*self._view_source_locator).click()
        from view_source import ViewSourcePage
        return ViewSourcePage(self.testsetup)
