import mcpi.minecraft as minecraft

import mcpi.block as block
import random
import time

craft = minecraft.Minecraft.create()


cor = craft.player.getTilePos()
x=cor.x+1
y=cor.y
z=cor.z
craft.setBlocks(x-2, y,z, x+5, y, z+10, 5)
craft.setBlocks(x+5, y+1,z, x+7, y+1, z+10, 5)
craft.setBlocks(x+10, y+1,z, x+15, y+1, z+8, 5)
craft.setBlocks(x+15, y+2,z+3, x+25, y+2, z+5, 5)
craft.setBlocks(x+25, y+2,z+3, x+25, y+2, z+20, 5)
craft.setBlocks(x+25, y+3,z+20, x+35, y+3, z+20, 5)

for i in range (20):
    craft.setBlocks(x+35, y+3+i,z+20+i, x+35, y+3+i, z+25+i, 5)
    craft.setBlocks(x+35, y+3+i,z+23+i, x+35, y+3+i, z+24+i, 0)
    z=z+3
    
for i in range (20):
    craft.setBlocks(x+35+i, y+23+i,z+44, x+36+i, y+23+i, z+44, 5)
    
craft.setBlocks(x+55, y+43,z+44, x+61, y+43, z+50, 5)
craft.setBlocks(x+58, y+44,z+47, x+59, y+44, z+48, 41)
while True:
    cor = craft.player.getTilePos()
    if craft.getBlock(cor.x, cor.y-1, cor.z)==41:
        x=cor.x-58
        y = cor.y-44
        z= cor.z - 48
        craft.player.setTilePos(cor.x-58, cor.y-44, cor.z - 48)
        craft.postToChat("Вы перешли на третий уровень ")
        craft.setBlocks(x-40, y,z-65, x+60, y+50, z+65, 0)
        break
    




    

