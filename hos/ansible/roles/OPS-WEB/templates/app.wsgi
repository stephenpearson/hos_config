{# (c) Copyright 2015 Hewlett Packard Enterprise Development Company LP #}
# This file is used to integrate our pecan application into an apache web
# server with mod-wsgi.
#
# For more information, refer to:
# http://pecan.readthedocs.org/en/latest/deployment.html#common-recipes
import os
from pecan.deploy import deploy

if os.path.isfile('{{ ops_console_config }}'):
    config_file = '{{ ops_console_config }}'
else:
    config_file = '{{ ops_console_config_old }}'

application = deploy(config_file)
