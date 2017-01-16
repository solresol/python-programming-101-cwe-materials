#!/usr/bin/python

import requests
r = requests.get('http://pokeapi.co/api/v2/pokemon/pikachu')
print [p['ability']['name'] for p in r.json()['abilities']]
