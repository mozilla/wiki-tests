#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert

from pages.home import HomePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage
import time


class TestEditWiki:

    def test_user_can_edit_page(self, mozwebqa):
        _edit_text_entered = 'MozWebQA Edit page wiki-test - ' + str(time.time())

        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()
        Assert.true(home_pg.is_the_current_page)

        Assert.true(home_pg.personal_tools_region.is_user_page_visible)
        home_pg.personal_tools_region.click_user_page()

        if home_pg.header_region.is_edit_visible:
            edit_pg = home_pg.header_region.click_edit()

            Assert.true(edit_pg.is_edit_page_textarea_present)
            edit_pg.enter_edit_textarea_text(_edit_text_entered)

            Assert.true(edit_pg.is_edit_page_save_button_present)
            edit_pg.click_save_button()

            Assert.true(edit_pg.is_user_entered_text_saved_and_present)
            Assert.equal(edit_pg.get_user_entered_text, _edit_text_entered)
        else:
            Assert.fail("Error - you don't have privileges to edit this page.")
