# HTML 5 and Canvas

## Who am I?
Developer, product manager, engineering manager for ~15 years at Rackspace and Red Hat. Now I’m an instructor at the Iron Yard.

## Who are you?

No experience with programming?
Learning?


## Why are you here?
What do you hope to get out of this?

## What to expect? How will the class go?

Interactive! Fingers on keyboards!
Make mistakes.
I’ll make mistakes too.
...and that’s ok!
Ask questions.


## What are we going to do today?

* Add a drawable canvas to web pages
* Make the canvas fill the entire page
* Draw lines, circles, and geometric shapes
* Draw images
* Do simple animations
* Basic composing

## What is HTML?

HTML stands for HyperText Markup Language.

We all intuitively know what a *language* is: a way to express ideas and concepts.

In this case, *markup* means that the things we express in HTML are "marked up" to add structure and meaning to our content.

Another easy concept is *text*: this language is written, not spoken.

The word *hyper* might sound a little fancy, but it just means that our documents include links to other content, like images and other documents.

## What is HTML 5?

HTML 5 is the latest version of HTML, released in 2014, which includes quite a few new features, including the canvas element.

## What is Canvas?

The canvas element gives us a *drawing surface*, conceptually a little like a painters canvas. Instead of paint and paint brushes, we're going to use code and markup to draw on our canvas.

## What is Javascript?

Javascript is a programming language that runs in our web browsers. We'll use some simple javascript to draw on our canvas.

## Getting started

Visit codepen.io/pen

You don't need to sign in, but if you do create a free account, you can save your work.

First, we need to have an HTML Document for our canvas. Since we're going to spend most of our time drawing on the canvas, we don't need much else in our document:

```
<html>
  <body>
    <canvas id="myCanvas"></canvas>
  </body>
</html>
```

While HTML defines the structure of our document, CSS defines the style.

```
canvas#myCanvas {
  width: 600px;
  height: 150px;
  background-color: black;
}
```

Finally, we can get access to our canvas in Javascript:

```
var canvas = document.getElementById('myCanvas');
var ctx = canvas.getContext('2d');
```

This code doesn't actually do anything yet. We need to draw on the canvas.

## Drawing on the canvas

The *context* (`ctx` here) is what we use to actually draw on the canvas. One of the basic methods is to draw rectangles. Canvas differentiates between the *stroke* (or outline) of a shape, and the *fill* (inside) of the shape. We can draw rectangles, either the stroke, the fill, or both.

```
ctx.fillStyle = "blue";
ctx.strokeStyle = "orange";

ctx.rect(10, 20, 50, 75);

ctx.fill();
ctx.stroke();
```

## Colors

We can set colors with the "plain english" names above, or we can give the *rgb value*. The term *RGB* stands for "Red, Green, Blue", and lets us say "how much" red, green, and blue we want in out color.

```
ctx.fillStyle = "rgb(200, 0, 110)"
ctx.rect(10, 20, 50, 75);

ctx.fill()
```

## Paths

If we try to draw more rectangles, we'll soon notice that we can't control the style of each rectangle separately. This is because the fill and stroke style are attached to the *context*, not the rectangle. To get shapes with different styles, we need to use a *path*. A *path* is a set of shapes with the same style.

```
ctx.beginPath();
ctx.fillStyle = "rgb(75, 30, 200)";
ctx.rect(50, 50, 100, 100);
ctx.fill();
ctx.closePath();

ctx.beginPath();
ctx.strokeStyle = "rgb(0, 0, 200)";
ctx.rect(50, 30, 30, 30);
ctx.stroke();
ctx.closePath();
```

You may notice that we're repeating ourselves a lot! When programmers find ourselves doing that, we start to recognize that it's time to write some functions and loops.

A *function* is a bit of code that we can re-use. Most functions have inputs, outputs, and code in the middle, like creating a little machine to do a small part of the work we're doing.

```
function makeRGB(r, g, b) {
  return "rgb(" + r + ", " + g + ", " + b + ")";
}
```

```
function drawRect(ctx, fill, stroke, x, y, w, h) {
  ctx.beginPath();

  ctx.rect(x, y, w, h);

  if (fill) {
    ctx.fillStyle = fill;
    ctx.fill();
  }

  if (stroke) {
    ctx.strokeStyle = stroke;
    ctx.stroke();
  }

  ctx.closePath();

  return;
}

drawRect(
  ctx,
  makeRGB(50, 200, 0),
  0,
  20, 20, 100, 100
  );
```

As our last rectangle trick, let's draw a bunch of random rectangles. First, we want a way to generate a random number.

```
function rnd(max) {
  return Math.floor(Math.random() * (max + 1));
}
```

```
for (var i=0; i<100; i++) {
  drawRect(ctx, randRGB(), randRGB(), rand(550), rand(125), rand(200), rand(200));
}
```

## Lines and shapes

```
ctx.beginPath();
ctx.strokeStyle = makeRGB(250, 0, 30);
ctx.moveTo(30, 20);
ctx.lineTo(175, 100);
ctx.stroke();
ctx.endPath();
```
```
function drawLine(ctx, clr, startX, startY, endX, endY) {
  ctx.beginPath();
  ctx.strokeStyle = clr;
  ctx.moveTo(startX, startY);
  ctx.lineTo(endX, endY);
  ctx.stroke();
  ctx.closePath();

  return;
}

for (var i=0; i<100; i++) {
  drawLine(ctx, randRGB(), rand(600), rand(250), rand(600), rand(250));
}
```

```
function drawTriangle(clr, x1, y1, x2, y2, x3, y3) {
  ctx.beginPath();
  ctx.fillStyle = clr;
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.lineTo(x3, y3);
  ctx.fill();
  ctx.closePath();
}
```

## Circles (and parts of circles)

### The arc function

```
ctx.beginPath();
ctx.fillStyle = "blue";
ctx.arc(100, 50, 75, 0, Math.PI * (3/4), 1);
ctx.fill();
ctx.closePath();
```


```
function drawCircle(fill, stroke, x, y, radius) {
  ctx.beginPath();
  ctx.fillStyle = fill;
  ctx.strokeStyle = stroke;
  ctx.arc(x, y, radius, 0, Math.PI * 2);
  ctx.fill();
  ctx.stroke();
  ctx.closePath();
}
```

```
var gradient = ctx.createLinearGradient(0, 0, 200, 0);
gradient.addColorStop(0, "red");
gradient.addColorStop(.5, "blue");
gradient.addColorStop(1, "green");


ctx.beginPath();
ctx.fillStyle = gradient;
ctx.rect(0, 0, 300, 225);
ctx.fill();
ctx.closePath();
```

```
var gradient = ctx.createRadialGradient(20, 25, 5, 20, 25, 100);
gradient.addColorStop(0, "red");
gradient.addColorStop(.5, "blue");
gradient.addColorStop(1, "green");

ctx.beginPath();
ctx.fillStyle = gradient;
ctx.rect(0, 0, 300, 225);
ctx.fill();
ctx.closePath();
```


### Images

```
var img = new Image();
img.src = 'http://www.cicis.com/media/1243/pizza_adven_zestypepperoni.png';
ctx.drawImage(img, 0, 0);

```
