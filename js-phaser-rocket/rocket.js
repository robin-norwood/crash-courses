function preload() {
    game.load.baseURL = 'https://s3.amazonaws.com/robinrocketdemo/';
    game.load.crossOrigin = 'anonymous';

    game.load.image('rocket', 'sls-small.png');
}

function create() {
    game.physics.startSystem(Phaser.Physics.ARCADE);

    rocket = game.add.sprite(345, 300, 'rocket');

    game.physics.enable(rocket, Phaser.Physics.ARCADE);
    rocket.inputEnabled = true;
    rocket.events.onInputDown.add(onClick, this);

    launch = false;
    countdown = false;
    counter = 10;

    clock = game.add.text(50, 16, '', { fill: 'yellow' });
}

function onClick() {
    countdown = true;
}



function update() {

    if (countdown === true) {
        counter -= .02;
        clock.text = Math.round(counter);
    }

    if (counter <= 0) {
        countdown = false;
        counter = 10;
        clock.text = 'Blast off!';
        launch = true;
    }

    if (launch === true) {
        rocket.body.velocity.y -= 1;
    }

}


function render() {

}
