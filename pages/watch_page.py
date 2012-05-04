#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class WatchPage(BasePage):

    _page_title = 'Added to watchlist - MozillaWiki'

    _return_to_page_locator = (By.CSS_SELECTOR, '#mw-returnto a')

    @property
    def return_to_page_visible(self):
        return self.is_element_visible(self._return_to_page_locator)

    def click_return_to_page(self):
        self.selenium.find_element(*self._return_to_page_locator).click()
