#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Contest Management System - http://cms-dev.github.io/
# Copyright © 2017 Luca Wehrstedt <luca.wehrstedt@gmail.com>
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""A class to update a dump created by CMS.

Used by ContestImporter and DumpUpdater.

This updater specifies the method contestant passwords are hashed with.

"""

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function


class Updater(object):

    def __init__(self, data):
        assert data["_version"] == 27
        self.objs = data

    def run(self):
        for k, v in self.objs.iteritems():
            if k.startswith("_"):
                continue

            if v["_class"] == "User":
                v["password"] = "plaintext:%s" % v["password"]

            if v["_class"] == "Participation" and v["password"] is not None:
                v["password"] = "plaintext:%s" % v["password"]

        return self.objs
