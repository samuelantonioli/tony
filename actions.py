from os import system, getcwd
import re

SCRIPTS = '{}/scripts'.format(getcwd())

ACTIONS = {
    # spotify
    'next': 'spotify.next',
    'previous': 'spotify.prev',
    'play': 'spotify.toggle_play',
    'stop': 'spotify.toggle_play',
    # youtube
    'close video': 'youtube.close',
}

PATTERN_ACTIONS = {
    # audio
    '(?:louder|loud)(?:\s+(\d+))?': 'audio.raise',
    '(?:quieter|quiet|quite)(?:\s+(\d+))?': 'audio.lower',
    '(?:mute|unmute|on mute|newt)': 'audio.toggle_mute', # don't know why it detects newt
    # search
    'search (.+)': 'search',
    'play music (.+)': 'spotify.search',
    'play video (.+)': 'youtube.search',
}

SHORTCUTS = {
    'eg': 'Eugen Cicero',
    'e g': 'Eugen Cicero',
}

def _exec_script(name, args = []):
    try:
        system('{}/{}.sh {}'.format(SCRIPTS, name, ' '.join(args)))
        return True
    except Exception:
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
    # first: simple one-word commands
    c = command.lower().replace('.', '').strip()
    if not c:
        return False
    for a in ACTIONS:
        if c == a:
            return _exec_script(ACTIONS[a])
    # second: simple pattern matching commands
    for p in PATTERN_ACTIONS:
        m = re.match(p, c)
        if m is not None:
            return _exec_script(PATTERN_ACTIONS[p], _replace_shortcuts(m.groups()))
    # third: nlu
    p = _parse_command(command)
    if p is None:
        return False
    return _exec_script(p[0], p[1])
