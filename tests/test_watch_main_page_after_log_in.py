#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage


class TestWatchPage:

    @pytest.mark.nondestructive
    def test_visitor_can_watch_page(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()

        Assert.false(home_pg.personal_tools_region.is_log_in_or_create_account_visible)
        Assert.true(home_pg.personal_tools_region.is_log_out_visible)

        if home_pg.header_region.is_watch_visible:
                watch_pg = home_pg.header_region.click_watch()
                Assert.true(watch_pg.is_the_current_page)
                Assert.equal(watch_pg.page_title, "Added to watchlist")
                watch_pg.click_return_to_page()
                Assert.true(home_pg.header_region.is_unwatch_visible)
                unwatch_pg = home_pg.header_region.click_unwatch()
                Assert.equal(watch_pg.page_title, "Removed from watchlist")
                unwatch_pg.click_return_to_page()
                Assert.true(home_pg.header_region.is_watch_visible)
        else:
                unwatch_pg = home_pg.header_region.click_unwatch()
                Assert.equal(watch_pg.page_title, "Removed from watchlist")
                unwatch_pg.click_return_to_page()
                Assert.true(home_pg.header_region.is_watch_visible)
                watch_pg = home_pg.header_region.click_watch()
                Assert.true(watch_pg.is_the_current_page)
                Assert.equal(watch_pg.page_title, "Added to watchlist")
                watch_pg.click_return_to_page()
                Assert.true(home_pg.header_region.is_unwatch_visible)
