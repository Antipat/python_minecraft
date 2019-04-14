import mcpi.minecraft as minecraft
import mcpi.block as block


craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

for i in range(20):
    y1 = -0.5*i-10
    craft.setBlock(x+i, y+y1,z, 35,0)
    
for i in range(20):
    y1 = -0.5*i+10
    craft.setBlock(x+i, y+y1,z, 35,1)

for i in range(20):
    y1 = 0.5*i-10
    craft.setBlock(x+i, y+y1,z, 35,2)

for i in range(20):
    y1 = 0.5*i+10
    craft.setBlock(x+i, y+y1,z, 35,3)
    


for i in range(-20,20):
    y1 = 0*i+0
    craft.setBlock(x+i, y+y1,z, 35,7)

for i in range(-20,20):
    x1 = 0*i+0
    craft.setBlock(x+x1, y+i,z, 35,7)

    
 
