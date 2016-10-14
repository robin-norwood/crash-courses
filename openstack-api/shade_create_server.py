import shade

import sys

# http://docs.openstack.org/infra/shade/usage.html
def create_server(name):
    # See clouds.yaml
    cloud = shade.openstack_cloud(cloud='robin')

    image = cloud.get_image('cirros-0.3.4-x86_64-uec')
    flavor = cloud.get_flavor('m1.tiny')

    # or...
    # image = 'cc3db5f2-9a00-43ff-96a0-37cd799ac4a0'
    # flavor = '1'

    return cloud.create_server(name, image, flavor)

if __name__ == '__main__':
    name = sys.argv[1]

    server = create_server(name)

    print(server)
