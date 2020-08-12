import textwrap
from setup import rooms,synonyms,items
from player import Player


def adventure():
    name = input("What is your name, adventurer? ")
    if name == '':
        name = 'adventurer'
    player = Player(name, rooms['outside'])

    while True:
        current_room = player.current_room
        print('\n{}\n'.format(current_room.name))
        if current_room.first_visit:
            print(textwrap.fill(current_room.description))
            current_room.first_visit = False
        if len(current_room.contents) > 0:
            print('You see here: ')
            for item in current_room.contents:
                print(item.long_name)
        entry = input('\nWhat do you do now? ').upper()
        split = entry.split(' ')
        if entry.upper() in synonyms['Q']:
            exit()
        elif entry in synonyms['N']:
            player.go('N')
        elif entry in synonyms['S']:
            player.go('S')
        elif entry in synonyms['E']:
            player.go('E')
        elif entry in synonyms['W']:
            player.go('W')
        elif entry in synonyms['U']:
            player.go('U')
        elif entry in synonyms['D']:
            player.go('D')
        elif entry in synonyms['I']:
            player.pack()
        elif split[0] in synonyms['GET']:
            player.take(split[-1])
        elif split[0] in synonyms['DROP']:
            player.drop(split[-1])
        elif split[0] in synonyms['L']:
            if len(split) > 1:
                player.look(split[-1])
            else:
                current_room.first_visit = True
        else:
            print('\nI don\'t know what you mean.')


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
