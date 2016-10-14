from const import *

from openstack import connection
from openstack import profile
from openstack import utils

import sys

# http://developer.openstack.org/sdks/python/openstacksdk/users/guides/connect.html

def authenticate():
#    utils.enable_logging(True, stream=sys.stdout)

# http://developer.openstack.org/sdks/python/openstacksdk/users/profile.html#openstack.profile.Profile
    prof = profile.Profile()
    prof.set_region(profile.Profile.ALL, 'RegionOne')

# This line took 2 hours of my life away:
    prof.set_version('identity', 'v2')

    return connection.Connection(
        profile=prof,
        auth_url='{PROTO}://{HOST}:{IDENTITY_PORT}/v2.0'.format(**CONNECTION),
        project_name=PROJECT,
        username=USERNAME,
        password=PASSWORD,
    )


if __name__ == '__main__':
    conn = authenticate()

# This gives me an infinite loop against devstack mitaka/stable :
#
#    for user in conn.identity.users():
#        print(user.name)
#
## FIXME: Bug?

# In general, if you have a _thing_, you can do:
#  conn._service_._thing_s() for a list
#  conn._service_.get_thing_()
#  conn._service_.create_thing_()
#  conn._service_.update_thing_()
#  conn._service_.find_thing_()
#  conn._service_.delete_thing_()

    for flavor in conn.compute.flavors():
        print(flavor)

    for server in conn.compute.servers():
        print(server)
