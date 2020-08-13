from item import Item, LightSource
from room import Room
from player import Player

items = {
    'knife': Item("knife","a rusty knife","""It's an old rusty knife. You don't think it would cut very well."""),
    'rope': Item("rope","some old rope","""It looks like someone used this a very long time ago. It is worn and fraying.""","A lot of good it'll do ya.",
"About time you got rid of that."),
    'flashlight': LightSource("flashlight","a flashlight","""It's a flashlight.""",True)
}

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons",
                     [items['flashlight']]),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""",
                     [items['knife']]),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
                     [items['rope']]),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
    'cliffside': Room("On the Side of the Cliff", """You've found an old, fraying rope to climb the cliff. The winds buffet you and make the climb difficult."""),
    'bottom': Room("Bottom of the Canyon", """Here at the bottom of the canyon, everything is peaceful. A stream runs nearby. You might be able to follow it west. The cliff on the opposite side looks unclimbable. There is an old, fraying rope here, leading up."""),
    'streambed': Room("Along the Stream", """Following the stream is a bit tricky, with all the rocks here. The path leads east and west."""),
    'beach': Room("Beach", """A small beach at the side of the stream. A path follows the stream east.""")
}

class Defaults:
    def __init__(self):
        self.player = Player('', None)
        self.items = items
        self.rooms = rooms
        self.run_rooms()
        self.player.current_room = self.rooms['outside']

    def run_rooms(self):
        self.rooms['narrow'].lit = False
        self.rooms['outside'].set_direction('N',rooms['foyer'])
        self.rooms['foyer'].set_direction('N',rooms['overlook'])
        self.rooms['foyer'].set_direction('E',rooms['narrow'])
        self.rooms['narrow'].set_direction('N',rooms['treasure'])
        self.rooms['overlook'].set_direction('D',rooms['cliffside'])
        self.rooms['cliffside'].set_direction('D',rooms['bottom'])
        self.rooms['bottom'].set_direction('W',rooms['streambed'])
        self.rooms['streambed'].set_direction('W',rooms['beach'])
        self.rooms['treasure'].set_direction('SW',rooms['foyer'])
