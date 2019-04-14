import mcpi.minecraft as minecraft

import mcpi.block as block

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

for j in range (5):
    for i in range(10):
        craft.setBlock(cor.x+2+i, cor.y, cor.z, 35, 14)
    
    cor.y = cor.y+1

cor.y = cor.y - 5

for j in range (5):
    for i in range(10):
        craft.setBlock(cor.x+2, cor.y, cor.z+i, 35, 14)
    
    cor.y = cor.y+1
    
cor.y = cor.y - 5

for j in range (5):
    for i in range(10):
        craft.setBlock(cor.x+2+i, cor.y, cor.z+10, 35, 14)
    
    cor.y = cor.y+1

cor.y = cor.y - 5

for j in range (5):
    for i in range(10):
        craft.setBlock(cor.x+12, cor.y, cor.z+i, 35, 14)
    
    cor.y = cor.y+1

cor.y = cor.y - 5
for j in range (10):
    for i in range(10):
        craft.setBlock(cor.x+2, cor.y, cor.z+i, 17)
    
    cor.x = cor.x+1

cor.y = cor.y+5

for j in range (8):
    for i in range(10):
        craft.setBlock(cor.x+2, cor.y, cor.z+i, block.GLASS.id)
    
    cor.x = cor.x-1


    
