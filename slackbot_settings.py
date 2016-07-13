import os
import csv
import urllib
import random

API_TOKEN = os.getenv('TEAMROCKETKEY')

CHANNEL = '#team-rocket'
DEFAULT_REPLY = (
    'Nothin\' to see here, just another law abidin\' Meowth abidin\''
    ' the law'
)
POKE_URL = (
    'https://raw.githubusercontent.com/veekun/pokedex/master/pokedex/data/'
    'csv/pokemon.csv'
)

POKE_DATA = csv.DictReader(urllib.urlopen(POKE_URL))
POKEMON_LIST = [x['identifier'] for x in POKE_DATA]

TEAM_VALOR_MEMBERS = ['james', 'jsantucci', 'joe', 'jmorrison', 'matt',
                      'mwilliams']

ERRORS_TO = 'jsantucci'


def MOTTO():
    lines = [
        'Prepare for trouble!',
        'Make it double!',
        'To protect the world from devastation!',
        'To unite all peoples within our nation!',
        'To denounce the evils of truth and love!',
        'To extend our reach to the stars above!',
        'Team Rocket, blast off at the speed of light!',
        'Surrender now, or prepare to fight!',
        'Meowth! That\'s right!'
    ]

    return random.choice(lines)
