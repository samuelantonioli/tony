from os import system, getcwd
import re


SHORTCUTS = {
    'eg': 'Eugen Cicero',
    'e g': 'Eugen Cicero',
}

ACTIONS, HANDLERS = {}, {}

def action(name, pattern):
    def wrapper(f):
        HANDLERS[name] = f
        return f
    if pattern:
        ACTIONS[pattern] = name
    return wrapper

# # # # # # # # # # # #
# define your actions #
# # # # # # # # # # # #

SCRIPTS = '{}/scripts'.format(getcwd())

def _exec_script(name, args = []):
    try:
        args = filter(lambda x: x is not None, args)
        system('{}/{}.sh {}'.format(SCRIPTS, name, ' '.join(args)))
        return True
    except Exception:
        return False

# spotify

@action('spotify.next', '^next$')
def spotify_next():
    return _exec_script('spotify.next')

@action('spotify.prev', '^previous$')
def spotify_prev():
    return _exec_script('spotify.prev')

@action('spotify.toggle_play', '^(play|stop)$')
def spotify_toggle_play():
    return _exec_script('spotify.toggle_play')

@action('spotify.search', '^play music (.+)$')
def spotify_search(*args):
    return _exec_script('spotify.search', args)

# audio

@action('audio.raise', '^(?:louder|loud)(?:\s+(\d+))?$')
def audio_raise(*args):
    return _exec_script('audio.raise', args)

@action('audio.lower', '^(?:quieter|quiet|quite)(?:\s+(\d+))?$')
def audio_lower(*args):
    return _exec_script('audio.lower', args)

# don't know why it detects newt
@action('audio.toggle_mute', '^(?:mute|unmute|on mute|newt)$')
def audio_toggle_mute():
    return _exec_script('audio.toggle_mute')

# youtube

@action('youtube.search', '^play video (.+)$')
def youtube_search(*args):
    return _exec_script('youtube.search', args)

@action('youtube.close', '^close video$')
def youtube_close():
    return _exec_script('youtube.close')

# search

@action('search', '^search (.+)$')
def google_search(*args):
    return _exec_script('search', args)

# # # # # # # # # # # # # # # # # # # # # #

def _exec_action(name, args = [], kwargs = {}):
    f = HANDLERS.get(name, None)
    if f is not None and callable(f):
        try:
            return True if f(*args, **kwargs) else False
        except Exception:
            pass
    return False

def _parse_command(command):
    # TODO:
    # try to detect with rasa NLU
    # https://rasa-nlu.readthedocs.io/en/latest/python.html#prediction-time
    # 
    # interpreter.parse(command)
    # returns _exec_script tuple: (name, args[])
    # return ('youtube.search', ['rick astley'])
    return None

def _replace_shortcuts(args):
    new_args = list()
    keys = SHORTCUTS.keys()
    for arg in args:
        if arg in keys:
            new_args.append(SHORTCUTS[arg])
        else:
            new_args.append(arg)
    return new_args

def exec_command(command):
    # first: simple pattern matching commands + one-word commands
    c = command.lower().replace('.', '').strip()
    if not c:
        return False
    for p in ACTIONS:
        m = re.match(p, c)
        if m is not None:
            return _exec_action(ACTIONS[p], _replace_shortcuts(m.groups()))
    # second: nlu
    p = _parse_command(command)
    if p is None:
        return False
    return _exec_action(p[0], p[1])
