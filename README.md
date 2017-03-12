# Tony

Build your own butler.  
Uses speech recognition to control your device.  
Press the button and talk with him.

- Flask
- xdotool
- python 3.x
- rasa NLU (TODO)
- Watson Speech-to-Text API

## Setup

Currently only running under Linux, tested with Python 3.4.  
You need `xdotool` to run the scripts under `scripts/`.

    $ sudo apt-get install xdotool
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

## Run

To start Tony:

    $ python app.py
    # visit <your-ip>:8080 and talk to Tony

## Add your own actions

Use `actions.py` to define new one-word commands.  
There are some examples to control [Spotify](https://github.com/samuelantonioli/spotify-for-linux),  
you have to modify them (update x and y values for the mouse clicks)  
to make them work for you.  

Look into the `scripts/` directory to see how it works.  
[xdotool manual](http://www.semicomplete.com/projects/xdotool/xdotool.xhtml).  
Don't use `--sync`, otherwise xdotool halts the whole process if an error occurs.  

**TODO:** Use [rasa NLU](https://github.com/golastmile/rasa_nlu) to parse complex commands.  

There are three types of actions:

- simple commands (words/short sentences): e.g. "next" to play the next song
- pattern matching commands (short sentences with parameters): e.g. "play music rick astley"
- complex commands: using natural language understanding (TODO)

## Caution!

This system is not safe. It's passing user input to the shell.  
So please just use it in safe private networks.
I'll work on an API to use it safely.
