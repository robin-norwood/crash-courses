from const import *

from openstack_auth import authenticate

import sys

# http://developer.openstack.org/sdks/python/openstacksdk/users/guides/compute.html

def create_server(name):
    if not name:
        print("Need server name.")
        exit(1)

    conn = authenticate()

    # FIXME: This "should work (TM)", but gives me error:
    #  "TypeError: openstack.compute.v2.flavor ... is not JSON serializable"

    # image = conn.compute.find_image('cirros-0.3.4-x86_64-uec')
    # flavor = conn.compute.find_flavor('m1.tiny')
    #
    # server = conn.compute.create_server(name=name, flavor=flavor, image=image)

    # You can also specify image and flavor ID:
    image = 'cc3db5f2-9a00-43ff-96a0-37cd799ac4a0'
    flavor = '1'

    server = conn.compute.create_server(name=name, flavor_id=flavor, image_id=image)

    return server

if __name__ == '__main__':
    name = sys.argv[1]

    server = create_server(name)

    print(server)
