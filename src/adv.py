import textwrap
from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
synonyms = {
    'Q': ['Q','QUIT'],
    'N': ['N','NORTH','GO N','GO NORTH'],
    'S': ['S','SOUTH','GO S','GO SOUTH'],
    'E': ['E','EAST','GO E','GO EAST'],
    'W': ['W','WEST','GO W','GO WEST'],
    'U': ['U','UP','GO U','GO UP','CLIMB','CLIMB UP']
    'D': ['D','DOWN','GO D','GO DOWN','CLIMB DOWN'],
    'L': ['L','LOOK','EXAMINE'],
    'GET': ['GET','TAKE','PICK UP','PICK']
}

def checkDirection(direction, room):
    if direction == 'N' and room.n_to is not None:
        return room.n_to
    elif direction == 'S' and room.s_to is not None:
        return room.s_to
    elif direction == 'E' and room.e_to is not None:
        return room.e_to
    elif direction == 'W' and room.w_to is not None:
        return room.w_to
    else:
        return room


def go(direction,player):
    newRoom = checkDirection(direction, player.currentRoom)
    if newRoom is player.currentRoom:
        print('You can\'t go that way.')
    else:
        player.currentRoom = newRoom


def adventure():
    name = input("What is your name, adventurer? ")
    if name == '':
        name = 'adventurer'
    player = Player(name, room['outside'])

    # Make a new player object that is currently in the 'outside' room.
    loop = True
    while loop:
        currentRoom = player.currentRoom
        print('\n{}\n'.format(currentRoom.name))
        if currentRoom.firstVisit:
            print(textwrap.fill(currentRoom.description))
            currentRoom.firstVisit = False
        entry = input('\nWhat do you do now? ')
        if entry.upper() in synonyms['Q']:
            exit()
        elif entry.upper() in synonyms['N']:
            go('N',player)
        elif entry.upper() in synonyms['S']:
            go('S',player)
        elif entry.upper() in synonyms['E']:
            go('E',player)
        elif entry.upper() in synonyms['W']:
            go('W',player)
        elif entry.split(' ')[0].upper() in synonyms['GET']:
            print('Get {}'.format(entry.split(' ')[-1]))


if __name__ == '__main__':
    adventure()
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
