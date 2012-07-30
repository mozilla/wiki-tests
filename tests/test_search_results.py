#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.search_results import SearchResultsPage
from pages.header_region import HeaderRegion
from pages.log_in_or_create_account import LogInOrCreateAccountPage


class TestSearchPage:

    @pytest.mark.nondestructive
    def test_no_results_returned_from_blank_search(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()

        search_results_pg = home_pg.header_region.click_search_button()
        Assert.true(search_results_pg.is_the_current_page)
        Assert.false(search_results_pg.is_search_results_area_present, "Search Results area is present.")

        Assert.true(search_results_pg.is_search_breadcrumbs_present)
        Assert.equal(search_results_pg.search_page_title, "Search", "Search Results page header mismatch.")
        Assert.equal(search_results_pg.search_page_breadcrumbs_text, u'Home \xbb  Search:', "Search Results page breadcrumbs are incorrect.")
        Assert.equal(search_results_pg.main_search_box_text, "", "Main Search field should be empty.")
