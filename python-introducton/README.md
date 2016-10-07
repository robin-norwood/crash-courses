# Introduction to Python

Join us for an introductory crash course targeted at those with little or no programming experience. We'll learn the basics of Python. Python is a versatile language used in a wide variety of industries, and it also makes an excellent “first” language for anyone interested in learning programming.
The Crash Course will be taught by The Iron Yard's Back-End Engineering instructor, Robin Norwood. Robin came to The Iron Yard with over 15 years of experience as a software developer, product manager, and leader of development teams.

## Who am I?
Developer, product manager, engineering manager for ~15 years at Rackspace and Red Hat. Now I’m an instructor at the Iron Yard

## Who are you?
* No experience programming?
* A little?
* Experience with python?
* Python experts?

## Why are you here?
* What do you hope to get out of this?
* What to expect?
* How will the class go?
* Interactive! Fingers on keyboards!
* Make mistakes.
* I’ll make mistakes too.
* ...and that’s ok!
* Ask questions.

## What will we learn?
* The very basics of python
* How to learn more...
* We will probably blow your mind at some point - that’s ok!

## Why Python?

* Commonly used: Google, facebook, NASA, Rackspace, Red Hat,...
* Low barrier to entry, logical and relatively easy to understand
* Very powerful
* Expressive - a language that tends to focuses on the problem, not the syntax

## Getting started

Everybody has an internet connection and a browser open, right?
...right?

Baby Steps

What is this?

A python “shell” - we enter python code, and trinket interprets it and shows the results right away
Type along with me!

## Glorified calculator
Addition, subtraction, multiplication, division, exponents

## Kinds of data
Numbers
Integers
Floats
Letters
Strings & characters
Add strings together

## Variables
Assignment:
my_number = 5
my_name = “Robin”
print()
Get a substring: []
Most programming languages start counting at 0!
a_string[startAt:endBefore]
Re-assignment
my_name = “Joe”
my_number = 12
+=, -=
Variables in python are just names for data
Any valid name can “point to” any kind of data
“Dynamically typed”

## More kinds of data

### Lists
Lists
List of numbers
Index of list
List of letters
Mixed list
Set value of items in a list
Length of list: len()
Get a sub list

### Tuples
Seven dwarfs
Can’t set values of a tuple!
This is called “Immutable”

### Sets
Un-ordered lists
Union, difference, intersection...

### Dictionaries
Sort of like a “look up table”
Ages = {‘Collin’: 16, …}
ages[‘Collin’] += 1

### Booleans
True, False
Equality, inequality, >, <
‘in’
‘If’
iff 3 == 2 + 1: print “Math works!”
If 12 < 3: print “Numbers are numbers!”
If “Grouchy” in dwarves:
None
Different from 0, or ‘’, or False - basically the same as “has no value”

## A little more about variables
A single piece of data can have more than one name
But just because two pieces of data have the same value, doesn’t make them the same data!
Is vs ==
type()

## Functions
Functions do stuff with data
Function/machine analogy
Draw a picture of a function:
Name
Arguments
Body
Return values
Some built in functions:
Do stuff with data
Strings: split, upper, lower, len(), etc...
Lists: append(), pop()
Dictionaries: keys(), values()
print()
sum()
int()
float()
round(float)
str()

### Make your own functions
greet()
area_of_circle() - import math; math.pi
round()
dwarf_of_the_day()
Import random
dwarves = (“Doc”, “Grumpy”, “Happy”, “Sleepy”, “Bashful”, “Sneezy”, “Dopey”)
random.choice(dwarves)

### Why functions are great:
Developers are lazy - we don’t like to repeat ourselves!
No one can do it all. Not using any functions would be like cooking a meal “from scratch” - raising the chickens, growing the wheat, etc
By doing the same thing the same way, we reduce errors - get a specific task right one time, never again - greek upper() example
Optimization - by writing a reusable function, we can spend a lot of time making that function as fast and efficient as possible, where a naive approach might not be so fast.
Encapsulation - don’t have to be an expert in everything, or know about all the details


## Loops
For ___ in ___
For dwarf in dwarfs:
While ___
While dwarf != “Grumpy”
TBD: Comprehensions
little_dwarves = [ d.lower() for d in dwarves ]
TBD: Objects
TBD: Modules

## Summary: What have we learned?

* A lot. First day or two of an intensive Python course
* If your mind isn’t blown, I have failed. That’s ok. This is an introduction.
* The zen of python
