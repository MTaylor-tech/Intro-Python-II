import random
import textwrap
import pcolors as p
from vars import synonyms
from item import LightSource

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        c = random.randint(1,2)
        if c == 1:
            return "It is you."
        elif c == 2:
            return "That's {}".format(self.name)
        elif c == 3:
            return "I'm not sure, but it might be {}.".format(self.name)

    def is_player(self):
        return True

    def go(self, direction):
        new_room = self.current_room.check_direction(direction)
        if new_room is self.current_room:
            p.prRed('You can\'t go that way.')
        else:
            self.current_room.characters.remove(self)
            self.current_room = new_room
            new_room.characters.append(self)

    def take(self, item_name):
        if item_name in synonyms['ALL']:
            item_list = []
            for item in self.current_room.contents:
                self.inventory.append(item)
                item_list.append(item)
                p.prRed("\nTaken.")
                item.on_take(self)
            for item in item_list:
                self.current_room.contents.remove(item)
        else:
            item = self.current_room.has_item(item_name)
            if item is not None:
                self.inventory.append(item)
                self.current_room.contents.remove(item)
                p.prRed("\nTaken.")
                item.on_take(self)
            else:
                p.prRed("\nI don't see that here.")

    def drop(self, item_name):
        if item_name in synonyms['ALL']:
            item_list = []
            for item in self.inventory:
                item_list.append(item)
                self.current_room.contents.append(item)
                p.prRed("\nDropped.")
                item.on_drop(self)
            for item in item_list:
                self.inventory.remove(item)
        else:
            item = self.has_item(item_name)
            if item is not None:
                self.inventory.remove(item)
                self.current_room.contents.append(item)
                p.prRed("\nDropped.")
                item.on_drop(self)
            else:
                p.prRed("\nYou don't have that.")

    def look(self, item_name):
        if self.current_room.is_lit(self):
            found_item = None
            if item_name in synonyms['SELF']:
                print('\n{}\n'.format(self.__str__()))
                return
            found_item = self.has_item(item_name)
            item_in_room = self.current_room.has_ifc(item_name)
            if item_in_room is not None:
                found_item = item_in_room
            if found_item is not None:
                print('\n{}\n'.format(found_item.long_name))
                print(textwrap.fill(found_item.description))
            else:
                p.prRed("\nI don't see that here.")
        else:
            p.prGrey('\nIt is too dark to see here.\n')

    def has_item(self, item_name):
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.name.upper() == item_name:
                    return item
        return None

    def has_light(self):
        for item in self.inventory:
            if isinstance(item, LightSource):
                if item.on:
                    return True
        return False

    def pack(self):
        if len(self.inventory) > 0:
            p.prYellow('\nYour pack contains:')
            for item in self.inventory:
                print(item.long_name)
        else:
            p.prRed('\nYour pack is empty.')

    def use(self, item_name):
        item = self.has_item(item_name)
        if item is not None:
            item.use(self)
        else:
            p.prRed('\nYou don\'t have that item.')

    def say(self, phrase):
        if len(phrase) > 1:
            phrase.remove(phrase[0])
            phrase = ' '.join(phrase)
            print('\nYou say, \"{}\"'.format(phrase))
        else:
            print('\nWhat would you like to say?')


class NonPlayerCharacter(Player):
    def __init__(self, name, long_name, description, current_room, inventory=[],sayings=[],poses=[],actions=[],mobile=0,fence=0,talkative=0):
        super().__init__(name, current_room, inventory)
        self.description = description
        self.long_name = long_name
        self.sayings = sayings
        self.poses = poses
        self.actions = actions
        self.mobile = mobile
        self.fence = fence
        self.path_home = []
        self.reporter = None
        self.talkative = talkative

    def is_player(self):
        return False

    def say(self, phrase):
        self.reporter.buffer('\n{} says, \"{}\"'.format(self.long_name,phrase),self.current_room)

    def go(self, direction):
        new_room = self.current_room.check_direction(direction)
        if new_room is not self.current_room:
            move = False
            if len(self.path_home) > 0:
                if direction == self.path_home[-1]:
                    move = True
                    self.path_home.pop()
                elif len(self.path_home) <= self.fence:
                    move = True
                    self.path_home.append(direction)
            elif len(self.path_home) <= self.fence:
                move = True
                self.path_home.append(direction)
            if move:
                self.reporter.buffer("{} goes {}.".format(self.name,synonyms[direction][1].lower()),self.current_room)
                self.current_room.characters.remove(self)
                self.current_room = new_room
                new_room.characters.append(self)

    def force(self,spRaw):
        spRaw.remove(spRaw[0])
        spRaw.remove(spRaw[0])
        command = spRaw[0].upper()
        if command in synonyms['SAY']:
            self.say(spRaw)
        elif command in synonyms['GO']:
            self.go(spRaw[1].upper())
        elif command in synonyms['GET']:
            self.take(spRaw[1].upper())
        elif command in synonyms['DROP']:
            self.drop(spRaw[1].upper())
        elif command in synonyms['USE']:
            self.use(spRaw[1].upper())
        else:
            print("I don't know what you mean by \"{}\"".format(' '.join(spRaw)))


class NPCAction:
    def __init__(self,chance,action,target):
        self.chance = chance
        self.action = action
        self.target = target

    def activate(self,character):
        print('{} {}s {}'.format(character.name,self.action,self.target))
