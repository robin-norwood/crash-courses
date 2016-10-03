(Stolen from James Allen)
Intro
(useful for meetup.com event description)
Snakes and Turtles: Introduction to programming with Python and turtle graphics

Join The Iron Yard instructor Robin Norwood for an introductory crash course targeted at those with little or no programming experience. We'll start by introducing some programming concepts and then use python code to generate graphics. If you want to participate, you’ll need to bring a laptop with wifi and a recent version of Firefox or Chrome web browser installed.

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
Baby Steps:
What is this?
A python “shell” - we enter python code, and trinket interprets it and shows the results right away
Type along with me!
Glorified calculator
Addition, subtraction, multiplication, division, exponents
Kinds of data
Numbers
Integers
Floats
Letters
Strings & characters
Add strings together
Variables
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
More kinds of data
Lists
Lists
List of numbers
List of letters
Index of list
Set value of items in a list
Length of list: len()
Get a sub list
Tuples
Seven dwarfs
Can’t set values of a tuple!
This is called “Immutable”
Sets
Un-ordered lists
Union, difference, intersection...
Booleans
True, False
Equality, inequality, >, <
‘in’
‘If’
iff 3 == 2 + 1: print “Math works!”
If 12 < 3: print “Numbers are numbers!”
If “Grouchy” in dwarves:
None
Different from 0, or ‘’, or False - basically the same as “has no value”
A little more about variables
A single piece of data can have more than one name
But just because two pieces of data have the same value, doesn’t make them the same data!
Is vs ==
type()
Functions
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
Loops
For ___ in ___
For dwarf in dwarfs:
While ___
While dwarf != “Grumpy”
TBD: Comprehensions
little_dwarves = [ d.lower() for d in dwarves ]
TBD: Objects
TBD: Modules
Summary: What have we learned?
A lot. First day or two of an intensive Python course
If your mind isn’t blown, I have failed. That’s ok. This is an introduction.
The zen of python

Break

Turtles
None


What is this thing?
Introduction to “scripts”
Instead of running each line as we type, run the whole “script” at once
Starts with an example, which is nice, but we want to get rid of it and do our own thang
Erase code, start fresh

Learning through play.

The basics:
Import turtle
forward/left/back/right
turtle.shape(‘turtle’)
Draw a square
The obvious way
Use a for loop:
For index in range(0,4):
turtle.forward(50)
turtle.left(90)
Make it a function: draw_square
Why functions are great:
Developers are lazy - we don’t like to repeat ourselves!
No one can do it all. Not using any functions would be like cooking a meal “from scratch” - raising the chickens, growing the wheat, etc
By doing the same thing the same way, we reduce errors - get a specific task right one time, never again - greek upper() example
Optimization - by writing a reusable function, we can spend a lot of time making that function as fast and efficient as possible, where a naive approach might not be so fast.
Encapsulation - don’t have to be an expert in everything, or know about all the details
Add a side_length parameter
Make it generic - draw_polygon function
turtle.speed(“normal”)
This is how programming often works!
Start with an idea
Make a simple version
Make it better
Draw a circle
	turtle.penup()
	turtle.color(color)
	turtle.fillcolor(color)
	turtle.goto(x,y)
	turtle.begin_fill()
	turtle.circle(size)
	turtle.end_fill()
	turtle.pendown()
Let’s make a rainbow!
color/pencolor
square_rainbow function
penup/pendown
round_rainbow function
hideturtle/showturtle
Circle
drawArch function
begin_fill/end_fill
turtle.goto
turtle.write
time.sleep()
Final rainbow
Bonus
Interactivity
screen = Turtle.screen()
# Tell the program which functions go with which keys
screen.onkey(go_left, 'Left')
screen.onkey(go_right, 'Right')
screen.onkey(go_forward, 'Up')
screen.onkey(go_backward, 'Down')

def drag_function(x,y):
  screen.tracer(0)
  tina.clear()
  tina.goto(x,y)
  for chaser in chasers:
    chaser.track(True)
  screen.tracer(1)

tina.ondrag(drag_function)

# Reset the game when the user presses 'r'
screen.onkey(reset,"r")

# Tell the screen to listen for key presses
screen.listen()
turtle.done()
Recursion
Make a tree function
Koch curve
Sierpinski triangle
How to learn more?
If you like to read stuff:
Dive into Python 3
Learn python the hard way
python.org
If you like videos:
Codeschool.com seems ok - lots of others
If you like a 12 week intensive course:
The Iron Yard!

