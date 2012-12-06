#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.user_contributions import ViewUserContributionsPage
from pages.log_in_or_create_account import LogInOrCreateAccountPage


class TestWatchPage:

    @pytest.mark.nondestructive
    def test_user_contributions_page(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()
        Assert.true(home_pg.personal_tools_region.is_log_out_visible)

        home_pg.personal_tools_region.click_my_contribs()
        user_contrib_pg = ViewUserContributionsPage(mozwebqa)

        Assert.true(user_contrib_pg.is_page_title_visible, "Page Title is missing from the page.")
        Assert.equal(user_contrib_pg.page_title_text, "User contributions", "Page Title is incorrect.")
        Assert.true(user_contrib_pg.is_breadcrumbs_visible, "Breadcrumbs are missing from the page.")
        Assert.true(user_contrib_pg.is_contrib_form_visible, "Search for contributions form is missing from the page.")
        Assert.true(user_contrib_pg.is_contrib_newbie_option_visible, "Options to only show contributions from new accounts is not present.")
        Assert.true(user_contrib_pg.is_contrib_user_option_visible, "Options to show contributions from any user or IP is not present.")

    @pytest.mark.nondestructive
    def test_search_user_contributions_results_returned(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()
        Assert.true(home_pg.personal_tools_region.is_log_out_visible)

        home_pg.personal_tools_region.click_my_contribs()
        user_contrib_pg = ViewUserContributionsPage(mozwebqa)

        user_contrib_pg.type_ip_or_username()
        user_contrib_pg.click_search_button()

        Assert.true(user_contrib_pg.is_contrib_results_present, "User contribution results are not present.")
