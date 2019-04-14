import mcpi.minecraft as minecraft

import mcpi.block as block
import random
import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

d=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

while True:
    k=random.randint(0, 15)
    craft.setBlock(cor.x+2, cor.y, cor.z, 35, d[k])
    time.sleep(0.1)
    k=random.randint(0, 15)
    
    craft.setBlocks(cor.x+2, cor.y, cor.z+5, cor.x+2, cor.y+k, cor.z+5, 35, d[k])
    craft.setBlocks(cor.x+2, cor.y+k, cor.z+5, cor.x+2, cor.y+14, cor.z+5, 0)
    time.sleep(0.1)
    
    k=random.randint(0, 15)
    craft.setBlock(cor.x+2, cor.y, cor.z+2, 35, d[k])
    craft.setBlocks(cor.x+2, cor.y, cor.z+4, cor.x+2, cor.y+k, cor.z+4, 35, d[k])
    craft.setBlocks(cor.x+2, cor.y+k, cor.z+4, cor.x+2, cor.y+14, cor.z+4, 0)
    time.sleep(0.1)
    k=random.randint(0, 15)
    craft.setBlock(cor.x+2, cor.y, cor.z+2, 35, d[k])
    craft.setBlocks(cor.x+2, cor.y, cor.z+3, cor.x+2, cor.y+k, cor.z+3, 35, d[k])
    craft.setBlocks(cor.x+2, cor.y+k, cor.z+3, cor.x+2, cor.y+14, cor.z+3, 0)
    time.sleep(0.1)
