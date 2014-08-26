#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


class MockUser(dict):

    def __init__(self, **kwargs):

        import os
        import binascii

        self['username'] = 'MozWebUser-' + binascii.b2a_hex(os.urandom(3))
        self['email'] = '%s@moztest.com' % self['username']
        self['password'] = 'p@ssw0rd'
        self['realname'] = 'Mozilla WebUser Test'

        self.update(**kwargs)

    def ___getattr__(self, attr):
        return self[attr]
