#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home_page import HomePage
import pages.log_in_or_create_account_page


class TestLogIn:

    @pytest.mark.nondestructive
    def test_valid_user_can_log_in(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()
		
        log_in_or_create_account_pg = pages.log_in_or_create_account_page.LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()
        Assert.true(home_pg.is_the_current_page)
        Assert.false(home_pg.personal_tools_region.is_log_in_or_create_account_visible)
        Assert.true(home_pg.personal_tools_region.is_log_out_visible)
