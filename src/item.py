class Item:
    def __init__(self, name, long_name, description, take_text='',
                 drop_text=''):
        self.name = name
        self.long_name = long_name
        self.description = description
        self.take_text = take_text
        self.drop_text = drop_text

    def on_take(self):
        print('You now have {}. {}'.format(self.long_name,self.take_text))

    def on_drop(self):
        print('You have dropped {}. {}'.format(self.long_name,self.drop_text))

class LightSource(Item):
    def __init__(self, name, long_name, description, duration, take_text='',
                 drop_text=''):
        super(self,name,long_name,description,take_text,drop_text)
        self.duration = duration

    def on_drop(self):
        print('It\'s not a good idea to drop your light source. {}'
              .format(self.long_name,self.drop_text))
