import mcpi.minecraft as minecraft

import mcpi.block as block
import random
import time

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()
x=cor.x+1
y=cor.y
z=cor.z

# Создаём ограниченную область из кирпича
craft.setBlocks(x, y,z, x+15, y, z+10, 45)
craft.setBlocks(x+1, y,z+1, x+14, y, z+9, 0)

# Создаём 10 лазуритов в случайном порядке расположения в области
for i in range(10):
    x1=x+random.randint(1, 14)
    z1=z+random.randint(1,9)
    craft.setBlock(x1, y,z1, 22)
    
t =0
l =0
while True:
    cor = craft.player.getTilePos()
    if cor.x >=x and cor.x<=x+15 and cor.z >=z and cor.z<=z+10:
        craft.postToChat("До завершения осталось "+ " t = "+ str(10 - t))
        t=t+0.1
    else:
        t=0
    if t>=15:
        craft.postToChat("Вы проиграли")
        break
    

    if craft.getBlock(cor.x+1, cor.y, cor.z)==22:
        craft.setBlock(cor.x+1, cor.y, cor.z, 0)
        l=l+1
        craft.postToChat("Вы собрали лазурита "+ " l = "+ str(l))
        
    elif craft.getBlock(cor.x-1, cor.y, cor.z)==22:
        craft.setBlock(cor.x-1, cor.y, cor.z, 0)
        l=l+1
        craft.postToChat("Вы собрали лазурита "+ " l = "+ str(l))
        
    elif craft.getBlock(cor.x, cor.y, cor.z-1)==22:
        craft.setBlock(cor.x, cor.y, cor.z-1, 0)
        l=l+1
        craft.postToChat("Вы собрали лазурита "+ " l = "+ str(l))
        
    elif craft.getBlock(cor.x-1, cor.y, cor.z+1)==22:
        craft.setBlock(cor.x, cor.y, cor.z+1, 0)
        l=l+1
        craft.postToChat("Вы собрали лазурита "+ " l = "+ str(l))
        
    time.sleep(0.3)

    if l>=10:
        craft.setBlocks(x-20, y,z-20, x+20, y, z+20, 0)
        craft.postToChat("Вы перешли на второй уровень ")
        break
    
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
    #y=y-1
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
    
    
    




    

