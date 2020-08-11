from room import Room
from item import Item

items = {
    'knife': Item("knife","a rusty knife","""It's an old rusty knife. You don't
                  think it would cut very well.""")
}

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['knife']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'cliffside': Room("On the Side of the Cliff", """You've found an old,
                      fraying rope to climb the cliff. The winds buffet you and
                      make the climb difficult."""),

    'bottom': Room("Bottom of the Canyon", """Here at the bottom of the canyon,
                   everything is peaceful. A stream runs nearby. You might be
                   able to follow it the West. The cliff on the opposite side
                   looks unclimbable. There is an old, fraying rope here,
                   leading up."""),

    'streambed': Room("Along the Stream", """Following the stream is a bit
                      tricky, with all the rocks here. The path leads East
                      and West."""),

    'beach': Room("Beach", """A small beach at the side of the stream.""")
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

rooms['overlook'].setDirection('D',rooms['cliffside'])
rooms['cliffside'].setDirection('D',rooms['bottom'])
rooms['bottom'].setDirection('W',rooms['streambed'])
rooms['streambed'].setDirection('W',rooms['beach'])

synonyms = {
    'Q': ['Q','QUIT'],
    'N': ['N','NORTH','GO N','GO NORTH'],
    'S': ['S','SOUTH','GO S','GO SOUTH'],
    'E': ['E','EAST','GO E','GO EAST'],
    'W': ['W','WEST','GO W','GO WEST'],
    'U': ['U','UP','GO U','GO UP','CLIMB','CLIMB UP'],
    'D': ['D','DOWN','GO D','GO DOWN','CLIMB DOWN'],
    'L': ['L','LOOK','EXAMINE'],
    'GET': ['GET','TAKE','PICK UP','PICK'],
    'DROP': ['DROP','REMOVE','PUT DOWN','LEAVE']
}
