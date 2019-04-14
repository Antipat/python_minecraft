import mcpi.minecraft as minecraft
import time

craft=minecraft.Minecraft.create()

x1 = -458
x2 = -451
z1 = -550
z2 = -537

t = 0

while True:
    time.sleep(1)
    cor=craft.player.getTilePos()
    if t ==10:
        craft.player.setTilePos (-453, 69, -550)
        t=0
        
    if cor.x >=x1 and cor.x<=x2 and cor.z>=z1 and cor.z<=z2:
        craft.postToChat("Игра началась t =" +str(t))
        t = t + 1
        
    else:
        craft.postToChat("Конец игры t = "+ str(t))
        t = 0






