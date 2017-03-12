from os import system, getcwd

SCRIPTS = '{}/scripts'.format(getcwd())

ACTIONS = {
    'next': 'spotify.next',
    'previous': 'spotify.prev',
    'play': 'spotify.toggle_play',
    'stop': 'spotify.toggle_play',
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
    # second: nlu
    p = _parse_command(command)
    if p is None:
        return False
    _exec_script(p[0], p[1])
    return True
