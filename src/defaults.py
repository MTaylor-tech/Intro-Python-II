from item import Item, LightSource
from room import Room
from player import Player, NonPlayerCharacter
import pcolors as p
import os.path as path
import csv


class Defaults:
    def __init__(self):
        self.player = Player('', None)
        self.items = {}
        self.rooms = {}
        self.npcs = {}
        self.rooms_to_connect = []
        self.process_csv_file('rooms')
        self.process_csv_file('items')
        self.player.current_room = self.rooms['outside']
        self.rooms['outside'].characters.append(self.player)
        self.connect_rooms()
        self.process_csv_file('npcs')

    def connect_rooms(self):
        for path in self.rooms_to_connect:
            path_split = path.split('.')
            origin = self.rooms.get(path_split[0].lower())
            direction = path_split[1].upper()
            target = None
            visible = True
            if len(path_split) > 3:
                target = self.rooms.get(path_split[3].lower())
                visible = False
            else:
                target = self.rooms.get(path_split[2].lower())
            if origin is not None and target is not None:
                # print("|{}| goes |{}| to |{}|".format(origin.name,direction,target.name))
                origin.set_direction(direction,target,visible)
            else:
                print('Something is None')

    def process_csv_file(self,name):
        csv_filename = './data/{}.csv'.format(name)
        if path.exists(csv_filename):
            with open(csv_filename, newline='') as csvfile:
                dict_reader = csv.DictReader(csvfile)
                if name == 'items':
                    self.process_items(dict_reader)
                if name == 'rooms':
                    self.process_rooms(dict_reader)
                if name == 'npcs':
                    self.process_npcs(dict_reader)

    def process_items(self,dict_reader):
        for row in dict_reader:
            item_name = row['Name']
            long_name = row['Long Name']
            description = row['Description']
            rooms = row['Rooms'].lower().split(' ')
            item_or_feature = row['ILF']
            is_on = False
            if row['On'] == 'Y':
                is_on = True
            if item_or_feature == 'F':
                item = Item(item_name,long_name,description)
                self.items[item_name.lower()] = item
                for room in rooms:
                    self.rooms[room].add_feature(item)
            elif item_or_feature == 'L':
                item = LightSource(item_name,long_name,description,on=is_on)
                self.items[item_name.lower()] = item
                for room in rooms:
                    self.rooms[room].add_item(item)
            else:
                item = Item(item_name,long_name,description)
                self.items[item_name.lower()] = item
                for room in rooms:
                    self.rooms[room].add_item(item)

    def process_rooms(self,dict_reader):
        for row in dict_reader:
            room_tag = row['Tag'].lower()
            # print('|{}|'.format(room_tag))
            room_name = row['Name']
            description = row['Description']
            description = description.replace('xi[',p.italic)
            description = description.replace('xb[',p.bold)
            description = description.replace(']x',p.clear_style)
            is_lit = False
            if row['Lit'] == 'Y':
                is_lit = True
            # room = Room(room_tag,room_name,description,lit=is_lit,contents=[],features=[])
            room = Room(room_tag,room_name,description,lit=is_lit)
            self.rooms[room_tag] = room
            paths = row['Paths'].split(' ')
            if paths[0] != '':
                for path in paths:
                    self.rooms_to_connect.append('{}.{}'.format(room_tag,path))

    def process_npcs(self,dict_reader):
        for row in dict_reader:
            tag = row['Tag'].lower()
            npc_name = row['Name']
            long_name = row['Long Name']
            description = row['Description']
            description = description.replace('xi[',p.italic)
            description = description.replace('xb[',p.bold)
            description = description.replace(']x',p.clear_style)
            room_tag = row['Starting Room']
            room = self.rooms.get(room_tag)
            inventory = row['Inventory']
            mobile = int(row['Mobile'])
            fence = int(row['Fence'])
            sayings = row['Sayings'].split('|')
            talkative = int(row['Talkative'])
            poses = row['Poses'].split('|')
            char = NonPlayerCharacter(name=npc_name,long_name=long_name,description=description,current_room=room,inventory=[],mobile=mobile,fence=fence,sayings=sayings,poses=poses,talkative=talkative)
            if len(inventory) > 0:
                inventory = inventory.split(' ')
                for item_name in inventory:
                    item = self.items.get(item_name)
                    if item is not None:
                        char.inventory.append(item)
            if room is not None:
                room.characters.append(char)
            self.npcs[tag] = char
