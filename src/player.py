import random
import textwrap
import pcolors as p
from vars import synonyms

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
        if len(self.current_room.contents) > 0:
            found = False
            for item in self.current_room.contents:
                if item.name.upper() == item_name:
                    self.inventory.append(item)
                    self.current_room.contents.remove(item)
                    found = True
                    p.prRed("\nTaken.")
                    item.on_take()
            if not found:
                p.prRed("\nI don't see that here.")
        else:
            p.prRed("\nI don't see that here.")

    def drop(self, item_name):
        if len(self.inventory) > 0:
            found = False
            for item in self.inventory:
                if item.name.upper() == item_name:
                    self.inventory.remove(item)
                    self.current_room.contents.append(item)
                    found = True
                    p.prRed("\nDropped.")
                    item.on_drop()
            if not found:
                p.prRed("\nYou don't have that.")
        else:
            p.prRed("\nYou don't have that.")

    def look(self, item_name):
        if self.current_room.is_lit(self):
            found_item = None
            if item_name in synonyms['SELF']:
                print('\n{}\n'.format(self.__str__()))
                return
            found_item = self.has_item(item_name)
            if len(self.current_room.contents) > 0:
                for item in self.current_room.contents:
                    if item.name.upper() == item_name:
                        found_item = item
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
