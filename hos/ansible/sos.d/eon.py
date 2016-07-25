#
# (c) Copyright 2016 Hewlett Packard Enterprise Development Company LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#

from sos.plugins import DebianPlugin
from sos.plugins import Plugin
from sos.plugins import RedHatPlugin


class Eon(Plugin):
    """eon log information
    """
    plugin_name = "eon"
    option_list = [("log", "gathers all eon logs", "slow", False)]
    packages = ( 'eon', )

    def setup(self):
        super(Eon, self).setup()
        self.add_copy_spec([
            "/var/log/eon/"
        ])


class DebianEon(Eon, DebianPlugin):
    """eon log information on Debian
    """

    def setup(self):
        super(DebianEon, self).setup()


class RedHatEon(Plugin, RedHatPlugin):
    """eon log information on RedHat
    """

    def setup(self):
        super(RedHatEon, self).setup()
