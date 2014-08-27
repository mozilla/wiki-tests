#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.toolbox_region import ToolBoxRegion
from pages.upload_file_page import UploadFilePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage


class TestUploadPage:

    @pytest.mark.nondestructive
    @pytest.mark.xfail(reason='Bug 1058736 - Toolbox in left sidebar is closed by default on dev, open on staging/prod.')
    def test_verify_file_upload_page(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        log_in_or_create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        log_in_or_create_account_pg.log_in()
        Assert.true(home_pg.personal_tools_region.is_log_out_visible)

        getToUploadFile_pg = ToolBoxRegion(mozwebqa)
        getToUploadFile_pg.click_upload_file_link()

        uploadFile_pg = UploadFilePage(mozwebqa)
        Assert.true(uploadFile_pg.is_the_current_page)
        Assert.true(uploadFile_pg.is_upload_form_present)
        Assert.true(uploadFile_pg.is_upload_description_text_present)
        Assert.true(uploadFile_pg.is_source_file_area_present)
        Assert.true(uploadFile_pg.is_file_description_area_present)
        Assert.true(uploadFile_pg.is_file_upload_options_area_present)
        Assert.true(uploadFile_pg.is_upload_file_button_present)
