#!/usr/bin/python
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

import glob
import os
import subprocess
import string
import re

def remove_wwid_from_dict(wwid, block_dict):
    for key in block_dict.keys():
        if wwid == block_dict[key]:
            del block_dict[key]

def main():
    module = AnsibleModule(
        argument_spec=dict()
    )

    block_devices = {}
    for device in os.listdir('/sys/block'):
        if os.path.exists('/sys/block/%s/device' % device):
            # Is this a 100% valid check for scsi devices
            if not device.startswith("sd"):
                continue
            pathname = os.path.join('/dev', device)
            wwid = subprocess.check_output(["/lib/udev/scsi_id", "-g", pathname]).strip()
            block_devices[device] = wwid
    try:
        subprocess.check_output(["/sbin/multipath", "-F"])
    except:
        pass


    root_dev = glob.glob("/dev/mapper/mpath*[a-z]")
    # We are on first run through - only 1 multipath device is possible(root) or
    # or maybe none
    my_list = {}
    if len(root_dev) != 1 and len(root_dev) != 0:
        module.fail_json(rc=256, msg="Incorrect number of device - in correct state %s" % (root_dev))
    if len(root_dev) == 1:
        root_wwid = subprocess.check_output(["/lib/udev/scsi_id", "-g", root_dev[0]]).strip()
        remove_wwid_from_dict(root_wwid, block_devices)
        root_dev[0] = os.path.basename(root_dev[0])
        my_list = {root_wwid:root_dev[0]}

    alpha = list(string.ascii_lowercase)
    beta = alpha
    basename = "sd"
    # 26 * 26 disk devices - initial install
    # Should sort block_devs by length and then for each group alphabetically
    myname = "sd"
    for i in alpha:
        for j in beta:
            name = myname + j
            if name in block_devices.keys():
                block_wwid = block_devices[name]
                if block_wwid in my_list:
                    module.fail_json(rc=256, msg="Inconsistent state in gathering information %s" %
                                    (block_wwid))
                my_list[block_wwid] = re.sub("^sd", "mpath", name)
                remove_wwid_from_dict(block_wwid, block_devices)
                if len(block_devices) == 0:
                    break
        if len(block_devices) == 0:
            break
        myname = basename + i

    module.exit_json(
       bindings = my_list,
        rc=0,
        changed=False
   )


from ansible.module_utils.basic import *    # NOQA

main()
