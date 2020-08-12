import pickle
import os.path as path
from player import Player
import defaults


class DataManager:
    def __init__(self, name=''):
        self.set_filename(name)

    def set_filename(self, name):
        self.filename = './data/{}.dat'.format(''.join(name.lower().split(' ')))

    def store_data(self, data):
        pickle.dump(data, open(self.filename, "wb"))

    def load_data(self):
        if path.exists(self.filename):
            return pickle.load(open(self.filename, "rb"))

    def load_defaults(self):
        data = {}
        player = Player('',None)
        items = defaults.items
        rooms = defaults.rooms
        rooms['narrow'].lit = False
        rooms['outside'].set_direction('N',rooms['foyer'])
        rooms['foyer'].set_direction('N',rooms['overlook'])
        rooms['foyer'].set_direction('E',rooms['narrow'])
        rooms['narrow'].set_direction('N',rooms['treasure'])
        rooms['overlook'].set_direction('D',rooms['cliffside'])
        rooms['cliffside'].set_direction('D',rooms['bottom'])
        rooms['bottom'].set_direction('W',rooms['streambed'])
        rooms['streambed'].set_direction('W',rooms['beach'])
        rooms['treasure'].set_direction('SW',rooms['foyer'])
        player.current_room = rooms['outside']
        #global data
        data['player']= player
        data['rooms'] = rooms
        data['items'] = items
        return data
