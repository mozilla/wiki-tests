#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage
from pages.edit_wiki import EditWiki


class TestEditWiki:  
 
    @pytest.mark.nondestructive
    def test_valid_user_can_log_in(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()
        Assert.true(home_pg.is_the_current_page)
        Assert.false(home_pg.personal_tools_region.is_log_in_or_create_account_visible)
        Assert.true(home_pg.personal_tools_region.is_user_page_visible)
        home_pg.personal_tools_region.click_user_page()
        
        if home_pg.header_region.is_edit_visible:
                edit_pg = home_pg.header_region.click_edit()
                Assert.true(edit_pg.is_the_current_page)
                edit_pg.edit_user_page()
                edit_pg.click_save_page()
                Assert.false(edit_pg.edit_save)
                Assert.true(edit_pg.verify_user_text)                
                Assert.equal('MozillaUser', EditWiki._text_entered)


