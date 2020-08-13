import textwrap
import os.path as path
from datamanager import DataManager
from vars import synonyms, opposites, directions
import pcolors as p


class Adventure:
    def __init__(self, data_manager):
        self.player = data_manager.data['player']
        self.data = data_manager.data
        self.data_manager = data_manager

    def mainLoop(self):
        self.show_room()
        self.get_input()

    def show_room(self):
        current_room = self.player.current_room
        if current_room.is_lit(self.player):
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
        entry = p.inNiceBlue('\nWhat do you do now? ').upper()
        split = self.rm_extra_words(entry.split(' '))
        if entry == 'SHOW COLORS':
            p.show_colors()
        if entry in synonyms['Q']:
            self.data_manager.store_data()
            exit()
        elif entry in synonyms['I']:
            self.player.pack()
        elif split[0] == '@TEL':
            if self.data.rooms[split[1]] is not None:
                self.player.current_room = self.data.rooms[split[1]]
        elif split[0] in synonyms['GET']:
            self.player.take(split[-1])
        elif split[0] in synonyms['DROP']:
            self.player.drop(split[-1])
        elif split[0] in synonyms['USE']:
            self.player.use(split[-1])
        elif split[0] in synonyms['L']:
            if len(split) > 1 and split[-1] not in synonyms['ROOM']:
                self.player.look(split[-1])
            else:
                self.player.current_room.first_visit = True
        else:
            for direction in directions:
                if entry in synonyms[direction]:
                    self.player.go(direction)
                    return()
            print('\nI don\'t know what you mean.')


def adventure():
    data = {}
    loaded = False
    name = input("What is your name, adventurer? ")
    if name == '':
        name = 'an adventurer'
        print('Welcome, adventurer.')
    else:
        print('Welcome, {}.'.format(name))
    data_manager = DataManager(name)
    if path.exists(data_manager.get_filename()):
        entry = input('I see you have a saved game. Would you like to load it? (Y/n)').upper()
        if entry in synonyms['YES']:
            data_manager.load_data()
            loaded = True
        else:
            data_manager.load_defaults()
    else:
        data_manager.load_defaults()
    if not loaded:
        data_manager.data['player'].name = name
    game = Adventure(data_manager)
    while True:
        game.mainLoop()


if __name__ == '__main__':
    adventure()
