#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page
from navigation_region import NavigationRegion
from personal_tools_region import PersonalToolsRegion
from header_region import HeaderRegion
from footer_region import FooterRegion
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(Page):

    _page_title_locator = (By.ID, 'page-title')

    @property
    def navigation_region(self):
        return NavigationRegion(self.testsetup)

    @property
    def personal_tools_region(self):
        return PersonalToolsRegion(self.testsetup)

    @property
    def header_region(self):
        return HeaderRegion(self.testsetup)

    @property
    def footer_region(self):
        return FooterRegion(self.testsetup)

    @property
    def page_title(self):
        return self.selenium.find_element(*self._page_title_locator).text

    def wait_for_page_to_load(self):
        WebDriverWait(self.selenium, self.timeout).until(lambda s: self.is_element_visible(self._page_title_locator))
