import pcolors as p

class SitBetween:
    def __init__(self, datamanager=None,rooms=None):
        self.datamanager = datamanager
        self.rooms = rooms

    def set_datamanager(self, datamanager):
        self.datamanager = datamanager
        self.rooms = datamanager.data['rooms']

crystal_counter = 0
sb = SitBetween()


def knife_use(knife, player):
    print('This is the knife being used. Chop chop.')
    if player.current_room.tag == 'outside':
        print("OoOoOoOoO!")

def lantern_use(lantern, player):
    print('Ouch! You burn yourself on the lantern!')
    lantern.turn_off()
    print("You can't turn it on! What are you going to do, {}?".format(player.name))

def crystal_take(crystal, player):
    p.prLightPurple("You feel warm inside.")
    global crystal_counter
    if crystal_counter >= 3:
        crystal_counter = 0

def crystal_drop(crystal, player):
    p.prLightPurple("You are so reluctant to part with it.")
    global crystal_counter
    if crystal_counter < 3:
        player.take('CRYSTAL')
        crystal_counter += 1

def key_use(key, player):
    if player.current_room.tag == 'narrow':
        target = sb.rooms.get('treasure')
        if target is not None:
            player.current_room.set_direction('N',target)
    else:
        p.prRed("You can't use that here.")

functions = {
    'knife_use': knife_use,
    'lantern_use': lantern_use,
    'crystal_take': crystal_take,
    'crystal_drop': crystal_drop,
    'key_use': key_use
}
