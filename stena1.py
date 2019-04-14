import mcpi.minecraft as minecraft

import mcpi.block as block

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

for i in range(10):
    craft.setBlock(cor.x+2, cor.y, cor.z, 35, 14)
    cor.x=cor.x+1
    
cor.x = cor.x - 10

cor.y = cor.y+1


for i in range(10):
    craft.setBlock(cor.x+2, cor.y, cor.z, 35, 14)
    cor.x=cor.x+1
    
cor.x = cor.x - 10

cor.y = cor.y+1


for i in range(10):
    craft.setBlock(cor.x+2, cor.y, cor.z, 35, 14)
    cor.x=cor.x+1

cor.x = cor.x - 10

cor.y = cor.y+1


for i in range(10):
    craft.setBlock(cor.x+2, cor.y, cor.z, 35, 14)
    cor.x=cor.x+1

cor.x = cor.x - 10

cor.y = cor.y+1


for i in range(10):
    craft.setBlock(cor.x+2, cor.y, cor.z, 35, 14)
    cor.x=cor.x+1
