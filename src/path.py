class Path:
    def __init__(self, direction, to_room, description='', use_text='',
                 passable=True, locked=False, key=None):
        self.direction = direction
        self.to_room = to_room
        self.description = description
        self.use_text = use_text
        self.passable = passable
        self.locked = locked
        self.key = key
