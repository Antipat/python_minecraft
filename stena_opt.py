import mcpi.minecraft as minecraft

import mcpi.block as block

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

for j in range (5):
    for i in range(10):
        craft.setBlock(cor.x+2+i, cor.y, cor.z, 35, 14)
    
    cor.y = cor.y+1


