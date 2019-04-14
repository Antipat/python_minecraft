import mcpi.minecraft as minecraft

import mcpi.block as block

import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

craft.setBlock(cor.x+8, cor.y-1, cor.z, 41)

for i in range(10):
    craft.setBlock(cor.x+i, cor.y, cor.z, 0)
    craft.setBlock(cor.x+1+i, cor.y, cor.z, 57)
    time.sleep(1)
    if craft.getBlock(cor.x+1+i, cor.y-1, cor.z)==41:
        craft.postToChat("Золотой блок ")
    else:
        craft.postToChat("Ищем блок ")


    
