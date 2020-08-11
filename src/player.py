# Write a class to hold player information, e.g. what room they are in
# currently.
import random

class Player:
    def __init__(self,name,currentRoom,description=None,inventory=[]):
        self.name = name
        self.currentRoom = currentRoom
        self.description = description
        self.inventory = inventory
    def __str__(self):
        c = random.randint(1,2)
        if c == 1:
            return "It is you."
        elif c == 2:
            return "That's {}".format(self.name)
        elif c == 3:
            return "I'm not sure, but it might be {}.".format(self.name)
