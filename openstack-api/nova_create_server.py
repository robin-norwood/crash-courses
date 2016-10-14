from const import *
from keystone_auth import authenticate

from novaclient import client

import sys

# http://docs.openstack.org/developer/python-novaclient/api.html

def create_server(name):
    if not name:
        print("Need server name.")
        exit(1)

    session = authenticate()

    # We could also use client.Client()with username and password
    # and the Nova client will auth. Use the session if you use
    # more than one client (Nova, keystone, glance, etc.)
    nova = client.Client(NOVA_API_VERSION, session=session)

    # Cheating - should find the image from glance
    image = 'cc3db5f2-9a00-43ff-96a0-37cd799ac4a0'
    flavor = '1'
    server = nova.servers.create(name, image, flavor)

    print(server)

if __name__ == '__main__':
    name = sys.argv[1]

    create_server(name)
