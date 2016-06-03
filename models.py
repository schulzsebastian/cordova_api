#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *

db = SqliteDatabase('foosball.db')

class Player(Model):
    id = PrimaryKeyField()
    name = CharField()
    points = IntegerField(null = False)

    class Meta:
        database = db