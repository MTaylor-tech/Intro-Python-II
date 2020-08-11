# Implement a class to hold room information. This should have name and
# description attributes.
# * Put the Room class in `room.py` based on what you see in `adv.py`.
  #
  # * The room should have `name` and `description` attributes.
  #
  # * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
  #   which point to the room in that respective direction.

import random

class Room:
    def __init__(self, name, description, contents=[], n_to=None, s_to=None,
                 e_to=None, w_to=None, u_to=None, d_to=None):
        self.name = name
        self.description = description
        self.contents = contents
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.u_to = u_to
        self.d_to = d_to

    def __str__(self):
        c = random.randint(1,2)
        if c == 1:
            return "It is {}".format(self.name)
        elif c == 2:
            return "That's {}".format(self.name)

    def checkDirection(self, direction):
        if direction == 'N' and self.n_to is not None:
            return self.n_to
        elif direction == 'S' and self.s_to is not None:
            return self.s_to
        elif direction == 'E' and self.e_to is not None:
            return self.e_to
        elif direction == 'W' and self.w_to is not None:
            return self.w_to
        elif direction == 'U' and self.u_to is not None:
            return self.u_to
        elif direction == 'D' and self.d_to is not None:
            return self.d_to
        else:
            return self

    def setDirection(self, direction, room):
        if direction == 'N' and self.n_to is None and room.s_to is None:
            self.n_to = room
            room.s_to = self
        elif direction == 'S' and self.s_to is None and room.n_to is None:
            self.s_to = room
            room.n_to = self
        elif direction == 'E' and self.e_to is None and room.w_to is None:
            self.e_to = room
            room.w_to = self
        elif direction == 'W' and self.w_to is None and room.e_to is None:
            self.w_to = room
            room.e_to = self
        elif direction == 'U' and self.u_to is None and room.d_to is None:
            self.u_to = room
            room.d_to = self
        elif direction == 'D' and self.d_to is None and room.u_to is None:
            self.d_to = room
            room.u_to = self
