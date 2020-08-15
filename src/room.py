import random
from item import LightSource
from vars import directions, opposites
from player import NonPlayerCharacter


class Room:
    def __init__(self, tag, name, description, lit=True):
        self.tag = tag
        self.name = name
        self.description = description
        self.contents = []
        self.lit = lit
        self.features = []
        self.first_visit = True
        self.characters = []
        self.visible_exits = []
        self.exits = {}
        for direction in directions:
            self.exits[direction] = None

    def check_direction(self, direction):
        if self.exits[direction] is not None:
            return self.exits[direction]
        else:
            return self

    def set_direction(self, direction, room, visible):
        if self.exits[direction] is None and\
                room.exits[opposites[direction]] is None:
            self.exits[direction] = room
            room.exits[opposites[direction]] = self
            if visible:
                self.visible_exits.append(direction)
                room.visible_exits.append(opposites[direction])

    def is_lit(self, player):
        lit = self.lit
        for item in self.contents:
            if isinstance(item, LightSource):
                if item.on:
                    return True
        for char in self.characters:
            if char.has_light():
                return True
        return lit

    def has_item(self, item_name):
        if len(self.contents) > 0:
            for item in self.contents:
                if item_name in item.name.upper():
                    return item
        return None

    def has_feature(self, item_name):
        if len(self.features) > 0:
            for item in self.features:
                if item_name in item.name.upper():
                    return item
        return None

    def has_item_or_feature(self, item_name):
        found_item = self.has_item(item_name)
        if found_item is None:
            found_item = self.has_feature(item_name)
        return found_item

    def has_ifc(self,query):
        found_item = self.has_item_or_feature(query)
        if found_item is None:
            found_item = self.has_char(query)
        return found_item

    def has_char(self, char_name):
        if len(self.characters) > 0:
            for char in self.characters:
                if isinstance(char,NonPlayerCharacter):
                    if char_name in char.name.upper() or char_name in char.long_name.upper():
                        return char
        return None

    def has_player(self):
        if len(self.characters) > 0:
            for char in self.characters:
                if not isinstance(char,NonPlayerCharacter):
                    return char
        return None

    def add_item(self, item):
        self.contents.append(item)

    def rm_item(self, item):
        self.contents.remove(item)

    def add_feature(self, item):
        self.features.append(item)

    def rm_feature(self, item):
        self.features.remove(item)
