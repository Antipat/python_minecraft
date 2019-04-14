import mcpi.minecraft as minecraft

import mcpi.block as block

import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()
x=cor.x+1
y=cor.y
z=cor.z
def avto1():
    
    craft.setBlocks(x, y, z, x+1, y+2, z+4, 5)
    craft.setBlocks(x, y+1, z, x+1, y+2, z, 0)
    craft.setBlocks(x, y+1, z+2, x+1, y+1, z+2, 0)
    craft.setBlocks(x, y+1, z+4, x+1, y+2, z+4, 0)
def avto2():
    
    craft.setBlocks(x, y, z, x+4, y+2, z+1, 5)
    craft.setBlocks(x, y+1, z, x, y+2, z+1, 0)
    craft.setBlocks(x+2, y+1, z, x+2, y+1, z+1, 0)
    craft.setBlocks(x+4, y+1, z, x+4, y+2, z+1, 0)

for i in range(10):
    avto1()
    z=z+5
    time.sleep(1)
    craft.setBlocks(x, y, z-5, x+1, y+2, z, 0)
for i in range(10):
    avto2()
    x=x+5
    time.sleep(1)
    craft.setBlocks(x-5, y, z, x, y+2, z+1, 0)
for i in range(10):
    avto1()
    z=z-5
    time.sleep(1)
    craft.setBlocks(x, y, z, x+1, y+2, z+10, 0)
for i in range(10):
    avto2()
    x=x-5
    time.sleep(1)
    craft.setBlocks(x, y, z, x+10, y+2, z+1, 0)
