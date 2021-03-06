# Copyright 2008-2015 Canonical
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# For further info, check  http://launchpad.net/filesync-server

"""Test versioninfo"""

__metaclass__ = type

import unittest
from versioninfo import version_info


class VersionInfoTestCase(unittest.TestCase):
    """Test a the autogenerated version_info dict"""
    def testInfo(self):
        """Validate the available data."""
        self.assert_(version_info['revno'], "Revison Number")
        self.assert_(version_info['branch_nick'], "Branch Nickname")
        self.assert_(version_info['date'], "Date of last update")
        self.assert_(version_info['build_date'], "Date of last Build")
        self.assert_(version_info['revision_id'], "ID of revision")


def test_suite():
    """Return a suite of versioninfo."""
    suite = unittest.TestSuite()
    suite.addTest(VersionInfoTestCase('testInfo'))
    return suite
