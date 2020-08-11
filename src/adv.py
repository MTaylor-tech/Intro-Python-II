import textwrap
from setup import rooms,synonyms,items
from player import Player


def adventure():
    name = input("What is your name, adventurer? ")
    if name == '':
        name = 'adventurer'
    player = Player(name, rooms['outside'])

    # Make a new player object that is currently in the 'outside' room.
    loop = True
    while loop:
        current_room = player.current_room
        print('\n{}\n'.format(current_room.name))
        print(textwrap.fill(current_room.description))
        if len(current_room.contents) > 0:
            print('You see here: ')
            for item in current_room.contents:
                print(item.long_name)
        entry = input('\nWhat do you do now? ')
        if entry.upper() in synonyms['Q']:
            exit()
        elif entry.upper() in synonyms['N']:
            player.go('N')
        elif entry.upper() in synonyms['S']:
            player.go('S')
        elif entry.upper() in synonyms['E']:
            player.go('E')
        elif entry.upper() in synonyms['W']:
            player.go('W')
        elif entry.upper() in synonyms['U']:
            player.go('U')
        elif entry.upper() in synonyms['D']:
            player.go('D')
        elif entry.split(' ')[0].upper() in synonyms['GET']:
            print('Get {}'.format(entry.split(' ')[-1]))
        elif entry.split(' ')[0].upper() in synonyms['DROP']:
            print('Drop {}'.format(entry.split(' ')[-1]))


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
