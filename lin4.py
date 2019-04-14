import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

for i in range(20):
    y1 = 0*i-2
    craft.setBlock(x+i, y+y1,z, 35,0)
    
for i in range(20):
    y1 = 0*i-1
    craft.setBlock(x+i, y+y1,z, 35,1)

for i in range(20):
    y1 = 0*i+1
    craft.setBlock(x+i, y+y1,z, 35,2)

for i in range(20):
    y1 = 0*i+2
    craft.setBlock(x+i, y+y1,z, 35,3)
    
for i in range(20):
    y1 = 0*i+math.sqrt(12)
    craft.setBlock(x+i, y+y1,z, 35,4)

    
 
