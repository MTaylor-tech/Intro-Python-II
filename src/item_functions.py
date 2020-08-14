crystal_counter = 0

def knife_use(knife, player):
    print('This is the knife being used. Chop chop.')
    if player.current_room.name == 'Outside Cave Entrance':
        print("OoOoOoOoO!")

def lantern_use(lantern, player):
    print('Ouch! You burn yourself on the lantern!')
    lantern.turn_off()
    print("You can't turn it on! What are you going to do, {}?".format(player.name))

def crystal_take(crystal, player):
    print("You feel warm inside.")
    global crystal_counter
    if crystal_counter >= 3:
        crystal_counter = 0

def crystal_drop(crystal, player):
    print("You are so reluctant to part with it.")
    global crystal_counter
    if crystal_counter < 3:
        player.take('CRYSTAL')
        crystal_counter += 1

functions = {
    'knife_use': knife_use,
    'lantern_use': lantern_use,
    'crystal_take': crystal_take,
    'crystal_drop': crystal_drop
}
