import mcpi.minecraft as minecraft

import mcpi.block as block

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

d1 = [1, 1, 1, 1, 1]
d2 = [1, 2, 1, 2, 1]
d3 = [1, 1, 0, 1, 1]

#Строим два первых ряда со входом
for j in range(2):
    for i in range(len(d3)):
        if d3[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z, 4)
        elif d3[i]==0:
            craft.setBlock(cor.x, cor.y, cor.z, 0)
        cor.x = cor.x+1
    cor.y = cor.y+1
    cor.x = cor.x-5
    
# строим двасплошных ряда блоков
for j in range(2):
    for i in range(len(d1)):
        if d1[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z, 4)
        elif d1[i]==0:
            craft.setBlock(cor.x, cor.y, cor.z, 0)
        cor.x = cor.x+1
    cor.y = cor.y+1
    cor.x = cor.x-5
    
# строим ряд блоков с окнами
for i in range(len(d2)):
    if d2[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d2[i]==2:
        craft.setBlock(cor.x, cor.y, cor.z, 20)
    cor.x = cor.x+1
cor.y = cor.y+1
cor.x = cor.x-5

# строим двасплошных ряда блоков
for j in range(2):
    for i in range(len(d1)):
        if d1[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z, 4)
        elif d1[i]==0:
            craft.setBlock(cor.x, cor.y, cor.z, 0)
        cor.x = cor.x+1
    cor.y = cor.y+1
    cor.x = cor.x-5
    
# строим ряд блоков с окнами        
for i in range(len(d2)):
    if d2[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d2[i]==2:
        craft.setBlock(cor.x, cor.y, cor.z, 20)
    cor.x = cor.x+1
cor.y = cor.y+1
cor.x = cor.x-5

for i in range(len(d1)):
    if d1[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d1[i]==0:
        craft.setBlock(cor.x, cor.y, cor.z, 0)
    cor.x = cor.x+1
    
# строим вторую стену
cor.y =cor.y - 8
cor.x=cor.x-1

for j in range(4):
    for i in range(len(d1)):
        if d1[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z, 4)
        elif d1[i]==0:
            craft.setBlock(cor.x, cor.y, cor.z, 0)
        cor.z = cor.z+1
    cor.y = cor.y+1
    cor.z = cor.z-5

for i in range(len(d2)):
    if d2[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d2[i]==2:
        craft.setBlock(cor.x, cor.y, cor.z, 20)
    cor.z = cor.z+1
cor.y = cor.y+1
cor.z = cor.z-5

for j in range(2):
    for i in range(len(d1)):
        if d1[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z, 4)
        elif d1[i]==0:
            craft.setBlock(cor.x, cor.y, cor.z, 0)
        cor.z = cor.z+1
    cor.y = cor.y+1
    cor.z = cor.z-5
    
for i in range(len(d2)):
    if d2[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d2[i]==2:
        craft.setBlock(cor.x, cor.y, cor.z, 20)
    cor.z = cor.z+1
cor.y = cor.y+1
cor.z = cor.z-5

for i in range(len(d1)):
    if d1[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d1[i]==0:
        craft.setBlock(cor.x, cor.y, cor.z, 0)
    cor.z = cor.z+1
cor.y = cor.y+1
cor.z = cor.z-5

# строим третью стену
cor.y =cor.y - 9
cor.x=cor.x-4

for j in range(4):
    for i in range(len(d1)):
        if d1[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z, 4)
        elif d1[i]==0:
            craft.setBlock(cor.x, cor.y, cor.z, 0)
        cor.z = cor.z+1
    cor.y = cor.y+1
    cor.z = cor.z-5

for i in range(len(d2)):
    if d2[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d2[i]==2:
        craft.setBlock(cor.x, cor.y, cor.z, 20)
    cor.z = cor.z+1
cor.y = cor.y+1
cor.z = cor.z-5

for j in range(2):
    for i in range(len(d1)):
        if d1[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z, 4)
        elif d1[i]==0:
            craft.setBlock(cor.x, cor.y, cor.z, 0)
        cor.z = cor.z+1
    cor.y = cor.y+1
    cor.z = cor.z-5
    
for i in range(len(d2)):
    if d2[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d2[i]==2:
        craft.setBlock(cor.x, cor.y, cor.z, 20)
    cor.z = cor.z+1
cor.y = cor.y+1
cor.z = cor.z-5

for i in range(len(d1)):
    if d1[i]==1:
        craft.setBlock(cor.x, cor.y, cor.z, 4)
    elif d1[i]==0:
        craft.setBlock(cor.x, cor.y, cor.z, 0)
    cor.z = cor.z+1



# строим четвёртую стену
cor.y =cor.y -8

craft.setBlocks(cor.x, cor.y,cor.z, cor.x+4, cor.y+8, cor.z, 4)

# строим крышу
craft.setBlocks(cor.x, cor.y+9,cor.z, cor.x+4, cor.y+9, cor.z-5, 20)
