from item_functions import functions

class Item:
    def __init__(self, name, long_name, description):
        self.name = name
        self.long_name = long_name
        self.description = description

    def use(self, player):
        print('You use {}.'.format(self.long_name))
        fn = functions.get('{}_use'.format(self.name.lower()))
        if fn is not None:
            fn(self, player)

    def on_take(self, player):
        print('You now have {}.'.format(self.long_name))
        fn = functions.get('{}_take'.format(self.name.lower()))
        if fn is not None:
            fn(self, player)

    def on_drop(self, player):
        print('You have dropped {}.'.format(self.long_name))
        fn = functions.get('{}_drop'.format(self.name.lower()))
        if fn is not None:
            fn(self, player)


class LightSource(Item):
    def __init__(self, name, long_name, description, on=False):
        super().__init__(name,long_name,description)
        self.on = on

    def use(self, player):
        if self.on:
            self.turn_off()
            print('You turn off {}.'.format(self.long_name))
        else:
            self.turn_on()
            print('You turn on {}.'.format(self.long_name))
        super().use(player)

    def turn_off(self):
        self.on = False

    def turn_on(self):
        self.on = True

    def on_take(self,player):
        super().on_take(player)

    def on_drop(self, player):
        print('It\'s not a good idea to drop your light source.')
        super().on_drop(player)
