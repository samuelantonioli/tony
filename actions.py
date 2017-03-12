from os import system, getcwd
import re

SCRIPTS = '{}/scripts'.format(getcwd())

ACTIONS = {
    # spotify
    'next': 'spotify.next',
    'previous': 'spotify.prev',
    'play': 'spotify.toggle_play',
    'stop': 'spotify.toggle_play',
    # audio
    'louder': 'audio.raise',
    'loud': 'audio.raise',

    'quieter': 'audio.lower',
    'quite': 'audio.lower', # pronunciation differences
    'quiet': 'audio.lower',

    'mute': 'audio.toggle_mute',
    'unmute': 'audio.toggle_mute',
    'on mute': 'audio.toggle_mute',
    'newt': 'audio.toggle_mute', # don't know why it detects this

    # youtube
    'close video': 'youtube.close',
}

PATTERN_ACTIONS = {
    'search for (.+)': 'search',
    'play music (.+)': 'spotify.search',
    'play video (.+)': 'youtube.search',
}

def _exec_script(name, args = []):
    system('{}/{}.sh {}'.format(SCRIPTS, name, ' '.join(args)))

def _parse_command(command):
    # TODO:
    # try to detect with rasa NLU
    # https://rasa-nlu.readthedocs.io/en/latest/python.html#prediction-time
    # 
    # interpreter.parse(command)
    # returns _exec_script tuple: (name, args[])
    # return ('youtube.search', ['rick astley'])
    return None

def exec_command(command):
    # first: simple one-word commands
    c = command.lower().replace('.', '').strip()
    if not c:
        return False
    for a in ACTIONS:
        if c == a:
            _exec_script(ACTIONS[a])
            return True
    # second: simple pattern matching commands
    for p in PATTERN_ACTIONS:
        m = re.match(p, c)
        if m is not None:
            _exec_script(PATTERN_ACTIONS[p], m.groups())
            return True
    # third: nlu
    p = _parse_command(command)
    if p is None:
        return False
    _exec_script(p[0], p[1])
    return True
