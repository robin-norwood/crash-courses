from const import *

import requests
import json
import sys
import pprint

# http://developer.openstack.org/api-ref/identity/v3/index.html?expanded=authenticate-detail

auth_request = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": USERNAME,
                    "domain": {
                        "id": "default"
                    },
                    "password": PASSWORD
                }
            }
        },
    }
}

auth_url = '{PROTO}://{HOST}:{IDENTITY_PORT}/v3/auth'.format(**CONNECTION)

def do_auth():
    resp = requests.post(auth_url + '/tokens', json=auth_request)

    if resp.status_code < 200 or resp.status_code >= 300:
        print("ERROR: {0}".format(resp.text))
        sys.exit()

    return resp.json() # Auth token is in response['token']['user']['id']

def get_service_catalog(token):
    auth_header = {'X-Auth-Token': token,
        'Content-Type': 'application/json'}
    resp = requests.get(auth_url + '/catalog', headers=auth_header)

    if resp.status_code < 200 or resp.status_code >= 300:
        print("ERROR: {0}".format(resp.text))
        sys.exit()

    return resp.json() # Auth token is in response['token']['user']['id']

def get_token_details(token):
    auth_header = {'X-Auth-Token': token,
        'X-Subject-Token': token,
        'Content-Type': 'application/json'}
    resp = requests.get(auth_url + '/tokens', headers=auth_header)

    if resp.status_code < 200 or resp.status_code >= 300:
        print("ERROR: {0}".format(resp.text))
        sys.exit()

    return resp.json() # Auth token is in response['token']['user']['id']


if __name__ == '__main__':
    print('USER: {0}'.format(USERNAME))
    auth_response = do_auth()

    token = auth_response['token']['user']['id']
    print(' TOKEN: {0}'.format(token))
    print(get_token_details(token))

    print('-SERVICE CATALOG-')
    catalog = get_service_catalog(token)

    for service in catalog['catalog']:
        print(service)
