import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos ()

craft.setBlocks(cor.x, cor.y-1, cor.z, cor.x+110, cor.y-1, cor.z+200, 7)
x=cor.x
y=cor.y
z=cor.z
craft.setBlocks(x,y,z,x+120, y+20, z+200, block.AIR.id)
#11 - dom_N
#12 - dom_S
#13 - dom_E
#14 - dom_W
#21 - dom2_N
#22 - dom2_S
#3 - bashny
#4 - most
d11 = [3, 0, 13, 13, 13, 13, 13, 0, 3, 0]
d21 = [22, 0, 14, 14, 14, 14, 14, 0, 21, 0]
d31 = [22, 0, 21, 0, 0, 0, 22, 0, 21, 0]
d41 = [22, 0, 21, 4, 22, 0, 21, 0]
d51 = [3, 0, 14, 14, 14, 14, 14, 0, 3, 0]
d61 = [22, 0, 13, 13, 13, 13, 13, 0, 21, 0]
def dom_N():
    sx = cor.x +2+ 5/2 # центр по X

    sy = cor.y + 5/2 # центр по Y

    sz = cor.z+5/2 # центр по Z

    craft.setBlocks(cor.x+1, cor.y, cor.z, cor.x+6, cor.y+5, cor.z+5, block.GOLD_BLOCK.id)

    craft.setBlocks(cor.x+2, cor.y+1, cor.z+1, cor.x+5, cor.y+4, cor.z+4, block.AIR.id)

    craft.setBlocks(sx-1, cor.y+1, cor.z, sx, cor.y+2, cor.z, block.AIR.id)

    craft.setBlocks(sx+1, sy+1, cor.z, sx+1, sy+2, cor.z, block.GLASS.id)

    craft.setBlocks(sx-2, sy+1, cor.z, sx-2, sy+2, cor.z, block.GLASS.id)


    craft.setBlocks(cor.x+1, sy+1, sz+2, cor.x+1, sy+2, sz+2, block.GLASS.id)

    craft.setBlocks(cor.x+1, sy+1, sz-1, cor.x+1, sy+2, sz-1, block.GLASS.id)

    craft.setBlocks(cor.x+6, sy+1, sz+2, cor.x+6, sy+2, sz+2, block.GLASS.id)

    craft.setBlocks(cor.x+6, sy+1, sz-1, cor.x+6, sy+2, sz-1, block.GLASS.id)


    craft.setBlocks(cor.x+1, cor.y+6, cor.z, cor.x+6, cor.y+6, cor.z+5, block.IRON_BLOCK.id)
    craft.setBlocks(cor.x+2, cor.y+7, cor.z, cor.x+5, cor.y+7, cor.z+5, block.IRON_BLOCK.id)
    craft.setBlocks(cor.x+3, cor.y+8, cor.z, cor.x+4, cor.y+8, cor.z+5, block.IRON_BLOCK.id)

def dom_S():
    sx = cor.x +2+ 5/2 # центр по X

    sy = cor.y + 5/2 # центр по Y

    sz = cor.z+5/2 # центр по Z

    craft.setBlocks(cor.x+1, cor.y, cor.z, cor.x+6, cor.y+5, cor.z+5, block.GOLD_BLOCK.id)

    craft.setBlocks(cor.x+2, cor.y+1, cor.z+1, cor.x+5, cor.y+4, cor.z+4, block.AIR.id)

    craft.setBlocks(sx-1, cor.y+1, cor.z+5, sx, cor.y+2, cor.z+5, block.AIR.id)

    craft.setBlocks(sx+1, sy+1, cor.z+5, sx+1, sy+2, cor.z+5, block.GLASS.id)

    craft.setBlocks(sx-2, sy+1, cor.z+5, sx-2, sy+2, cor.z+5, block.GLASS.id)


    craft.setBlocks(cor.x+1, sy+1, sz+2, cor.x+1, sy+2, sz+2, block.GLASS.id)

    craft.setBlocks(cor.x+1, sy+1, sz-1, cor.x+1, sy+2, sz-1, block.GLASS.id)

    craft.setBlocks(cor.x+6, sy+1, sz+2, cor.x+6, sy+2, sz+2, block.GLASS.id)

    craft.setBlocks(cor.x+6, sy+1, sz-1, cor.x+6, sy+2, sz-1, block.GLASS.id)


    craft.setBlocks(cor.x+1, cor.y+6, cor.z, cor.x+6, cor.y+6, cor.z+5, block.IRON_BLOCK.id)
    craft.setBlocks(cor.x+2, cor.y+7, cor.z, cor.x+5, cor.y+7, cor.z+5, block.IRON_BLOCK.id)
    craft.setBlocks(cor.x+3, cor.y+8, cor.z, cor.x+4, cor.y+8, cor.z+5, block.IRON_BLOCK.id)

def dom_E():
    sx = cor.x +2+ 5/2 # центр по X

    sy = cor.y + 5/2 # центр по Y

    sz = cor.z+5/2 # центр по Z

    craft.setBlocks(cor.x+1, cor.y, cor.z, cor.x+6, cor.y+5, cor.z+5, block.GOLD_BLOCK.id)

    craft.setBlocks(cor.x+2, cor.y+1, cor.z+1, cor.x+5, cor.y+4, cor.z+4, block.AIR.id)



    craft.setBlocks(cor.x+6, cor.y+1, sz, cor.x+6, cor.y+2, sz+1, block.AIR.id)

    craft.setBlocks(cor.x+6, sy+1, sz+2, cor.x+6, sy+2, sz+2, block.GLASS.id)

    craft.setBlocks(cor.x+6, sy+1, sz-1, cor.x+6, sy+2, sz-1, block.GLASS.id)


    craft.setBlocks(sx-1, sy+1, cor.z, sx-1, sy+2, cor.z, block.GLASS.id)

    craft.setBlocks(sx+1, sy+1, cor.z, sx+1, sy+2, cor.z, block.GLASS.id)

    craft.setBlocks(sx-1, sy+1, cor.z+5, sx-1, sy+2, cor.z+5, block.GLASS.id)

    craft.setBlocks(sx+1, sy+1, cor.z+5, sx+1, sy+2, cor.z+5, block.GLASS.id)


    craft.setBlocks(cor.x+1, cor.y+6, cor.z, cor.x+6, cor.y+6, cor.z+5, block.IRON_BLOCK.id)
    craft.setBlocks(cor.x+1, cor.y+7, cor.z+1, cor.x+6, cor.y+7, cor.z+4, block.IRON_BLOCK.id)
    craft.setBlocks(cor.x+1, cor.y+8, cor.z+2, cor.x+6, cor.y+8, cor.z+3, block.IRON_BLOCK.id)

def dom_W():
    sx = cor.x +2+ 5/2 # центр по X

    sy = cor.y + 5/2 # центр по Y

    sz = cor.z+5/2 # центр по Z

    craft.setBlocks(cor.x+1, cor.y, cor.z, cor.x+6, cor.y+5, cor.z+5, block.GOLD_BLOCK.id)

    craft.setBlocks(cor.x+2, cor.y+1, cor.z+1, cor.x+5, cor.y+4, cor.z+4, block.AIR.id)

    craft.setBlocks(cor.x+1, cor.y+1, sz, cor.x+1, cor.y+2, sz+1, block.AIR.id)

    craft.setBlocks(cor.x+1, sy+1, sz+2, cor.x+1, sy+2, sz+2, block.GLASS.id)

    craft.setBlocks(cor.x+1, sy+1, sz-1, cor.x+1, sy+2, sz-1, block.GLASS.id)

    craft.setBlocks(sx-1, sy+1, cor.z, sx-1, sy+2, cor.z, block.GLASS.id)

    craft.setBlocks(sx+1, sy+1, cor.z, sx+1, sy+2, cor.z, block.GLASS.id)

    craft.setBlocks(sx-1, sy+1, cor.z+5, sx-1, sy+2, cor.z+5, block.GLASS.id)

    craft.setBlocks(sx+1, sy+1, cor.z+5, sx+1, sy+2, cor.z+5, block.GLASS.id)


    craft.setBlocks(cor.x+1, cor.y+6, cor.z, cor.x+6, cor.y+6, cor.z+5, block.IRON_BLOCK.id)
    craft.setBlocks(cor.x+1, cor.y+7, cor.z+1, cor.x+6, cor.y+7, cor.z+4, block.IRON_BLOCK.id)
    craft.setBlocks(cor.x+1, cor.y+8, cor.z+2, cor.x+6, cor.y+8, cor.z+3, block.IRON_BLOCK.id)

def dom2_N():
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

def dom2_S():
    d1 = [1, 1, 1, 1, 1]
    d2 = [1, 2, 1, 2, 1]
    d3 = [1, 1, 0, 1, 1]

    #Строим два первых ряда со входом
    for j in range(2):
        for i in range(len(d3)):
            if d3[i]==1:
                craft.setBlock(cor.x, cor.y, cor.z+5, 4)
            elif d3[i]==0:
                craft.setBlock(cor.x, cor.y, cor.z+5, 0)
            cor.x = cor.x+1
        cor.y = cor.y+1
        cor.x = cor.x-5
    
    # строим двасплошных ряда блоков
    for j in range(2):
        for i in range(len(d1)):
            if d1[i]==1:
                craft.setBlock(cor.x, cor.y, cor.z+5, 4)
            elif d1[i]==0:
                craft.setBlock(cor.x, cor.y, cor.z+5, 0)
            cor.x = cor.x+1
        cor.y = cor.y+1
        cor.x = cor.x-5
    
    # строим ряд блоков с окнами
    for i in range(len(d2)):
        if d2[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z+5, 4)
        elif d2[i]==2:
            craft.setBlock(cor.x, cor.y, cor.z+5, 20)
        cor.x = cor.x+1
    cor.y = cor.y+1
    cor.x = cor.x-5

    # строим двасплошных ряда блоков
    for j in range(2):
        for i in range(len(d1)):
            if d1[i]==1:
                craft.setBlock(cor.x, cor.y, cor.z+5, 4)
            elif d1[i]==0:
                craft.setBlock(cor.x, cor.y, cor.z+5, 0)
            cor.x = cor.x+1
        cor.y = cor.y+1
        cor.x = cor.x-5
    
    # строим ряд блоков с окнами        
    for i in range(len(d2)):
        if d2[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z+5, 4)
        elif d2[i]==2:
            craft.setBlock(cor.x, cor.y, cor.z+5, 20)
        cor.x = cor.x+1
    cor.y = cor.y+1
    cor.x = cor.x-5

    for i in range(len(d1)):
        if d1[i]==1:
            craft.setBlock(cor.x, cor.y, cor.z+5, 4)
        elif d1[i]==0:
            craft.setBlock(cor.x, cor.y, cor.z+5, 0)
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
    craft.setBlocks(cor.x, cor.y,cor.z-5, cor.x+4, cor.y+8, cor.z-5, 4)

    # строим крышу
    craft.setBlocks(cor.x, cor.y+9,cor.z, cor.x+4, cor.y+9, cor.z-5, 20)

def bashny():
    # Создаём первую опору башни 
    for i in range (5):
        craft.setBlock(x+i,y+i,z, block.STONE.id)
   
    # Создаём вторую опору башни
    for i in range (5):
        craft.setBlock(x+10+i,y+4-i,z, block.STONE.id)
    
    # Создаём площадку на высоте y+5
    craft.setBlocks(x+5,y+5,z,x+10, y+5, z+5, block.STONE.id)

    # Создаём третью опору
    for i in range (5):
        craft.setBlock(x+10+i,y+4-i,z+5, block.STONE.id)
    
    # Создаём четвёртую опору    
    for i in range (5):
        craft.setBlock(x+i,y+i,z+5, block.STONE.id)
    
    # Создаём четыре опоры на высоте y+5    
    for w in range(5):
        craft.setBlock(x+5,y+5+w,z, block.STONE.id)
        craft.setBlock(x+10,y+5+w,z, block.STONE.id)
        craft.setBlock(x+5,y+5+w,z+5, block.STONE.id)
        craft.setBlock(x+10,y+5+w,z+5, block.STONE.id)
    
    #создаём площадку на высоте y+10
    craft.setBlocks(x+5,y+10,z,x+10, y+10, z+5, block.STONE.id)

    #Создаём две опоры для третьей площадки-крыши    
    for i in range (3):
        craft.setBlock(x+5+i,y+11+i,z, block.STONE.id)
    for i in range (3):
        craft.setBlock(x+8+i,y+13-i,z, block.STONE.id)
    
    #Создание третьей площадки-крыши    
    craft.setBlocks(x+7,y+13,z,x+8, y+13, z+5, block.STONE.id)

    # Создание двух оставшихся опор от второй до третьей площадки
    for i in range (3):
        craft.setBlock(x+5+i,y+11+i,z+5, block.STONE.id)
    for i in range (3):
        craft.setBlock(x+8+i,y+13-i,z+5, block.STONE.id)

    # Создание в центре башни на второй площадке куба из Золотых и стеклянных блоков с центральным блоком - лава.    
    craft.setBlocks(x+7,y+6,z+2,x+8, y+6, z+3, block.GOLD_BLOCK.id)
    craft.setBlocks(x+6,y+7,z+1,x+9, y+8, z+4, block.GLASS.id)
    craft.setBlocks(x+7,y+7,z+2,x+8, y+8, z+3, block.LAVA_FLOWING .id)
    craft.setBlocks(x+7,y+9,z+2,x+8, y+9, z+3, block.GOLD_BLOCK.id)
    
def most():
    # Создание четырёх опор моста
    craft.setBlocks(x+1,y,z, x+1, y+15, z, 98)
    craft.setBlocks(x+6,y,z, x+6, y+15, z, 98)

    craft.setBlocks(x+1,y,z+30, x+1, y+15, z+30, 98)
    craft.setBlocks(x+6,y,z+30, x+6, y+15, z+30, 98)

    # Создание площадки моста
    craft.setBlocks(x+1,y+5,z, x+6, y+5, z+30, 98)

    # Создание опор для каната
    for i in range(5, 30, 10):
        craft.setBlocks(x+1,y+5,z+i, x+1, y+10, z+i, 98)
    for i in range(10, 30, 10):
        craft.setBlocks(x+1,y+5,z+i, x+1, y+15, z+i, 45)
    for i in range(5, 30, 10):
        craft.setBlocks(x+6,y+5,z+i, x+6, y+10, z+i, 45)
    for i in range(10, 30, 10):
        craft.setBlocks(x+6,y+5,z+i, x+6, y+15, z+i, 98)
    
    # Создание каната с одной стороны моста
    for i in range(5):
        craft.setBlock(x+1,y+15-i,z+i, 22)
    for i in range(5):
        craft.setBlock(x+1,y+11+i,z+5+i, 22)
    for i in range(5):
        craft.setBlock(x+1,y+15-i,z+10+i, 22)
    for i in range(5):
        craft.setBlock(x+1,y+11+i,z+15+i, 22)
    for i in range(5):
        craft.setBlock(x+1,y+15-i,z++20+i, 22)
    for i in range(5):
        craft.setBlock(x+1,y+11+i,z+25+i, 22)

    # Создание каната с другой стороны моста
    for i in range(5):
        craft.setBlock(x+6,y+15-i,z+i, 22)
    for i in range(5):
        craft.setBlock(x+6,y+11+i,z+5+i, 22)
    for i in range(5):
        craft.setBlock(x+6,y+15-i,z+10+i, 22)
    for i in range(5):
        craft.setBlock(x+6,y+11+i,z+15+i, 22)
    for i in range(5):
        craft.setBlock(x+6,y+15-i,z++20+i, 22)
    for i in range(5):
        craft.setBlock(x+6,y+11+i,z+25+i, 22)

    # Продолжение канатов до земли
    for i in range(17):
        craft.setBlock(x+6,y+15-i,z-0.5*i, 22)
    for i in range(17):
        craft.setBlock(x+1,y+15-i,z-0.5*i, 22)
    for i in range(17):
        craft.setBlock(x+6,y+15-i,z+30+0.5*i, 22)
    for i in range(17):
        craft.setBlock(x+1,y+15-i,z+30 + 0.5*i, 22)

    # Создание лестниц на мост
    for i in range(5):
        craft.setBlocks(x+1,y+i,z-5+i,x+6, y+i, z-5+i, 35,14)
    for i in range(5):
        craft.setBlocks(x+1,y+i,z+35-i,x+6, y+i, z+35-i, 35,14)

    # Создание фрагмента реки
    craft.setBlocks(x-10, y-1, z+3, x+10, y-1, z+27, 8)

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
    

for k in range (len(d11)):
    if d11[k]==3:
        bashny()
    elif d11[k]==0:
        craft.setBlocks(cor.x, cor.y, cor.z, cor.x+5, cor.y+5, cor.x+5, 0)
    elif d11[k]==13:
        dom_E()
    cor.z =cor.z+20
    x=cor.x
    y=cor.y
    z=cor.z
cor.z = cor.z - 20*len(d11)
cor.x = cor.x + 15

for k in range (len(d21)):
    if d21[k]==22:
        dom2_S()
        cor.z=cor.z-5
    elif d21[k]==14:
        dom_W()
   
    cor.z =cor.z+20
    x=cor.x
    y=cor.y
    z=cor.z
cor.z = cor.z -20*len(d21)
cor.x = cor.x + 15

for k in range (len(d31)):
    if d31[k]==22:
        dom2_S()
        cor.z=cor.z-5
    elif d31[k]==21:
        dom2_N()
        cor.z=cor.z-5
    elif d31[k]==0:
        craft.setBlocks(cor.x, cor.y, cor.z, cor.x+5, cor.y+5, cor.x+5, 0)
   
    cor.z =cor.z+20
    x=cor.x
    y=cor.y
    z=cor.z
cor.z = cor.z -20*len(d21)
cor.x = cor.x + 15

for k in range (len(d41)):
    if d41[k]==22:
        dom2_S()
        cor.z=cor.z-5
    elif d41[k]==21:
        dom2_N()
        cor.z=cor.z-5
    elif d41[k]==0:
        craft.setBlocks(cor.x, cor.y, cor.z, cor.x+5, cor.y+5, cor.x+5, 0)
    elif d41[k]==4:
        most()
        cor.z=cor.z + 38
   
    cor.z =cor.z+20
    x=cor.x
    y=cor.y
    z=cor.z
cor.z = cor.z -20*len(d21)
cor.x = cor.x + 15


for k in range (len(d31)):
    if d31[k]==22:
        dom2_S()
        cor.z=cor.z-5
    elif d31[k]==21:
        dom2_N()
        cor.z=cor.z-5
    elif d31[k]==0:
        craft.setBlocks(cor.x, cor.y, cor.z, cor.x+5, cor.y+5, cor.x+5, 0)
   
    cor.z =cor.z+20
    x=cor.x
    y=cor.y
    z=cor.z
cor.z = cor.z -20*len(d31)
cor.x = cor.x + 15

for k in range (len(d61)):
    if d61[k]==22:
        dom2_S()
        cor.z=cor.z-5
    elif d61[k]==13:
        dom_E()
    elif d61[k]==0:
        craft.setBlocks(cor.x, cor.y, cor.z, cor.x+5, cor.y+5, cor.x+5, 0)
    elif d61[k]==21:
        dom2_N()
        cor.z=cor.z-5
    cor.z =cor.z+20
    x=cor.x
    y=cor.y
    z=cor.z
cor.z = cor.z -20*len(d21)

cor=craft.player.getTilePos ()
cor.x = cor.x + 100
x = cor.x
y = cor.y
z = cor.z

for k in range (len(d51)):
    if d51[k]==3:
        bashny()
    elif d51[k]==0:
        craft.setBlocks(cor.x, cor.y, cor.z, cor.x+5, cor.y+5, cor.x+5, 0)
    elif d51[k]==14:
        dom_W()
    cor.z =cor.z+20
    x=cor.x
    y=cor.y
    z=cor.z
    
cor=craft.player.getTilePos ()

a = cor.x+5
b = cor.y
d = cor.z+12
c = [41,45,22]
while True:
    x=a
    y=b
    z=d
    while True:
        for i in range(18):
            
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+20, cor.y-1, cor.z+10, cor.x+25, cor.y-1, cor.z+35, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+88, cor.y-1, cor.z+40, cor.x+100, cor.y-1, cor.z+45, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+70, cor.y-1, cor.z+125, cor.x+65, cor.y-1, cor.z+145, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+5, cor.y-1, cor.z+40, cor.x+15, cor.y-1, cor.z+45, c[ff])
            avto2()
            if craft.getBlock(x, y-1, z)==41:
                craft.postToChat("Стоим пять секунд ")
                time.sleep(5)
            elif craft.getBlock(x, y-1, z)==45:
                craft.postToChat("Стоим десять секунд ")
                time.sleep(10)
            elif craft.getBlock(x, y-1, z)==22:
                craft.postToChat("Движение открыто ")
            x=x+5
            time.sleep(0.5)
            craft.setBlocks(x-5, y, z, x, y+2, z+1, 0)

        for i in range(24):
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+20, cor.y-1, cor.z+10, cor.x+25, cor.y-1, cor.z+35, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+88, cor.y-1, cor.z+40, cor.x+100, cor.y-1, cor.z+45, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+70, cor.y-1, cor.z+125, cor.x+65, cor.y-1, cor.z+145, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+5, cor.y-1, cor.z+40, cor.x+15, cor.y-1, cor.z+45, c[ff])
            avto1()
            if craft.getBlock(x, y-1, z)==41:
                craft.postToChat("Стоим пять секунд ")
                time.sleep(5)
            elif craft.getBlock(x, y-1, z)==45:
                craft.postToChat("Стоим десять секунд ")
                time.sleep(10)
            elif craft.getBlock(x, y-1, z)==22:
                craft.postToChat("Движение открыто ")
            z=z+5
            time.sleep(0.5)
            craft.setBlocks(x, y, z-5, x+1, y+2, z, 0)

        for i in range(17):
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+20, cor.y-1, cor.z+10, cor.x+25, cor.y-1, cor.z+35, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+88, cor.y-1, cor.z+40, cor.x+100, cor.y-1, cor.z+45, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+70, cor.y-1, cor.z+125, cor.x+65, cor.y-1, cor.z+145, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+5, cor.y-1, cor.z+40, cor.x+15, cor.y-1, cor.z+45, c[ff])
            avto2()
            if craft.getBlock(x, y-1, z)==41:
                craft.postToChat("Стоим пять секунд ")
                time.sleep(5)
            elif craft.getBlock(x, y-1, z)==45:
                craft.postToChat("Стоим десять секунд ")
                time.sleep(10)
            elif craft.getBlock(x, y-1, z)==22:
                craft.postToChat("Движение открыто ")
            #craft.postToChat(str())
            x=x-5
            time.sleep(0.5)
            craft.setBlocks(x, y, z, x+10, y+2, z+1, 0)

        for i in range(24):
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+20, cor.y-1, cor.z+10, cor.x+25, cor.y-1, cor.z+35, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+88, cor.y-1, cor.z+40, cor.x+100, cor.y-1, cor.z+45, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+70, cor.y-1, cor.z+125, cor.x+65, cor.y-1, cor.z+145, c[ff])
            ff = random.randint(0, 2)
            craft.setBlocks(cor.x+5, cor.y-1, cor.z+40, cor.x+15, cor.y-1, cor.z+45, c[ff])
            avto1()
            if craft.getBlock(x, y-1, z)==41:
                craft.postToChat("Стоим пять секунд ")
                time.sleep(5)
            elif craft.getBlock(x, y-1, z)==45:
                craft.postToChat("Стоим десять секунд ")
                time.sleep(10)
            elif craft.getBlock(x, y-1, z)==22:
                craft.postToChat("Движение открыто ")
            z=z-5
            time.sleep(0.5)
            craft.setBlocks(x, y, z, x+1, y+2, z+10, 0)
        break
    
    
