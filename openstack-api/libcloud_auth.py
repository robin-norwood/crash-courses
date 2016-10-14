from const import *

from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

import libcloud.security

# http://libcloud.readthedocs.io/en/latest/compute/examples.html#create-an-openstack-node-using-trystack-org-provider
libcloud.security.VERIFY_SSL_CERT = False

OpenStack = get_driver(Provider.OPENSTACK)

auth_url = '{PROTO}://{HOST}:{IDENTITY_PORT}'.format(**CONNECTION)

driver = OpenStack(USERNAME, PASSWORD,
                secure=False,
                ex_tenant_name=TENANT,
                ex_force_auth_url=auth_url,
                ex_force_auth_version='2.0_password')

print(driver.list_nodes())
