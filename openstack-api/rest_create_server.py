from const import *
from rest_auth import do_auth

import requests
import json
import sys
import pprint

def create_server(name):
    if not name:
        print("Need server name.")
        exit(1)

    auth_response = do_auth()
    server_base_url = [
        svc['endpoints'][0]['publicURL']
        for svc
        in auth_response['access']['serviceCatalog']
        if svc['name'] == 'nova'
        ][0]

    auth_header= {'X-Auth-Token': auth_response['access']['token']['id']}

    # http://developer.openstack.org/api-ref-compute-v2.1.html#createServer

    create_server_request = {
        "server": {
            'name': name,
            'imageRef': 'cc3db5f2-9a00-43ff-96a0-37cd799ac4a0',
            'flavorRef': '1'
        }
    }

    resp = requests.post(
        server_base_url + '/servers',
        headers=auth_header,
        json=create_server_request
        )

    if resp.status_code < 200 or resp.status_code >= 300:
        print("ERROR: {0}".format(resp.text))

        sys.exit()

    pprint.pprint(resp.json())
    return resp.json()

if __name__ == '__main__':
    name = sys.argv[1]

    create_server(name)
