#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import os
import binascii
from unittestzero import Assert

from pages.home import HomePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage


class TestCreateUser:

    username = 'MozWebUser-' + binascii.b2a_hex(os.urandom(3))
    email = username + '@moztest.com'
    password = 'p@ssw0rd'
    realname = 'Mozilla WebUser Test'

    @pytest.mark.nondestructive
    def test_user_already_exists_error(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user('gbh', TestCreateUser.password,
                                      TestCreateUser.password, TestCreateUser.password, TestCreateUser.realname)
        Assert.true(create_account_pg.is_error_message_present)
        Assert.true(create_account_pg.get_error_message_text().index(
            'Username entered already in use. Please choose a different name.'))

    @pytest.mark.nondestructive
    def test_passwords_mismatch_error(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user(TestCreateUser.username, TestCreateUser.password,
                                      'blah', TestCreateUser.email, TestCreateUser.realname)
        Assert.true(create_account_pg.is_error_message_present)
        Assert.true(create_account_pg.get_error_message_text().index('The passwords you entered do not match.'))

    @pytest.mark.nondestructive
    def test_email_required_error(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user(TestCreateUser.username, TestCreateUser.password,
                                      TestCreateUser.password, '', TestCreateUser.realname)
        Assert.true(create_account_pg.is_error_message_present)
        Assert.true(create_account_pg.get_error_message_text().index('No e-mail address'))

    @pytest.mark.nondestructive
    def test_valid_email_required_error(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user(TestCreateUser.username, TestCreateUser.password,
                                      TestCreateUser.password, 'notValidEmail', TestCreateUser.realname)
        Assert.true(create_account_pg.is_error_message_present)
        Assert.true(create_account_pg.get_error_message_text().index('The e-mail address cannot be accepted '
                                                                     'as it appears to have an invalid format. '
                                                                     'Please enter a well-formatted address or '
                                                                     'empty that field.'))
        # Commenting out this check due to issue https://bugzilla.mozilla.org/show_bug.cgi?id=839457
        # Once the issue is fixed, I'll uncomment the check.
        #
        # create_account_pg.create_user(TestCreateUser.username, TestCreateUser.password,
        #                               TestCreateUser.password, 'notValidEmail@something', TestCreateUser.realname)
        # Assert.true(create_account_pg.is_error_message_present)
        # Assert.true(create_account_pg.get_error_message_text().index('The e-mail address cannot be accepted '
        #                                                              'as it appears to have an invalid format. '
        #                                                              'Please enter a well-formatted address or '
        #                                                              'empty that field.'))

    @pytest.mark.nondestructive
    def test_create_valid_new_user(self, mozwebqa):
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user(TestCreateUser.username, TestCreateUser.password,
                                      TestCreateUser.password, TestCreateUser.email, TestCreateUser.realname)
        Assert.equal(create_account_pg.get_user_created_message(), 'Login successful')
        Assert.equal(create_account_pg.get_user_welcome_message(), 'Welcome, ' + TestCreateUser.username + '!')
