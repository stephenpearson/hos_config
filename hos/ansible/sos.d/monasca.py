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

from sos.plugins import DebianPlugin
from sos.plugins import Plugin
from sos.plugins import RedHatPlugin


class Monasca(Plugin):
    """Monasca related information
    """

    plugin_name = "monasca"

    def setup(self):
        monasca_files = [
            "/etc/monasca",
            "/etc/kafka",
            "/etc/zookeeper",
            "/opt/storm/current/conf",
            "/opt/vertica/config/admintools.conf",
            "/var/log/monasca/",
            "/var/log/zookeeper/zookeeper.log",
            "/var/log/kafka",
            "/var/log/storm",
            "/var/log/influxdb",
            "/etc/opt/influxdb",
            "/opt/vertica/log/adminTools-dbadmin.log",
            "/var/vertica/catalog/mon/v_mon_node0001_catalog/vertica.log",
            "/var/vertica/catalog/mon/v_mon_node0001_catalog/startup.log",
            "/var/vertica/catalog/mon/v_mon_node0002_catalog/vertica.log",
            "/var/vertica/catalog/mon/v_mon_node0002_catalog/startup.log",
            "/var/vertica/catalog/mon/v_mon_node0003_catalog/vertica.log",
            "/var/vertica/catalog/mon/v_mon_node0003_catalog/startup.log"]

        self.add_copy_spec(monasca_files)


class DebianMonasca(Monasca, DebianPlugin):
    """Monasca related information for Debian distributions
    """
    def setup(self):
        super(DebianMonasca, self).setup()


class RedHatMonasca(Monasca, RedHatPlugin):
    """Monasca related information for RedHat distributions
    """
    def setup(self):
        super(RedHatMonasca, self).setup()
