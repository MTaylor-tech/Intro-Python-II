# Write a class to hold player information, e.g. what room they are in
# currently.
import random
import textwrap

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
        newRoom = self.current_room.checkDirection(direction)
        if newRoom is self.current_room:
            print('You can\'t go that way.')
        else:
            self.current_room = newRoom

    def take(self, item_name):
        if len(self.current_room.contents) > 0:
            found = False
            for item in self.current_room.contents:
                if item.name.upper() == item_name:
                    self.inventory.append(item)
                    self.current_room.contents.remove(item)
                    found = True
                    print("\nTaken.")
                    item.on_take()
            if not found:
                print("\nI don't see that here.")
        else:
            print("\nI don't see that here.")

    def drop(self, item_name):
        if len(self.inventory) > 0:
            found = False
            for item in self.inventory:
                if item.name.upper() == item_name:
                    self.inventory.remove(item)
                    self.current_room.contents.append(item)
                    found = True
                    print("\nDropped.")
                    item.on_drop()
            if not found:
                print("\nYou don't have that.")
        else:
            print("\nYou don't have that.")

    def look(self, item_name):
        found_item = None
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.name.upper() == item_name:
                    found_item = item
        if len(self.current_room.contents) > 0:
            for item in self.current_room.contents:
                if item.name.upper() == item_name:
                    found_item = item
        if found_item is not None:
            print('\n{}\n'.format(found_item.long_name))
            print(textwrap.fill(found_item.description))
        else:
            print("\nI don't see that here.")

    def pack(self):
        if len(self.inventory) > 0:
            print('\nYour pack contains:')
            for item in self.inventory:
                print(item.long_name)
        else:
            print('\nYour pack is empty.')
