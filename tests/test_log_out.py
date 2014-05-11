#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage
from pages.log_out import LogOutPage


class TestLogOut:

    @pytest.mark.nondestructive
    def test_valid_user_can_log_out(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()

        log_out_pg = LogOutPage(mozwebqa)
        home_pg.personal_tools_region.click_log_out()
        Assert.true(log_out_pg.is_the_current_page)
        Assert.true(log_out_pg.personal_tools_region.is_log_in_or_create_account_visible)
        Assert.false(log_out_pg.personal_tools_region.is_log_out_visible)
