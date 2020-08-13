import random
import textwrap
import pcolors as p
from vars import synonyms
from item import LightSource

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        c = random.randint(1,2)
        if c == 1:
            return "It is you."
        elif c == 2:
            return "That's {}".format(self.name)
        elif c == 3:
            return "I'm not sure, but it might be {}.".format(self.name)

    def go(self, direction):
        new_room = self.current_room.check_direction(direction)
        if new_room is self.current_room:
            p.prRed('You can\'t go that way.')
        else:
            self.current_room = new_room

    def take(self, item_name):
        if item_name in synonyms['ALL']:
            item_list = []
            for item in self.current_room.contents:
                self.inventory.append(item)
                item_list.append(item)
                p.prRed("\nTaken.")
                item.on_take()
            for item in item_list:
                self.current_room.contents.remove(item)
        else:
            item = self.current_room.has_item(item_name)
            if item is not None:
                self.inventory.append(item)
                self.current_room.contents.remove(item)
                p.prRed("\nTaken.")
                item.on_take()
            else:
                p.prRed("\nI don't see that here.")

    def drop(self, item_name):
        if item_name in synonyms['ALL']:
            item_list = []
            for item in self.inventory:
                item_list.append(item)
                self.current_room.contents.append(item)
                p.prRed("\nDropped.")
                item.on_drop()
            for item in item_list:
                self.inventory.remove(item)
        else:
            item = self.has_item(item_name)
            if item is not None:
                self.inventory.remove(item)
                self.current_room.contents.append(item)
                p.prRed("\nDropped.")
                item.on_drop()
            else:
                p.prRed("\nYou don't have that.")

    def look(self, item_name):
        if self.current_room.is_lit(self):
            found_item = None
            if item_name in synonyms['SELF']:
                print('\n{}\n'.format(self.__str__()))
                return
            found_item = self.has_item(item_name)
            item_in_room = self.current_room.has_item_or_feature(item_name)
            if item_in_room is not None:
                found_item = item_in_room
            if found_item is not None:
                print('\n{}\n'.format(found_item.long_name))
                print(textwrap.fill(found_item.description))
            else:
                p.prRed("\nI don't see that here.")
        else:
            p.prGrey('\nIt is too dark to see here.\n')

    def has_item(self, item_name):
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.name.upper() == item_name:
                    return item
        return None

    def has_light(self):
        for item in self.inventory:
            if isinstance(item, LightSource):
                if item.on:
                    return True
        return False

    def pack(self):
        if len(self.inventory) > 0:
            p.prYellow('\nYour pack contains:')
            for item in self.inventory:
                print(item.long_name)
        else:
            p.prRed('\nYour pack is empty.')

    def use(self, item_name):
        item = self.has_item(item_name)
        if item is not None:
            item.use()
        else:
            p.prRed('\nYou don\'t have that item.')
