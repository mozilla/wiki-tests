#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class ViewHistoryPage(BasePage):

    _page_title = 'Revision history of "Main Page" - MozillaWiki'

    _history_list_locator = (By.ID, 'pagehistory')

    @property
    def history_list(self):
        return self.selenium.find_element(*self._history_list_locator).text
