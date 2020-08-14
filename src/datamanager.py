import pickle
import os.path as path
from player import Player
from defaults import Defaults


class DataManager:
    def __init__(self, data={}, name=''):
        self.set_filename(name)
        self.data = data
        self.functions = {}

    def set_filename(self, name):
        self._filename = './data/{}.dat'.format(''.join(name.lower().split(' ')))

    def get_filename(self):
        return self._filename

    def store_data(self):
        pickle.dump(self.data, open(self._filename, "wb"))

    def load_data(self):
        if path.exists(self._filename):
            self.data = pickle.load(open(self._filename, "rb"))

    def load_defaults(self):
        self.data = {}
        defaults = Defaults()
        self.data['player']= defaults.player
        self.data['rooms'] = defaults.rooms
        self.data['items'] = defaults.items
        self.data['npcs'] = defaults.npcs
