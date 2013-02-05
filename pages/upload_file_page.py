#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class UploadFilePage(Page):

    _page_title = 'Upload file - MozillaWiki'

    _upload_desc_text_locator = (By.ID, 'uploadtext')
    _upload_form_locator = (By.ID, 'mw-upload-form')
    _source_file_area_locator = (By.ID, 'mw-htmlform-source')
    _file_description_area_locator = (By.ID, 'mw-htmlform-description')
    _file_upload_options_area_locator = (By.ID, 'mw-htmlform-options')
    _upload_file_button_locator = (By.CSS_SELECTOR, '.mw-htmlform-submit')

    @property
    def is_upload_description_text_present(self):
        return self.is_element_present(*self._upload_desc_text_locator)

    @property
    def is_upload_form_present(self):
        return self.is_element_present(*self._upload_form_locator)

    @property
    def is_source_file_area_present(self):
        return self.is_element_present(*self._source_file_area_locator)

    @property
    def is_file_description_area_present(self):
        return self.is_element_present(*self._file_description_area_locator)

    @property
    def is_file_upload_options_area_present(self):
        return self.is_element_present(*self._file_upload_options_area_locator)

    @property
    def is_upload_file_button_present(self):
        return self.is_element_present(*self._upload_file_button_locator)

    def click_upload_file_button(self):
        self.selenium.find_element(*self._upload_file_button_locator).click()
