# Copyright (C) 2016 Hewlett-Packard Development Company, L.P.
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


class Kronos(Plugin):
    """Kronos related information
    """

    plugin_name = "kronos"

    def setup(self):
        kronos_files = [
            "/var/log/elasticsearch",
            "/var/log/beaver",
            "/var/log/logstash",
            "/var/log/kronos",
            "/etc/elasticsearch",
            "/etc/beaver",
            "/etc/logstash"]

        self.add_copy_spec(kronos_files)
        self.gather_elasticsearch_data()

    def gather_elasticsearch_data(self):
        self.add_cmd_output(["curl localhost:9200/_cluster/health?pretty"])


class DebianKronos(Kronos, DebianPlugin):
    """Kronos related information for Debian
    """

    def setup(self):
        super(DebianKronos, self).setup()


class RedHatKronos(Kronos, RedHatPlugin):
    """Kronos related information for RedHat
    """

    def setup(self):
        super(RedHatKronos, self).setup()
