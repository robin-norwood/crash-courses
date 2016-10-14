from const import *

from keystoneclient import session
from keystoneclient.v3 import client
from keystoneclient.auth.identity import v3

# http://docs.openstack.org/developer/python-keystoneclient/using-api-v3.html

def authenticate():
    auth_url = '{PROTO}://{HOST}:{IDENTITY_PORT}/v3'.format(**CONNECTION)

    auth = v3.Password(auth_url=auth_url,
        username=USERNAME,
        password=PASSWORD,
        project_name=TENANT
    )

    return session.Session(auth=auth)

if __name__ == '__main__':
    session = authenticate()
    keystone = client.Client(session=session)

    print(' TOKEN: {0}'.format(session.get_token()))

    print('-SERVICE CATALOG-')

    for service in keystone.services.list():
        print('--')
        print("NAME: {0}".format(service.name))
        print("TYPE: {0}".format(service.type))
