import random
from item import LightSource
from vars import directions, opposites


class Room:
    def __init__(self, name, description, contents=[], lit=True, features=[]):
        self.name = name
        self.description = description
        self.contents = contents
        self.lit = lit
        self.features = features
        self.first_visit = True
        self.exits = {}
        for direction in directions:
            self.exits[direction] = None

    def __str__(self):
        c = random.randint(1,2)
        if c == 1:
            return "It is {}".format(self.name)
        elif c == 2:
            return "That's {}".format(self.name)

    def check_direction(self, direction):
        if self.exits[direction] is not None:
            return self.exits[direction]
        else:
            return self

    def set_direction(self, direction, room):
        if self.exits[direction] is None and\
                room.exits[opposites[direction]] is None:
            self.exits[direction] = room
            room.exits[opposites[direction]] = self

    def is_lit(self, player):
        lit = self.lit
        for item in self.contents:
            if isinstance(item, LightSource):
                lit = True
        for item in player.inventory:
            if isinstance(item, LightSource):
                if item.on:
                    lit = True
        return lit
