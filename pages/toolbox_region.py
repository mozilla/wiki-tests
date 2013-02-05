#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class ToolBoxRegion(Page):

    _what_links_here_link_locator = (By.CSS_SELECTOR, '#t-whatlinkshere a')
    _related_changes_link_locator = (By.CSS_SELECTOR, '#t-recentchangeslinked a')
    _upload_file_link_locator = (By.CSS_SELECTOR, '#t-upload a')
    _special_pages_link_locator = (By.CSS_SELECTOR, '#t-specialpages a')
    _browse_properties_link_locator = (By.CSS_SELECTOR, '#t-smwbrowselink a')

    @property
    def is_upload_file_link_visible(self):
        return self.is_element_visible(self._upload_file_link_locator)

    def click_upload_file_link(self):
        self.selenium.find_element(*self._upload_file_link_locator).click()
