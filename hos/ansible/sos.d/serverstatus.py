# Copyright (C) 2015 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import subprocess
from sos.plugins import DebianPlugin
from sos.plugins import Plugin
from sos.plugins import RedHatPlugin


class serverstatus(Plugin):

    plugin_name = "serverstatus"

    def common_setup(self, http_status_exe):
        tmp = subprocess.check_output(
            http_status_exe + " -t -D DUMP_VHOSTS | awk 'END{ print $2 }'",
            shell=True)
        tmp2 = tmp.replace("\n", "")
        self.add_cmd_output('wget -qO- http://'+tmp2+'/server-status?auto', suggest_filename="server-status")
        self.add_cmd_output('wget -qO- http://'+tmp2+'/server-status', suggest_filename="server-status.full")


class DebianServerStatus(serverstatus, DebianPlugin):
    """ related information for Debian distributions
    """

    def setup(self):
        self.common_setup('/usr/sbin/apache2ctl')


class RedHatServerStatus(serverstatus, RedHatPlugin):
    """ related information for RedHat distributions
    """

    def setup(self):
        self.common_setup('/usr/sbin/httpd')
