from item import Item, LightSource
from room import Room
from player import Player
import pcolors as p
import os.path as path
import csv

def knife_use():
    print('This is the knife being used. Chop chop.')

items = {
    'knife': Item("knife","a rusty knife","""It's an old rusty knife. You don't think it would cut very well.""",used=knife_use),
    'rope': Item("rope","an old rope","""It looks like someone used this a very long time ago. It is worn and fraying. It might just hold your weight, but it could give out any moment."""),
    'flashlight': LightSource("flashlight","a flashlight","""It's a flashlight.""",on=False),
    'cave': Item("cave","the mouth of the cave","""Jagged stalactites hang from the roof of the cave, reminding you of some grotesque beast's fangs."""),
    'edge': Item("cliff","the edge of the cliff","""The edge is frightening. The cliff descends many meters. A length of rope dangles down into the depths."""),
    'key': Item("key","a key","It's a simple brass key. I wonder what lock it belongs to.")
}

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     f"The breeze blows through the trees. Birds chirp and squabble in the canopy. North of you, the {p.italic}cave{p.clear_style} mouth beckons. An unpleasant odor emanates from it.",
                     contents=[items['flashlight']],features=[items['cave']]),
    'foyer':    Room("Just Inside the Cave", f"""Dim light filters in from the south. The cave continues north.""",
                     contents=[items['knife']],features=[items['cave']]),
    'overlook': Room("Grand Overlook", f"""A steep {p.italic}cliff{p.clear_style} appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm. An old {p.italic}rope{p.clear_style} is tied to a tree.""",features=[items['edge'],items['rope']]),
    'narrow':   Room("Narrow Passage", f"""The narrow passage bends here from west to north. The smell of gold permeates the air.""",lit=False,contents=[],features=[]),
    'treasure': Room("Treasure Chamber", f"""You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",contents=[],features=[]),
    'cliffside': Room("On the Side of the Cliff", f"""You've found an old, fraying {p.italic}rope{p.clear_style} to climb the cliff. The winds buffet you and make the climb difficult.""",features=[items['rope']],contents=[]),
    'bottom': Room("Bottom of the Canyon", f"""Here at the bottom of the canyon, everything is peaceful. A stream runs nearby. You might be able to follow it west. The cliff on the opposite side looks unclimbable. There is an old, fraying {p.italic}rope{p.clear_style} here, leading up.""",features=[items['rope']],contents=[]),
    'streambed': Room("Along the Stream", f"""Following the stream is a bit tricky, with all the rocks here. The path leads east and west.""",contents=[],features=[]),
    'beach': Room("Beach", f"""A small beach at the side of the stream. A path follows the stream east.""",contents=[],features=[]),
    'second': Room("Further Into the Cave", f"Dark shadows hide all the pits in the floor. You had better stick to the path if you don't want to twist an ankle. The path continues north.",lit=False,contents=[],features=[]),
    'third': Room("In the Cave",f"The path twists and winds between stalagmites. You see openings to the west and south",lit=False,contents=[],features=[]),
    'forth': Room("In the Cave",f"The cave is worn smooth here, as if from the passage of some great beast. The path exits to the northwest and east.",lit=False,contents=[],features=[]),
    'fifth': Room("In the Cave",f"The cave is tight here, and it's tough to move. A gentle purple light comes from the south. Sounds of water trickling come from the north. You can see exits to the north, south, and southeast.",lit=False,contents=[],features=[]),
    'crystal': Room("The Crystal Cavern",f"A gentle purple light envelopes you as hundreds of thousands of crystals in the walls, floor, and ceiling glow violet. A sense of peace settles on you. The only exit is to the north, but why would anyone want to leave this beautiful place.",contents=[],features=[]),
    'sixth': Room("In the Cave",f"The cave is worn smooth here. The sound of trickling water comes from the chamber to the northeast. Another opening leads to the south.",lit=False,contents=[],features=[]),
    'seventh': Room("In the Cave",f"Light and the smell of fresh air filter in from the north. A deep darkness and an unpleasant odor emanate from the cave to the southwest.",contents=[],features=[]),
}


class Defaults:
    def __init__(self):
        self.player = Player('', None)
        self.items = items
        self.rooms = rooms
        self.rooms_to_connect = []
        self.process_csv_file('rooms')
        self.process_csv_file('items')
        self.player.current_room = self.rooms['outside']
        self.connect_rooms()

    def connect_rooms(self):
        self.rooms['outside'].set_direction('N',rooms['foyer'])
        self.rooms['foyer'].set_direction('N',rooms['second'])
        self.rooms['second'].set_direction('N',rooms['third'])
        self.rooms['third'].set_direction('W',rooms['forth'])
        self.rooms['forth'].set_direction('NW',rooms['fifth'])
        self.rooms['fifth'].set_direction('S',rooms['crystal'])
        self.rooms['fifth'].set_direction('N',rooms['sixth'])
        self.rooms['sixth'].set_direction('NE',rooms['seventh'])
        self.rooms['seventh'].set_direction('N',rooms['overlook'])
        self.rooms['second'].set_direction('E',rooms['narrow2'])
        self.rooms['narrow2'].set_direction('N',rooms['narrow3'])
        #self.rooms['second'].set_direction('E',rooms['narrow'])
        self.rooms['narrow'].set_direction('N',rooms['treasure'])
        self.rooms['overlook'].set_direction('D',rooms['cliffside'])
        self.rooms['cliffside'].set_direction('D',rooms['bottom'])
        self.rooms['bottom'].set_direction('W',rooms['streambed'])
        self.rooms['streambed'].set_direction('W',rooms['beach'])
        print(self.rooms_to_connect)

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
                self.rooms[rooms[0]].add_item(item)
            else:
                item = Item(item_name,long_name,description)
                self.items[item_name.lower()] = item
                self.rooms[rooms[0]].add_item(item)

    def process_rooms(self,dict_reader):
        for row in dict_reader:
            room_tag = row['Tag']
            room_name = row['Name']
            description = row['Description']
            is_lit = False
            if row['Lit'] == 'Y':
                is_lit = True
            room = Room(room_name,description,lit=is_lit,contents=[],features=[])
            self.rooms[room_tag] = room
            paths = row['Paths'].split(' ')
            for path in paths:
                self.rooms_to_connect.append('{}.{}'.format(room_tag,path))
