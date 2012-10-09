#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.footer_region import FooterRegion


class TestFooterPresent:

    @pytest.mark.nondestructive
    def test_footer_items_present_for_guest(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.navigation_region.click_randon_page_link()

        random_pg = home_pg.footer_region

        Assert.true(random_pg.is_footer_area_visible, "Footer Region is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_footer_logo_visible, "Footer Region Logo is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_last_modified_label_visible, "Footer Region Last Modified label is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_view_count_label_visible, "Footer Region Page View Count label is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_about_wiki_link_visible, "Footer Region About MozillaWiki link is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_disclaimer_link_visible, "Footer Region Disclaimer link is missing for " + random_pg.get_random_page_title)
        Assert.true(random_pg.is_privacy_policy_link_visible, "Footer Region Privacy Policy link is missing for " + random_pg.get_random_page_title)
