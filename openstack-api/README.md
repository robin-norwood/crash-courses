# Managing OpenStack with Python

 We’ll learn how to connect to and manage your OpenStack instance with Python and the OpenStack API. We’ll also explore a few simple use cases for adding automation to your OpenStack environment. Some knowledge of Python will be helpful to follow along, but isn’t required.

## Installing Devstack

I'm not talking about installing devstack today, but what I did was:

1. Created an 8gb vm running Ubuntu 14.04.5 x64 on digital ocean
2. Followed this blog post: https://www.datadoghq.com/blog/install-openstack-in-two-commands/

## First major hurdle

I first tried OpenStack Liberty, and ran into some major hurdles. To keep it short, OpenStack documentation, libraries, and the various blog posts and other resources don't do a great job of distinguishing between which versions support what, and often names, concepts, and usage change between versions in a way that seems arbitrary unless you live and breathe openstack ("tenant" vs "project" for instance). In my experience, using the latest version of OpenStack generally works with the documentation and libaries, but "older" versions can be quite painful. I suspect you already know that, though. For these examples, I ended up using Mitaka, simply because it (mostly) worked.

## Many ways to connect to the OpenStack APIs

Each OpenStack project maintains its own set of REST APIs, as well as command line clients, and SDKs in various languages. This means that support for projects and features can vary widely from project to project and SDK to SDK. In addition to the per-project APIs, there are (at least) two Python libraries in active development that are intended to provide a unified interface to all of the OpenStack projects: *openstacksdk* and *shade*. Finally, *Apache libcloud* is another Python library intended to interact with all major commercial and free cloud providers (Rackspace, OpenStack, AWS, DigitalOcean, et. al.).

So, if you've been keeping score, that makes at least *five* different ways to manage your OpenStack deployments with Python. First we'll do a flyover of these methods, then dive into a few with working examples.

## Flyover: How to OpenStack with Python

Unfortunately, there is no perfect solution. The different options we'll talk about today each have their strengths and weaknesses. On the bright side, since OpenStack projects generally use REST for their APIs, and Python for their commandline clients, we can do almost anything we want to with Python.

All things considered, Python is probably the best language to use to automate your OpenStack cloud. Not only is it awesome all by itself, many OpenStack projects use Python both for their implementation and client libraries.

We'll look at all five different ways to use Python to automate your OpenStack API, spending the most time on the official OpenStack SDK.

## Second major hurdle

Error messages. Again, I'm sure you've all dealt with this pain way more than me, but the error messages suck. They seem to vacillate between generic and downright fraudulent. To compound that, between the various versions of each component, the almost infinite ways to install and configure OpenStack, getting code to work across more than a single deployment, even using the API, is quite a challenge. The higher-level APIs we'll talk about later help with this a bit, but unfortunately can sometimes interject their own level of complexity to make debugging "fun".

### Direct REST access

http://developer.openstack.org/api-guide/quick-start/

The most direct way to access the OpenStack API is with the REST clients maintained by each project. Since each project maintains its own API, in theory, these APIs should be up to date and support all the features provided by each component.

#### You want this if...

* You're using new features from a development snapshot of OpenStack
* A feature you need isn't supported by the SDKs yet
* You really like using REST directly
* You really, *really* like JSON
* You have too much time on your hands

#### You don't want this if...

* You don't like handling errors manually
* You use different versions/implementations of OpenStack
* You don't like keeping up with low-level API changes when you update OpenStack
* You don't like reading obscure and often inconsistent API docs
* You probably don't want to use this, unless you absolutely have to

In addition to the above, you'll increasingly see OpenStack developers say "Don't use the REST API, use the libraries" if you ask for help with the REST API.

#### Demo

* rest_auth.py - Auth against the v2 API
* rest_v3_auth.py - Auth against the v3 API
* rest_create_server.py - Create a server


### Per-project SDKs

https://wiki.openstack.org/wiki/OpenStackClients

Each project maintains its own commandline client, most of which ship with a Python SDK. Since each project is responsible for these, they tend to include new features as they are created. Also, they tend to match the commandline tools very closely.

#### You want this if...

* You only need to automate one or two components of OpenStack
* You need a feature that isn't supported by the other SDKs yet
* You're transitioning from using the commandline clients

#### You don't want this if...

* You use several different OpenStack versions or components
* You don't want to keep track of changes each time a new client is released
* You like consistency
* You're working with more than just OpenStack

The python SDKs tend to track very well with versions of each component, since they are closely tied to the commandline clients. However, there can be some consistency issues between them, and the docs tend to be fairly sparse and low level. Similar to using the REST APIs, I think many OpenStack developers would tell you to use either the OpenStack SDK or shade.

#### Demo

* keystone_auth.py - authenticate with keystone
* keystone_v3_auth.py - authenticate with keystone v3
* nova_create_server.py - create a server

### OpenStack SDK

http://developer.openstack.org/sdks/python/openstacksdk/users/index.html

https://www.openstack.org/summit/vancouver-2015/summit-videos/presentation/building-applications-using-the-openstack-sdk

The OpenStack SDK Python module wraps the per-project APIs, and provides a unified interface to all the major OpenStack components.

#### You want this if...

* This is probably the one you want
* You want to use Python to do complex management of your OpenStack cloud

#### You don't want this if...

* You manage multi-cloud deployments running different versions or from different vendors
* It doesn't support specific features you need
* You're using something older than Mitaka (but this could have just been my own experience)
* You're working with more than just OpenStack

#### Demo

* openstack_auth - authenticate (v2 only)
* openstack_create_server - create a server


### OpenStack shade

http://docs.openstack.org/infra/shade/
https://github.com/openstack/os-client-config

The OpenStack shade project is intended to provide a simple SDK that is compatible with both free and commercial OpenStack deployments. On the plus side, it is pretty "pythonic" and it "just works", at least in the simple examples I used. For minuses, it explicitly doesn't seek to support every possible OpenStack feature, and having a single flat namespace for all features and functions means finding out what it can do can be a bit of a pain.

#### You want this if...

* You want to do a few simple things, especially across multiple OpenStack clouds (internal, Rackspace, Red Hat, et. al.)
* You use and like Ansible (shade is based on code developed in Ansible)
* Openstack isn't your full-time job, you just want to get something done

#### You don't want this if...

* You need more features than shade provides
* You're working with more than just OpenStack

#### Demo

* shade_auth.py - authenticate
* shade_create_server.py

### Apache libcloud

http://libcloud.readthedocs.io/en/latest/compute/drivers/openstack.html
http://libcloud.readthedocs.io/en/latest/compute/examples.html

Apache libcloud is designed to abstract any cloud - OpenStack or otherwise. It includes providers for OpenStack, as well as many commercial options. This is probably the most ambitious of the libraries we cover.

#### You want this if...

* You want to work with not just OpenStack, but also other clouds in a seamless(-ish) way

#### You don't want this if...

* It doesn't support features you need
* You don't plan to support non-OpenStack clouds
