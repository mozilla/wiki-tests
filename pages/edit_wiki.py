#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class EditWiki(BasePage):

    _edit_textarea_locator = (By.ID, 'wpTextbox1')
    _save_button_locator = (By.ID, 'wpSave')
    _user_text_entered_locator = (By.CSS_SELECTOR, '#main-content p')

    @property
    def is_edit_page_textarea_present(self):
        return self.is_element_present(*self._edit_textarea_locator)

    def enter_edit_textarea_text(self, enter_text):
        self.selenium.find_element(*self._edit_textarea_locator).clear()
        self.selenium.find_element(*self._edit_textarea_locator).send_keys(enter_text)

    @property
    def is_edit_page_save_button_present(self):
        return self.is_element_present(*self._save_button_locator)

    def click_save_button(self):
        self.selenium.find_element(*self._save_button_locator).click()

    @property
    def is_user_entered_text_saved_and_present(self):
        return self.is_element_present(*self._user_text_entered_locator)

    @property
    def get_user_entered_text(self):
        return self.selenium.find_element(*self._user_text_entered_locator).text
