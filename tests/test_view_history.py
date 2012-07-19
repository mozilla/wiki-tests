#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage


class TestViewHistory:

    @pytest.mark.nondestructive
    def test_visitor_can_view_history(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()

        history_pg = home_pg.header_region.click_history()
        Assert.true(history_pg.is_the_current_page)
        Assert.greater(len(history_pg.history_list.strip()), 0)

    @pytest.mark.nondestructive
    def test_logged_in_user_can_view_history(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()

        home_pg.personal_tools_region.click_log_in_or_create_account()
        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()

        history_pg = home_pg.header_region.click_history()
        Assert.true(history_pg.is_the_current_page)
        Assert.greater(len(history_pg.history_list.strip()), 0)
