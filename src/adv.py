import textwrap
from setup import data, synonyms, store_data
from player import Player
import pcolors as p


class Adventure:
    def __init__(self, player, data):
        self.player = player
        self.data = data


    def mainLoop(self):
        self.show_room()
        self.get_input()


    def show_room(self):
        current_room = self.player.current_room
        if current_room.isLit(self.player):
            p.prGreen('\n{}\n'.format(current_room.name))
            if current_room.first_visit:
                print(textwrap.fill(current_room.description))
                current_room.first_visit = False
            if len(current_room.contents) > 0:
                p.prYellow('You see here:')
                for item in current_room.contents:
                    print(item.long_name)
        else:
            p.prGrey('\nIt is dark here.\n')


    def rm_extra_words(self, split):
        if len(split) > 1:
            for word in split:
                if word in synonyms['-']:
                    split.remove(word)
        return split


    def get_input(self):
        entry = input('\n\033[96mWhat do you do now?\033[00m ').upper()
        split = self.rm_extra_words(entry.split(' '))
        if entry.upper() in synonyms['Q']:
            store_data(data)
            exit()
        elif entry in synonyms['N']:
            self.player.go('N')
        elif entry in synonyms['S']:
            self.player.go('S')
        elif entry in synonyms['E']:
            self.player.go('E')
        elif entry in synonyms['W']:
            self.player.go('W')
        elif entry in synonyms['U']:
            self.player.go('U')
        elif entry in synonyms['D']:
            self.player.go('D')
        elif entry in synonyms['I']:
            self.player.pack()
        elif split[0] in synonyms['GET']:
            self.player.take(split[-1])
        elif split[0] in synonyms['DROP']:
            self.player.drop(split[-1])
        elif split[0] in synonyms['L']:
            if len(split) > 1 and split[-1] not in synonyms['ROOM']:
                self.player.look(split[-1])
            else:
                self.player.current_room.first_visit = True
        else:
            print('\nI don\'t know what you mean.')


def adventure():
    name = input("What is your name, adventurer? ")
    if name == '':
        name = 'an adventurer'
    player = Player(name, data['rooms']['outside'])
    game = Adventure(player, data)

    while True:
        game.mainLoop()


if __name__ == '__main__':
    adventure()
