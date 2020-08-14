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
        self.rooms_to_connect = []
        self.process_csv_file('rooms')
        self.process_csv_file('items')
        self.player.current_room = self.rooms['outside']
        self.connect_rooms()
        npc = NonPlayerCharacter('a man','Lord Alfred','A tall slender man.',self.rooms['outside'])
        self.rooms['outside'].characters.extend([self.player,npc])

    def connect_rooms(self):
        for path in self.rooms_to_connect:
            path_split = path.split('.')
            origin = self.rooms.get(path_split[0].lower())
            direction = path_split[1].upper()
            target = self.rooms.get(path_split[2].lower())
            if origin is not None and target is not None:
                # print("|{}| goes |{}| to |{}|".format(origin.name,direction,target.name))
                origin.set_direction(direction,target)
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
