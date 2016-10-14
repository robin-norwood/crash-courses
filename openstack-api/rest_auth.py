from const import *

import requests
import json
import sys
import pprint

# http://developer.openstack.org/api-ref/identity/v2/index.html?expanded=authenticate-detail

auth_request = {
 "auth": {
     "passwordCredentials": {
         "username": USERNAME,
         "password": PASSWORD
     },
     "tenantName": TENANT
 }
}

auth_url = '{PROTO}://{HOST}:{IDENTITY_PORT}/v2.0'.format(**CONNECTION)

def do_auth():
    resp = requests.post(auth_url + '/tokens', json=auth_request)

    if resp.status_code < 200 or resp.status_code >= 300:
        print("ERROR: {0}".format(resp.text))
        sys.exit()

    return resp.json() # Auth token is in response['access']['token']['id']

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

    print(' TOKEN: {0}'.format(auth_response['access']['token']['id']))
    print(' ROLES: {0}'.format(auth_response['access']['metadata']['roles']))
    token = auth_response['access']['token']['id']
    print(' TOKEN: {0}'.format(token))
#    print(get_token_details(token))
    print('-SERVICE CATALOG-')

    for service in auth_response['access']['serviceCatalog']:
        print('--')
        print("NAME: {0}".format(service['name']))
        print("TYPE: {0}".format(service['type']))
        print("PUBLIC URL: {0}".format(service['endpoints'][0]['publicURL']))
