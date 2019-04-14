import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z


for i in range(20):
    y1 = math.tan((math.pi*45)/180)*i+0
    craft.setBlock(x+i, y+y1,z, 35,4)
    
