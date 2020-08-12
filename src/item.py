class Item:
    def __init__(self, name, long_name, description, take_text='',
                 drop_text='', use_text=''):
        self.name = name
        self.long_name = long_name
        self.description = description
        self.take_text = take_text
        self.drop_text = drop_text

    def use(self):
        print('You use {}. {}'.format(self.long_name,self.use_text))

    def on_take(self):
        print('You now have {}. {}'.format(self.long_name,self.take_text))

    def on_drop(self):
        print('You have dropped {}. {}'.format(self.long_name,self.drop_text))


class LightSource(Item):
    def __init__(self, name, long_name, description, on=False, take_text='',
                 drop_text='', use_text=''):
        super().__init__(name,long_name,description,take_text,drop_text,use_text)
        self.on = on

    def use(self):
        if self.on:
            self.turn_off()
            print('You turn off {}. {}'.format(self.long_name,self.use_text))
        else:
            self.turn_on()
            print('You turn on {}. {}'.format(self.long_name,self.use_text))

    def turn_off(self):
        self.on = False

    def turn_on(self):
        self.on = True

    def on_drop(self):
        print('It\'s not a good idea to drop your light source. {}'
              .format(self.long_name,self.drop_text))
