#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from page import Page


class FooterRegion(Page):

    _footer_area_locator = (By.ID, 'footer')
    _footer_logo_locator = (By.ID, 'logo-footer')
    _footer_last_modified_locator = (By.ID, 'f-lastmod')
    _footer_page_view_count_locator = (By.ID, 'f-viewcount')
    _footer_about_wiki_link_locator = (By.CSS_SELECTOR, '#f-list #f-about a')
    _footer_privacy_policy_link_locator = (By.CSS_SELECTOR, '#f-list li a[href*=privacy-policy]')
    _random_page_title_locator = (By.ID, 'page-title')

    @property
    def is_footer_area_visible(self):
        return self.is_element_visible(self._footer_area_locator)

    @property
    def is_footer_logo_visible(self):
        return self.is_element_visible(self._footer_logo_locator)

    @property
    def is_last_modified_label_visible(self):
        return self.is_element_visible(self._footer_last_modified_locator)

    @property
    def is_view_count_label_visible(self):
        return self.is_element_visible(self._footer_page_view_count_locator)

    @property
    def is_about_wiki_link_visible(self):
        return self.is_element_visible(self._footer_about_wiki_link_locator)

    @property
    def is_privacy_policy_link_visible(self):
        return self.is_element_visible(self._footer_privacy_policy_link_locator)

    @property
    def get_random_page_title(self):
        return self.selenium.find_element(*self._random_page_title_locator).text
