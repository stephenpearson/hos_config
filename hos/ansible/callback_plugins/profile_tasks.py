#
# (c) Copyright 2015 Hewlett Packard Enterprise Development Company LP
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
import os
import time


class CallbackModule(object):
    """A plugin for timing tasks."""

    def __init__(self):
        self.stats = []
        self.start = time.time()
        self.current = None
        self.current_start = None

    def playbook_on_task_start(self, name, is_conditional):
        """Logs the start of each task."""

        if os.getenv("ANSIBLE_PROFILE_DISABLE") is not None:
            return

        if self.current_start is not None:
            # Record the running time of the last executed task
            self.stats.append((self.current, time.time() - self.current_start))

        # Record the start time of the current task
        self.current = name
        self.current_start = time.time()

    def playbook_on_stats(self, stats):
        """Prints the timings."""

        if os.getenv("ANSIBLE_PROFILE_DISABLE") is not None:
            return

        # Record the timing of the very last task
        if self.current_start is not None:
            self.stats.append((self.current, time.time() - self.current_start))

        # Sort the tasks by their running time
        results = sorted(
            self.stats,
            key=lambda value: value[1],
            reverse=True,
        )

        if os.getenv("ANSIBLE_PROFILE_SHOW_ALL") is None:
            # Just keep the top 10
            results = results[:10]

        # Print the timings
        for name, elapsed in results:
            print(
                "{0:-<70}{1:->9}".format(
                    '{0} '.format(name),
                    ' {0:.02f}s'.format(elapsed),
                )
            )
        print("{0:-<79}".format("-"))
        print("{0:-<70}{1:->9}".format(
            '{0} '.format("Total:"),
            ' {0:.02f}s'.format(time.time() - self.start),
        ))
