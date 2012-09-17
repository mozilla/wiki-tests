#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class SearchResultsPage(BasePage):

    _page_title = 'Search - MozillaWiki'
    _search_term = 'mozwebqa'

    _search_results_area_locator = (By.CSS_SELECTOR, '.searchresults')
    _search_page_header_locator = (By.ID, 'page-title')
    _search_page_breadcrumbs_locator = (By.ID, 'breadcrumbs')
    _search_page_main_search_box_locator = (By.ID, 'searchText')
    _search_page_search_types_locator = (By.CSS_SELECTOR, '.search-types')
    _search_page_matched_term_locator = (By.CSS_SELECTOR, '.searchmatch')

    @property
    def is_search_results_area_present(self):
        return self.is_element_present(*self._search_results_area_locator)

    @property
    def is_search_breadcrumbs_present(self):
        return self.is_element_present(*self._search_page_breadcrumbs_locator)

    @property
    def search_page_breadcrumbs_text(self):
        return self.selenium.find_element(*self._search_page_breadcrumbs_locator).text

    @property
    def is_search_types_present(self):
        return self.is_element_present(*self._search_page_search_types_locator)

    @property
    def search_page_title(self):
        return self.selenium.find_element(*self._search_page_header_locator).text

    @property
    def main_search_box_text(self):
        return self.selenium.find_element(*self._search_page_main_search_box_locator).get_attribute('value')

    @property
    def get_matched_search_term_in_results(self):
        return self.selenium.find_elements(*self._search_page_matched_term_locator)
