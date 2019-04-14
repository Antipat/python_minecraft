import mcpi.minecraft as minecraft

import mcpi.block as block

import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()


for i in range(10):
    craft.setBlock(cor.x+i, cor.y, cor.z, 0)
    craft.setBlock(cor.x+1+i, cor.y, cor.z, 57)
    time.sleep(0.5)
    
    
for i in range(10):
    
    craft.setBlock(cor.x+1+i, cor.y, cor.z, 57)
    time.sleep(0.5)
    craft.setBlock(cor.x+i+1, cor.y, cor.z, 0)

    
