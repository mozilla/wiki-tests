#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from page import Page


class HeaderRegion(Page):

    _page_locator = (By.CSS_SELECTOR, '#ca-nstab-main a')
    _discussion_locator = (By.CSS_SELECTOR, '#ca-talk a')
    _view_source_locator = (By.CSS_SELECTOR, '#ca-viewsource a')
    _edit_locator = (By.CSS_SELECTOR, '#ca-edit a')
    _history_locator = (By.CSS_SELECTOR, '#ca-history a')
    _watch_locator = (By.CSS_SELECTOR, '#ca-watch a')
    _unwatch_locator = (By.CSS_SELECTOR, '#ca-unwatch a')
    _refresh_locator = (By.CSS_SELECTOR, '#ca-watch a')
    _search_field_locator = (By.CSS_SELECTOR, '#quick-search div input#q')
    _search_button_locator = (By.ID, 'quick-search-btn')

    @property
    def is_main_page_visible(self):
        return self.is_element_visible(self._page_locator)

    def click_main_page(self):
        self.selenium.find_element(*self._page_locator).click()

    @property
    def is_view_source_visible(self):
        return self.is_element_visible(self._view_source_locator)

    def click_view_source(self):
        self.selenium.find_element(*self._view_source_locator).click()
        from view_source import ViewSourcePage
        return ViewSourcePage(self.testsetup)

    @property
    def is_history_visible(self):
        return self.is_element_visible(self._history_locator)

    def click_history(self):
        self.selenium.find_element(*self._history_locator).click()
        from view_history import ViewHistoryPage
        return ViewHistoryPage(self.testsetup)

    @property
    def is_edit_visible(self):
        return self.is_element_visible(self._edit_locator)

    def click_edit(self):
        self.selenium.find_element(*self._edit_locator).click()
        from edit_wiki import EditWiki
        return EditWiki(self.testsetup)

    @property
    def is_watch_visible(self):
        return self.is_element_visible(self._watch_locator)

    def click_watch(self):
        self.selenium.find_element(*self._watch_locator).click()
        from watch_page import WatchPage
        return WatchPage(self.testsetup)

    @property
    def is_unwatch_visible(self):
        return self.is_element_visible(self._unwatch_locator)

    def click_unwatch(self):
        self.selenium.find_element(*self._unwatch_locator).click()
        from watch_page import WatchPage
        return WatchPage(self.testsetup)

    @property
    def is_refresh_visible(self):
        return self.is_element_visible(self._refresh_locator)

    def click_refresh(self):
        self.selenium.find_element(*self._refresh_locator).click()

    @property
    def is_search_visible(self):
        return self.is_element_visible(self._search_field_locator)

    def enter_text_into_search_field(self):
        from search_results import SearchResultsPage
        self.selenium.find_element(*self._search_field_locator).send_keys(SearchResultsPage._search_term)
        return SearchResultsPage(self.testsetup)

    def click_search_button(self):
        self.selenium.find_element(*self._search_button_locator).click()
        from search_results import SearchResultsPage
        return SearchResultsPage(self.testsetup)
