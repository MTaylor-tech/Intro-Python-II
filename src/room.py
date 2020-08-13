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
                if item.on:
                    lit = True
        for item in player.inventory:
            if isinstance(item, LightSource):
                if item.on:
                    lit = True
        return lit

    def has_item(self, item_name):
        if len(self.contents) > 0:
            for item in self.contents:
                if item.name.upper() == item_name:
                    return item
        return None

    def has_feature(self, item_name):
        if len(self.features) > 0:
            for item in self.features:
                if item.name.upper() == item_name:
                    return item
        return None

    def has_item_or_feature(self, item_name):
        found_item = has_item(item_name)
        if found_item is None:
            found_item = has_feature(item_name)
        return found_item
