#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage
from page import Page


class SearchResultsPage(BasePage):

    _page_title = 'Search - MozillaWiki'

    _search_results_area_locator = (By.CSS_SELECTOR, '.searchresults')

    @property
    def is_search_results_area_present(self):
        return self.is_element_present(*self._search_results_area_locator)
