from const import *

from keystoneauth1.identity import v2
from keystoneauth1 import session
from keystoneclient.v2_0 import client

# http://docs.openstack.org/developer/python-keystoneclient/using-api-v2.html

def authenticate():
    auth_url = '{PROTO}://{HOST}:{IDENTITY_PORT}/v2.0'.format(**CONNECTION)

    auth = v2.Password(auth_url=auth_url,
        username=USERNAME,
        password=PASSWORD,
        tenant_name=TENANT,
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

# keystone.projects.list()

# glance_service = keystone.services.create(name="glance",
#     service_type="image",
#     description="OpenStack Image Service")

# tenant = [t for t in keystone.tenants.list() if t.name=='demo'][0]
# new_user = keystone.users.create(name="new_user",
#                                 password="secret",
#                                 tenant_id=tenant.id)
