import textwrap
import os.path as path
from datamanager import DataManager, Reporter
from vars import synonyms, opposites, directions
import pcolors as p
from item_functions import sb
from npc_controller import NPCController



class Adventure:
    def __init__(self, data_manager):
        self.player = data_manager.data['player']
        self.data = data_manager.data
        self.data_manager = data_manager
        sb.set_datamanager(data_manager)
        self.npc_controller = NPCController(data_manager)
        self.reporter = Reporter(self.player)
        sb.set_reporter = self.reporter
        for npc in self.data.get('npcs'):
            self.data['npcs'][npc].reporter = self.reporter

    def mainLoop(self):
        self.show_room()
        self.get_input()
        self.npc_controller.step()

    def show_room(self):
        current_room = self.player.current_room
        if current_room.is_lit(self.player):
            p.prGreen('\n{}\n'.format(current_room.name))
            if current_room.first_visit:
                print(textwrap.fill(current_room.description))
                # current_room.first_visit = False
            if len(current_room.contents) > 0:
                p.prYellow('You see here:')
                for item in current_room.contents:
                    print(item.long_name)
            if len(current_room.characters) > 1:
                p.prYellow('Also here:')
                for char in current_room.characters:
                    if char is not self.player:
                        print(char.name)
            if len(current_room.visible_exits) > 0:
                string = ', '.join(current_room.visible_exits)
                p.prYellow('Visible exits: {}'.format(string))

        else:
            p.prGrey('\nIt is dark here.\n')

    def rm_extra_words(self, split):
        if len(split) > 1:
            for word in split:
                if word in synonyms['-']:
                    split.remove(word)
        return split

    def god_commands(self,entry,split,spRaw):
        if split[0] == '@TEL':
            target = self.data['rooms'].get(split[1].lower())
            if target is not None:
                self.player.current_room.characters.remove(self.player)
                self.player.current_room = target
                target.characters.append(self.player)
            else:
                print("That location is unknown to me.")
        elif entry == '@COLORS':
            p.show_colors()
        elif split[0] == '@CLONE':
            target = self.data['items'].get(split[1].lower())
            if target is not None:
                self.player.current_room.add_item(target)
            else:
                print("I can't find that.")
        elif split[0] == '@SUMMON':
            target = self.data['npcs'].get(split[1].lower())
            if target is not None:
                target.current_room.characters.remove(target)
                target.current_room = self.player.current_room
                self.player.current_room.characters.append(target)
                p.prGreen('Summoned {}'.format(target.long_name))
            else:
                print("I don't know who you mean.")
        elif split[0] == '@DESTROY':
            target = self.player.has_item(split[1])
            if target is not None:
                p.prRed('Destroyed {}'.format(target.long_name))
                self.player.inventory.remove(target)
            else:
                target = self.player.current_room.has_item(split[1])
                if target is not None:
                    p.prRed('Destroyed {}'.format(target.long_name))
                    self.player.current_room.contents.remove(target)
                else:
                    print("I can't find that.")
        elif split[0] == '@FORCE':
            target = self.data['npcs'].get(split[1].lower())
            if target is not None:
                target.force(spRaw)
            else:
                print("I don't know who you mean.")

    def get_input(self):
        raw = p.inNiceBlue('\nWhat do you do now? ')
        if raw == '':
            return
        entry = raw.upper()
        split = self.rm_extra_words(entry.split(' '))
        spRaw = raw.split(' ')
        if entry[0] == '@':
            self.god_commands(entry, split, spRaw)
        elif entry in synonyms['Q']:
            self.data_manager.store_data()
            exit()
        elif entry in synonyms['I']:
            self.player.pack()
        elif split[0] in synonyms['GET']:
            self.player.take(split[-1])
        elif split[0] in synonyms['DROP']:
            self.player.drop(split[-1])
        elif split[0] in synonyms['USE']:
            self.player.use(split[-1])
        elif split[0] in synonyms['SAY']:
            self.player.say(spRaw)
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
