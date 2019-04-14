import mcpi.minecraft as minecraft
import time

import random

craft=minecraft.Minecraft.create()

x1 = -458
x2 = -451
z1 = -550
z2 = -537

t = 0


while True:
    time.sleep(1)
    cor=craft.player.getTilePos()
    xr = random.randint(x1, x2)
    zr = random.randint (z1, z2)
    
    if t ==3:
        craft.player.setTilePos (xr, 69, zr)
        t=0
        
    if cor.x >=x1 and cor.x<=x2 and cor.z>=z1 and cor.z<=z2:
        craft.postToChat("Игра началась t =" +str(t))
        t = t + 1
        
    else:
        craft.postToChat("Конец игры t = "+ str(t))
        t = 0






