import shade
import pprint

# http://docs.openstack.org/infra/shade/

# See clouds.yaml
cloud = shade.openstack_cloud(cloud='robin')

pprint.pprint(cloud.list_servers())
