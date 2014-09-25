#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage


class TestHomePage:

    @pytest.mark.nondestructive
    def test_footer_items_present_for_guest(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.navigation_region.click_random_page_link()

        random_pg = home_pg.footer_region

        Assert.true(random_pg.is_footer_area_visible,
                    "Footer Region is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_footer_logo_visible,
                    "Footer Region Logo is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_last_modified_label_visible,
                    "Footer Region Last Modified label is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_view_count_label_visible,
                    "Footer Region Page View Count label is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_about_wiki_link_visible,
                    "Footer Region About MozillaWiki link is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_privacy_policy_link_visible,
                    "Footer Region Privacy Policy link is missing for " + random_pg.get_random_page_title)

    @pytest.mark.nondestructive
    def test_logged_in_user_can_view_source(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()

        home_pg.personal_tools_region.click_log_in_or_create_account()
        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()

        Assert.false(home_pg.personal_tools_region.is_log_in_or_create_account_visible)
        Assert.true(home_pg.personal_tools_region.is_log_out_visible)

        view_source_pg = home_pg.header_region.click_view_source()
        Assert.true(view_source_pg.is_the_current_page)
        Assert.greater(len(view_source_pg.source_textarea.strip()), 0)

    @pytest.mark.nondestructive
    def test_valid_user_can_log_in(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()

        home_pg.personal_tools_region.click_log_in_or_create_account()
        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()

        Assert.true(home_pg.is_the_current_page)
        Assert.false(home_pg.personal_tools_region.is_log_in_or_create_account_visible,
                    "Log in is still visible")
        Assert.true(home_pg.personal_tools_region.is_user_page_visible,
                    "User page is not visible")
        Assert.true(home_pg.personal_tools_region.is_my_talk_visible,
                    "Talk is not visible")
        Assert.true(home_pg.personal_tools_region.is_my_prefs_visible,
                    "Preferences are not visible")
        Assert.true(home_pg.personal_tools_region.is_my_watchlist_visible,
                    "Watchlist is not visible")
        Assert.true(home_pg.personal_tools_region.is_semantic_wl_visible,
                    "Semantic wl is not visible")
        Assert.true(home_pg.personal_tools_region.is_my_contribs_visible,
                    "My contributions are not visible")
        Assert.true(home_pg.personal_tools_region.is_log_out_visible,
                    "Log out is not visible")

    @pytest.mark.nondestructive
    def test_visitor_can_view_source(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()

        view_source_pg = home_pg.header_region.click_view_source()
        Assert.true(view_source_pg.is_the_current_page,
                    "View source is not visible")
        Assert.greater(len(view_source_pg.source_textarea.strip()), 0)
