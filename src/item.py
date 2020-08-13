class Item:
    def __init__(self, name, long_name, description, taken=None,
                 dropped=None, used=None):
        self.name = name
        self.long_name = long_name
        self.description = description
        self.taken = taken
        self.dropped = dropped
        self.used = used

    def use(self):
        print('You use {}.'.format(self.long_name))
        if self.used is not None:
            self.used()

    def on_take(self):
        print('You now have {}.'.format(self.long_name))
        if self.taken is not None:
            self.taken()

    def on_drop(self):
        print('You have dropped {}.'.format(self.long_name))
        if self.dropped is not None:
            self.dropped()


class LightSource(Item):
    def __init__(self, name, long_name, description, on=False, taken=None,
                 dropped=None, used=None):
        super().__init__(name,long_name,description,taken,dropped,used)
        self.on = on

    def use(self):
        if self.on:
            self.turn_off()
            print('You turn off {}.'.format(self.long_name))
        else:
            self.turn_on()
            print('You turn on {}.'.format(self.long_name))
        if self.used is not None:
            self.used()

    def turn_off(self):
        self.on = False

    def turn_on(self):
        self.on = True

    def on_drop(self):
        print('It\'s not a good idea to drop your light source.')
        if self.dropped is not None:
            self.dropped()
