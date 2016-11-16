# Fly a rocket with Phaser

Notes and code for a simple rocket demo use the Phaser javascript library. I used this code to lead groups of middle schoolers for the phenomenon210.org program in November 2016.

The Rocket image used in this lesson is a mockup of the Space Launch System, NASA's next generation launch system which will replace the Space Shuttle. The image is from: http://blogs.nasa.gov/commercialcrew/wp-content/uploads/sites/230/2015/06/SLS-conceptwhite-cropped.jpg

I modified it by changing the background to transparent, and shrinking it to 109 x 300. I hope NASA doesn't mind...I don't want to be sent to space prison.

## Getting started

Phaser is a library of code that helps create simple animations and games. We'll use it today to make a rocket fly off the screen. First, go to phaser.io/sandbox and click on 'Create Blank Project'.

You'll see an editor with six tabs at the top. We'll start in the 'preload' tab. We need to load the picture of the rocket into our game, which means a little typing:

```
function preload() {
    game.load.baseURL = 'https://s3.amazonaws.com/robinrocketdemo/';
    game.load.crossOrigin = 'anonymous';

    game.load.image('rocket', 'sls-small.png');
}
```

Next, we need to put the rocket on the screen. Go to the 'create' tab to create it:

```
function create() {
  rocket = game.add.sprite(0, 0, 'rocket');
}
```

In computer games, a "sprite" is a thing that moves around the screen...like a character, pokemon, or in this case, a rocket. Our rocket won't move yet, but it will soon.

The two zeros tell the game the location of the sprite. "0, 0" is the upper left hand corner. If we want to move it across the screen, we add to the first number (sometimes called the "x" position). To move it down the screen, we add to the second number (the "y" position).

```
rocket = game.add.sprite(350, 300, 'rocket');
```

Now our rocket is on the launch pad, but we still need to launch it.

## Our countdown clock

In the 'create()' function:

```
counter = 10;
countdown = true;

clock = game.add.text(50, 25, counter, { fill: 'yellow' });
```

### Start the count down

In update():

```
if (countdown === true) {
    counter -= .02;
    clock.text = Math.round(counter);
}

if (counter <= 0) {
    countdown = false;
    counter = 10;
    clock.text = 'Blast off!';
}
```

So, now we should have a counter, but no launch! Let's add that.

In `create()`:

```
rocket = game.add.sprite(350, 300, 'rocket');

game.physics.startSystem(Phaser.Physics.ARCADE);
game.physics.enable(rocket, Phaser.Physics.ARCADE);

launch = false;
```

The in update(), we need to add two things:

```
clock.text = 'Blast off!';
launch = true;
```

And below that, let's move the rocket up a little faster each time we update:

```
if (launch === true) {
    rocket.body.velocity.y -= 1;
}
```
