#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from base import BasePage


class EditWiki(BasePage):
    
    _page_title = 'Editing User:SakshiArora - MozillaWiki'
    _text_entered = 'MozillaUser'
    _edit_box_locator = (By.ID, 'wpTextbox1')
    _save_button_locator = (By.ID, 'wpSave')  
    _user_text = (By.CSS_SELECTOR,'#main-content p')
    @property
    def edit_user(self):
        return self.is_element_present(*self._edit_box_locator)
    
    def edit_user_page(self):
        self.selenium.find_element(*self._edit_box_locator).clear();
        self.selenium.find_element(*self._edit_box_locator).send_keys(EditWiki._text_entered)

    
    @property
    def edit_save(self):
        return self.is_element_present(*self._save_button_locator)
    
    def click_save_page(self):
        self.selenium.find_element(*self._save_button_locator).click()


    @property
    def verify_user_text(self):
        return self.is_element_present(*self._user_text)

