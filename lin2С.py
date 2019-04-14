import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

for i in range(5):
    y1=0*i+0
    craft.setBlock(x+i,y+y1,z, 35,0)
    y1 = 0*i+5
    craft.setBlock(x+i,y+y1,z, 35,1)
    x1=i*0+0
    craft.setBlock(x+x1,y+i,z, 35,2)
    x1=i*0+5
    craft.setBlock(x+x1,y+i,z, 35,3)
    x1=i*0+0
    craft.setBlock(x+x1,y,z+i, 35,4)
    x1=i*0+5
    craft.setBlock(x+x1,y,z+i, 35,5)

    y1=0*i+0
    craft.setBlock(x+i,y+y1,z+5, 35,6)
    y1 = 0*i+5
    craft.setBlock(x+i,y+y1,z+5, 35,7)
    x1=i*0+0
    craft.setBlock(x+x1,y+i,z+5, 35, 8)
    x1=i*0+5
    craft.setBlock(x+x1,y+i,z+5, 35,9)
    x1=i*0+0
    craft.setBlock(x+x1,y+5,z+i, 35,10)
    x1=i*0+5
    craft.setBlock(x+x1,y+5,z+i, 35,11)



    
