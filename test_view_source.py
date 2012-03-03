#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

import home_page


class TestViewSource:

    @pytest.mark.nondestructive
    def test_visitor_can_view_source(self, mozwebqa):
        home_pg = home_page.HomePage(mozwebqa)
        home_pg.go_to_home_page()
        view_source_pg = home_pg.click_view_source()

        Assert.true(view_source_pg.is_the_current_page)
        Assert.greater(len(view_source_pg.source_textarea.strip()), 0)
