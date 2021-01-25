import pcolors as p

class SitBetween:
    def __init__(self, datamanager=None,rooms=None,reporter=None):
        self.datamanager = datamanager
        self.rooms = rooms
        self.reporter = reporter

    def set_datamanager(self, datamanager):
        self.datamanager = datamanager
        self.rooms = datamanager.data['rooms']

    def set_reporter(self, reporter):
        self.reporter = reporter

crystal_counter = 0
sb = SitBetween()


def knife_use(knife, player):
    if player.is_player():
        sb.reporter.buffer('You use the knife.',player.current_room)
    else:
        sb.reporter.buffer('{} waves the knife around.'.format(player.name),player.current_room)

def lantern_use(lantern, player):
    if player.is_player():
        sb.reporter.buffer('Ouch! You burn yourself on the lantern!',player.current_room)
        lantern.turn_off()
        sb.reporter.buffer("You can't turn it on! What are you going to do, {}?".format(player.name),player.current_room)
    else:
        sb.reporter.buffer("{} uses the lantern.".format(player.name),player.current_room)

def crystal_take(crystal, player):
    if player.is_player():
        sb.reporter.buffer(p.sLightPurple("You feel warm inside."),player.current_room)
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
