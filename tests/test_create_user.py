#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.home import HomePage
from pages.log_in_or_create_account import LogInOrCreateAccountPage
from mocks.mock_user import MockUser


class TestCreateUser:

    @pytest.mark.nondestructive
    def test_user_already_exists_error(self, mozwebqa):
        mock_user = MockUser()
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user('gbh', mock_user['password'],
                                      mock_user['password'], mock_user['email'], mock_user['realname'])
        Assert.true(create_account_pg.is_error_message_present)
        Assert.true(create_account_pg.get_error_message_text.index(
            'Username entered already in use. Please choose a different name.'))

    @pytest.mark.nondestructive
    def test_passwords_mismatch_error(self, mozwebqa):
        mock_user = MockUser()
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user(mock_user['username'], mock_user['password'],
                                      'blah', mock_user['email'], mock_user['realname'])
        Assert.true(create_account_pg.is_error_message_present)
        Assert.true(create_account_pg.get_error_message_text.index('The passwords you entered do not match.'))

    @pytest.mark.nondestructive
    def test_email_required_error(self, mozwebqa):
        mock_user = MockUser()
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user(mock_user['username'], mock_user['password'],
                                      mock_user['password'], '', mock_user['realname'])
        Assert.true(create_account_pg.is_error_message_present)
        Assert.true(create_account_pg.get_error_message_text.index('No email address'))

    @pytest.mark.nondestructive
    def test_valid_email_required_error(self, mozwebqa):
        mock_user = MockUser()
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user(mock_user['username'], mock_user['password'],
                                      mock_user['password'], 'notValidEmail', mock_user['realname'])
        Assert.true(create_account_pg.is_error_message_present)
        Assert.true(create_account_pg.get_error_message_text.index('The email address cannot be accepted as '
                                                                   'it appears to have an invalid format. Please '
                                                                   'enter a well-formatted address or empty that field.'))
        # Commenting out this check due to issue https://bugzilla.mozilla.org/show_bug.cgi?id=839457
        # Once the issue is fixed, I'll uncomment the check.
        #
        # create_account_pg.create_user(mock_user['username'], mock_user['password'],
        #                               mock_user['password'], 'notValidEmail@something', mock_user['realname'])
        # Assert.true(create_account_pg.is_error_message_present)
        # Assert.true(create_account_pg.get_error_message_text.index('The e-mail address cannot be accepted '
        #                                                              'as it appears to have an invalid format. '
        #                                                              'Please enter a well-formatted address or '
        #                                                              'empty that field.'))

    def test_create_valid_new_user(self, mozwebqa):
        mock_user = MockUser()
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_home_page()
        home_pg.personal_tools_region.click_log_in_or_create_account()

        create_account_pg = LogInOrCreateAccountPage(mozwebqa)
        create_account_pg.click_create_account_link()
        create_account_pg.create_user(mock_user['username'], mock_user['password'],
                                      mock_user['password'], mock_user['email'], mock_user['realname'])
        Assert.equal(create_account_pg.get_user_created_message, 'Login successful')
        Assert.equal(create_account_pg.get_user_welcome_message, 'Welcome, ' + mock_user['username'] + '!')
