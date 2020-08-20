from player import NonPlayerCharacter
import random as r
from vars import directions
import pcolors as p

class NPCController:
    def __init__(self,datamanager):
        self.datamanager = datamanager
        self.counter = 0

    def step(self):
        npcs = self.datamanager.data.get('npcs')
        self.counter += 1
        if npcs is not None:
            for tag in npcs:
                npc = npcs.get(tag)
                if npc is not None:
                    self.move_random(npc)
                    self.say_random(npc)

    def move_random(self,npc):
        if npc.mobile > 0:
            rand = r.randint(1,10)
            if rand <= npc.mobile:
                exits = npc.current_room.visible_exits
                rand = r.randint(1,len(exits))
                npc.go(exits[rand-1])
                p.prOrange(">>>{}->{}<<<".format(npc.name,exits[rand-1]))

    def say_random(self,npc):
        if npc.talkative > 0:
            rand = r.randint(1,10)
            if rand <= npc.talkative:
                rand = r.randint(1,len(npc.sayings))
                npc.say(npc.sayings[rand-1])
