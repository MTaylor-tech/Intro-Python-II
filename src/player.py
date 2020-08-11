# Write a class to hold player information, e.g. what room they are in
# currently.
import random

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
