#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *

db.connect()
db.create_table(Player)

default_players = [
	{'name': 'Sebastian', 'points': 0, 'games': 0},
	{'name': 'Łukasz', 'points': 0, 'games': 0},
	{'name': 'Wojciech', 'points': 0, 'games': 0},
	{'name': 'Aleksandra', 'points': 0, 'games': 0}]

for player in default_players:
    Player.create(**player)
