#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

import home_page
import log_in_or_create_account_page
import log_out_page


class TestLogIn:

    @pytest.mark.prod
    def test_valid_user_can_log_out(self, mozwebqa):
        home_pg = home_page.HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        log_in_or_create_account_pg = log_in_or_create_account_page.LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()

        log_out_pg = log_out_page.LogOutPage(mozwebqa)
        home_pg.personal_tools_region.click_log_out()
        Assert.true(log_out_pg.is_the_current_page)
        Assert.true(log_out_pg.personal_tools_region.is_log_in_or_create_account_visible)
        Assert.false(log_out_pg.personal_tools_region.is_log_out_visible)
