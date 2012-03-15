#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

import base


class ViewSourcePage(base.BasePage):

    _page_title = 'View source - MozillaWiki'

    _source_textarea_locator = (By.ID, 'wpTextbox1')

    @property
    def source_textarea(self):
        return self.selenium.find_element(*self._source_textarea_locator).text
