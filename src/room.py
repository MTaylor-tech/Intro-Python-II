# Implement a class to hold room information. This should have name and
# description attributes.
import random

class Room:
    def __init__(self,name,description,firstVisit=True,n_to=None,s_to=None,
                 e_to=None,w_to=None):
        self.name = name
        self.description = description
        self.firstVisit = firstVisit
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    def __str__(self):
        c = random.randint(1,2)
        if c == 1:
            return "It is {}".format(self.name)
        elif c == 2:
            return "That's {}".format(self.name)
