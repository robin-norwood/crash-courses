Title: Learn API Basics to Grab Data with Python! 
Intro
(Useful for meetup.com description)
Connecting the web: APIs for fun and profit

Learn to bring ideas to life on the internet through a crash course in Python!

Python is a versatile language used in a wide variety of industries, and it also makes an excellent “first” language for anyone interested in learning programming.
Python is increasingly applied in the field of scientific research and analysis because of its combination of readability and power. In addition, Python powers many high-profile websites, including Instagram, Pinterest, and YouTube, where it is used to keep the code maintainable and running efficiently.
An API is a way for the creator of a web site or service to let other people write code that uses their data instead of just accessing it through a web browser. As the web gets increasingly complex and interconnected, modern websites and other programmers use APIs to connect their apps to a variety of data and capabilities. 
Join us for a 3-hour Crash Course and learn how to connect to one of the many free APIs available on the internet, retrieve data, and process it with Python. Crash Course attendees will leave the class with a basic understanding of using Python to collect and process data.
The Crash Course will be taught by The Iron Yard's Back-End Engineering instructor, Robin Norwood. Robin came to The Iron Yard with over 15 years of experience as a software developer, product manager, and leader of development teams.
Pre-work for Robin
Set up the docker instance. I used Carina and the jupyter/scipy-notebook image. Steps were

Sign up for Carina at getcarina.com
Create a cluster
Download & unzip the credentials
Run `source ~/docker/python_apis/docker.env`
Run `docker run -P -ti -d jupyter/scipy-notebook`
Run `docker ps` to make sure it started, and note the IP and port
Visit that ip & port in web browser
Who am I?
Developer, product manager, engineering manager for ~15 years at Rackspace and Red Hat. Now I’m an instructor at the Iron Yard
Who are you?
No experience programming?
A little?
Experience with python?
Python experts?
Why are you here?
What do you hope to get out of this?
What to expect?
How will the class go?
Interactive! Fingers on keyboards!
Make mistakes.
I’ll make mistakes too.
...and that’s ok!
Ask questions.
What will we learn?
The very basics of python
How to play with turtle graphics
Learn even more python
Draw some simple graphics on the screen
...then draw some not-so-simple graphics!
How to learn more...
We will probably blow your mind at some point - that’s ok!
Why Python?
Commonly used: Google, facebook, NASA, Rackspace, Red Hat,...
Low barrier to entry, logical and relatively easy to understand
Very powerful
Expressive - a language that tends to focuses on the problem, not the syntax
Everybody has an internet connection and a browser open, right?
...right?



# Python and APIs

Python is a great language for connecting to remote APIs. We can use it to collect, process, and send data over the internet.

## Creating and using your notebook

First, create a new notebook for you to use during the class. Visit (http://104.130.0.141:8888), click on New->Notebooks->Python 3. You should see a new window open with "Jupyter Untitled" in the upper left. Next, click on the "Untitled" and give your notebook a name, like "Steve's Notebook".

Notebooks are made up of *cells*, which can contain different kinds of things. The two things we care about for this class are *Markdown*, for creating text, and *Code* for runnable Python code. When a cell is *active*, you'll see a green or blue border, and you can type into it, or if it's code, run it. You should have a single cell in your notebook; make sure it has a colored border around it, and click the dropdown above it that says 'Code', and change it to 'Markdown'. Now you can type some text in it. Start the first line with a 'hash' and a space to show that it's a header, and type something like "Python and APIs". Then go down to the next line, and type a sentence or five about what you hope to get out of this class.

Once you're done, hit the *escape* key, and then the letter 'B', then the *enter* key. If everything went according to plan, you should have 'In [ ]' and a blinking cursor. This is where you can write some code. We'll spend a few minutes reviewing (or learning for the first time) some Python basics.


## Python Basics

Let's review some basic python, and practice running it in our notebook!

### Data and names for data

One of the basic ideas in any programming language is data. We can enter data directly:

Numbers

```python
5
3.14159
4.7
3 / 4
2 + 8
3 - 7
37 * 3
Letters and words

"Joe"
'Abracadabra'
"John" + " " + "Smith"
Names for data

my_name = "James Dean"
print("Hello, " + my_name)
my_age = 55
print("I am " + str(my_age) + " years old")
```

	Hello, James Dean
	I am 55 years old


### Lists and dictionaries

Each of the kinds of data we already talked about only "hold" one thing at a name; a single number or string. There are two other kinds of data that can hold more than one thing: *lists* and *dictionaries*.


```python
colors = ["red", "orange”, “yellow”, “green”, “blue”, “indigo”, “violet”]
primes = [1, 2, 3, 5, 7, 11, 13, 17]

print(colors[0])
print(primes[0])
print(colors[2:4])

primes[2] = 3
del primes[3]
primes.append(19)
```


Dictionaries:

```
fave_food = {"John": "pizza", "Jill": "pizza", "James": "Steak", "Joseph": "Tofu"}

print("Jill's favorite food is " + fave_food["Jill"])
```

### Loops

Now that we have lists and dictionaries, we might want to do something with everything in them. We can do that with a *for loop*.


```python
for c in colors:
	print(c)
    
for name in fave_food:
	print(name + "'s favorite food is " + fave_food[name])
    
```

	red
	green
	blue
	Joseph's favorite food is Tofu
	Jill's favorite food is pizza
	James's favorite food is Steak
	John's favorite food is pizza

### Boolean logic, if

True, False
Equality, inequality, >, <
‘in’
‘If’
iff 3 == 2 + 1: print “Math works!”
If 12 < 3: print “Numbers are numbers!”

### Loops: for and while

For ___ in ___
For dwarf in dwarfs:
While ___
While dwarf != “Grumpy”


### Modules

One of the ways that programmers work together is to share code with each other. In Python, we call this code that others share *modules*. We use those modules by *importing* them. After importing someone's code, we can use it by name.


```python
import math

print("Would you like some " + str(math.pi) + " ?")

import random

for i in range(5):
	print("Today's color is " + random.choice(colors))

```

	Would you like some 3.141592653589793 ?
	Today's color is red
	Today's color is red
	Today's color is red
	Today's color is green
	Today's color is blue


One doesn't just magically know how a module works. Any good module (or api!) will have documentation. You can read the documentation for the [https://docs.python.org/3/library/math.html] and [https://docs.python.org/3/library/random.html] modules online.

-- 1.5 hour mark should be about here --

## Calling APIs

Ok, now let's get down to business. First, we need to take a few minutes to understand what an API is, and specifically what a web API is.

### APIs and HTTP and other acronyms

API is an acronym that stands for *application programming interface*. That's a fancy way of saying that we're going to run some code somewhere, and get back the result. When we talk about a web API, that code is running on a computer somewhere on the internet. Most web APIs these days use a *protocol* called HTTP. That's a fancy way of saying that they work a lot like web pages. Instead of websites, though, we'll be getting back data we can use in our programs. There's a lot of complexity to HTTP, but for now, we just need to know that we'll be making *requests* to these APIs, and getting back *responses*. To make a request, we need at least two things: The *method*, and the *url*. We can also send some data to the API if we want. The *response* could contain almost anything, but the examples we'll use today will use something called *JSON*, which is a lot like a python dictionary.

### The requests module

Python has a really powerful and easy to use *module* to make HTTP requests, called *requests*. You can read the documentation at (http://docs.python-requests.org)


```python
import requests
from pprint import pprint

resp = requests.get('http://httpbin.org/ip')
print(resp.json())
```

	{'origin': '104.130.0.141'}



```python
post_data = {'words': ['I', 'love', 'cookies']}

resp = requests.post('http://httpbin.org/post', json=post_data)
pprint(resp.json())
```

	{'args': {},
 	'data': '{"words": ["I", "love", "cookies"]}',
 	'files': {},
 	'form': {},
 	'headers': {'Accept': '*/*',
             	'Accept-Encoding': 'gzip, deflate',
             	'Content-Length': '35',
             	'Content-Type': 'application/json',
             	'Host': 'httpbin.org',
             	'User-Agent': 'python-requests/2.10.0'},
 	'json': {'words': ['I', 'love', 'cookies']},
 	'origin': '104.130.0.141',
 	'url': 'http://httpbin.org/post'}



```python
resp = requests.get('https://api.github.com/events')
print("Status: " + str(resp.status_code))
print("Events: " + str(len(resp.json()[0])))

pprint(resp.json()[0]['actor'])
```

	Status: 200
	Events: 8
	{'avatar_url': 'https://avatars.githubusercontent.com/u/1822073?',
 	'display_login': 'opencm',
 	'gravatar_id': '',
 	'id': 1822073,
 	'login': 'opencm',
 	'url': 'https://api.github.com/users/opencm'}



```python
for evt in resp.json():
	print(evt['actor']['login'] + ': ' + evt['actor']['avatar_url'])
```

	opencm: https://avatars.githubusercontent.com/u/1822073?
	AllToTheX: https://avatars.githubusercontent.com/u/13769413?
	theaaronmartin: https://avatars.githubusercontent.com/u/14972947?
	bizley: https://avatars.githubusercontent.com/u/8577314?
	OpenLocalizationTest: https://avatars.githubusercontent.com/u/14175800?
	pimentelfelipe: https://avatars.githubusercontent.com/u/20479063?
	rmwdeveloper: https://avatars.githubusercontent.com/u/6384139?
	alanhamlett: https://avatars.githubusercontent.com/u/522344?
	asridharan: https://avatars.githubusercontent.com/u/3128730?
	veguiman: https://avatars.githubusercontent.com/u/6326956?
	capitaladot: https://avatars.githubusercontent.com/u/1619329?
	DynamicSTOP: https://avatars.githubusercontent.com/u/9434504?
	bderusha: https://avatars.githubusercontent.com/u/444835?
	maxilapo: https://avatars.githubusercontent.com/u/3606588?
	steppnasty: https://avatars.githubusercontent.com/u/987805?
	r0bis: https://avatars.githubusercontent.com/u/183669?
	alisman: https://avatars.githubusercontent.com/u/186521?
	veguiman: https://avatars.githubusercontent.com/u/6326956?
	capitaladot: https://avatars.githubusercontent.com/u/1619329?
	spencerlyon2: https://avatars.githubusercontent.com/u/1001948?
	y-zeng: https://avatars.githubusercontent.com/u/17460127?
	panyaspy: https://avatars.githubusercontent.com/u/8084229?
	szustakd: https://avatars.githubusercontent.com/u/16948980?
	phottell: https://avatars.githubusercontent.com/u/5996223?
	bradgessler: https://avatars.githubusercontent.com/u/4628?
	asridharan: https://avatars.githubusercontent.com/u/3128730?
	2xNibbleMe: https://avatars.githubusercontent.com/u/20526858?
	kc284: https://avatars.githubusercontent.com/u/3705142?
	perlancar: https://avatars.githubusercontent.com/u/211084?
	Lang-ger: https://avatars.githubusercontent.com/u/19306487?


### XKCD API

The popular nerd webcomic XKCD has an API to get info about the comics


```python
resp = requests.get('http://xkcd.com/353/info.0.json')
pprint(resp.json())
```

	{'alt': 'I wrote 20 short programs in Python yesterday.  It was wonderful.  '
        	"Perl, I'm leaving you.",
 	'day': '5',
 	'img': 'http://imgs.xkcd.com/comics/python.png',
 	'link': '',
 	'month': '12',
 	'news': '',
 	'num': 353,
 	'safe_title': 'Python',
 	'title': 'Python',
 	'transcript': '[[ Guy 1 is talking to Guy 2, who is floating in the sky ]]\n'
               	"Guy 1: You're flying! How?\n"
               	'Guy 2: Python!\n'
               	'Guy 2: I learned it last night! Everything is so simple!\n'
               	'Guy 2: Hello world is just \'print "Hello, World!" \'\n'
               	'Guy 1: I dunno... Dynamic typing? Whitespace?\n'
               	"Guy 2: Come join us! Programming is fun again! It's a whole "
               	'new world up here!\n'
               	'Guy 1: But how are you flying?\n'
               	"Guy 2: I just typed 'import antigravity'\n"
               	"Guy 1: That's it?\n"
               	'Guy 2: ...I also sampled everything in the medicine cabinet '
               	'for comparison.\n'
               	'Guy 2: But i think this is the python.\n'
               	'{{ I wrote 20 short programs in Python yesterday.  It was '
               	"wonderful.  Perl, I'm leaving you. }}",
 	'year': '2007'}



```python
from IPython.display import Image
Image(resp.json()['img'])
```




![png](output_18_0.png)



### Star api

From http://hacktheuniverse.github.io/star-api/


```python
resp = requests.get('http://star-api.herokuapp.com/api/v1/stars/Sun')
pprint(resp.json())
```

	{'absmag': 4.85,
 	'appmag': -26.72,
 	'colorb_v': 0.65,
 	'created_at': '2014-11-08T14:49:09.334Z',
 	'dcalc': 0.0,
 	'distly': 0.0,
 	'hipnum': 0.0,
 	'id': 53794,
 	'label': 'Sun',
 	'lum': 0.8913,
 	'plx': 0.0,
 	'plxerr': 0.0,
 	'speed': 0.0,
 	'texnum': 1.0,
 	'updated_at': '2014-11-08T14:49:09.334Z',
 	'vx': 0.0,
 	'vy': 0.0,
 	'vz': 0.0,
 	'x': 0.0,
 	'y': 0.0,
 	'z': 0.0}



```python
resp = requests.get('http://star-api.herokuapp.com/api/v1/stars?max[distly]=100')
pprint(len(resp.json()))
```

	500



```python
exoplanet_data = `
print("Found " + str(len(exoplanet_data.json())) + " exoplanets.")
pprint(exoplanet_data.json()[0])

```

	Found 500 exoplanets.
	{'created_at': '2014-11-08T15:08:27.390Z',
 	'distance': 360.6,
 	'id': 1,
 	'label': '11 Com',
 	'numplanets': 1,
 	'texture': 1,
 	'updated_at': '2014-11-08T15:08:27.390Z',
 	'x': -2.2931,
 	'y': -22.3478,
 	'z': 108.2944}



```python
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

exoplanets = [ planet for planet in exoplanet_data.json() if planet['distance'] < 50 ]
print("Showing " + str(len(exoplanets)) + " planets within 50 light years")
xs = [ exo['x'] for exo in exoplanets ]
ys = [ exo['y'] for exo in exoplanets ]
zs = [ exo['z'] for exo in exoplanets ]

ax.scatter(xs, ys, zs)

ax.scatter([0], [0], [0], c='y', marker='^') # The Sun

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

```

	Showing 37 planets within 50 light years



![png](output_23_1.png)

```python

```

# OMDB

http://www.omdbapi.com/

resp = requests.get('http://www.omdbapi.com/?t=cars 2')
resp.json()

from IPython.display import Image
Image(resp.json()['Poster'])
Authenticating with APIs
So far, we’ve used APIs that don’t require authentication. Authentication is how programs (and people) identify themselves to computers. When you logged into your facebook account, that’s “authentication”. Many APIs require that their users authenticate for a variety of reasons.

# Open weather API

api_key = "&APPID=61852be9461ed55533242bf434a53d6a"

current_weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q=San Antonio" + api_key)
print(current_weather.json()['main']['temp'] * 9/5 - 459.67)



# Instagram

x
