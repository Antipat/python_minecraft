import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

craft = minecraft.Minecraft.create()
cor = craft.player.getTilePos()
x=cor.x+1
y=cor.y
z=cor.z
    
def avto1(x,y,z):
    
    craft.setBlocks(x, y, z, x+1, y+2, z+4, 5)
    craft.setBlocks(x, y+1, z, x+1, y+2, z, 0)
    craft.setBlocks(x, y+1, z+2, x+1, y+1, z+2, 0)
    craft.setBlocks(x, y+1, z+4, x+1, y+2, z+4, 0)
    
def avto2(x,y,z):
    
    craft.setBlocks(x, y, z, x+4, y+2, z+1, 5)
    craft.setBlocks(x, y+1, z, x, y+2, z+1, 0)
    craft.setBlocks(x+2, y+1, z, x+2, y+1, z+1, 0)
    craft.setBlocks(x+4, y+1, z, x+4, y+2, z+1, 0)

def dom_N(x, y, z):
    sx = x +2+ 5/2 # центр по X

    sy = y + 5/2 # центр по Y

    sz = z+5/2 # центр по Z

    craft.setBlocks(x+1, y, z, x+6, y+5, z+5, block.GOLD_BLOCK.id)

    craft.setBlocks(x+2, y+1, z+1, x+5, y+4, z+4, block.AIR.id)

    craft.setBlocks(sx-1, y+1, z, sx, y+2, z, block.AIR.id)

    craft.setBlocks(sx+1, sy+1, z, sx+1, sy+2, z, block.GLASS.id)

    craft.setBlocks(sx-2, sy+1, z, sx-2, sy+2, z, block.GLASS.id)

    craft.setBlocks(x+1, sy+1, sz+2, x+1, sy+2, sz+2, block.GLASS.id)

    craft.setBlocks(x+1, sy+1, sz-1, x+1, sy+2, sz-1, block.GLASS.id)

    craft.setBlocks(x+6, sy+1, sz+2, x+6, sy+2, sz+2, block.GLASS.id)

    craft.setBlocks(x+6, sy+1, sz-1, x+6, sy+2, sz-1, block.GLASS.id)

    craft.setBlocks(x+1, y+6, z, x+6, y+6, z+5, block.IRON_BLOCK.id)
    craft.setBlocks(x+2, y+7, z, x+5, y+7, z+5, block.IRON_BLOCK.id)
    craft.setBlocks(x+3, y+8, z, x+4, y+8, z+5, block.IRON_BLOCK.id)


craft.setBlocks(cor.x-2, cor.y, cor.z-2, cor.x+22, cor.y+3, cor.z+76, block.IRON_BLOCK.id)
craft.setBlocks(cor.x-1, cor.y, cor.z-1, cor.x+21, cor.y+3, cor.z+75, 0)
craft.setBlocks(cor.x-1, cor.y-1, cor.z+50, cor.x+21, cor.y-1, cor.z+51, 10)

# Создаём пьедестал к кубку
craft.setBlocks(cor.x+5, cor.y+1, cor.z+70, cor.x+15, cor.y+1, cor.z+75, 57)

# Создаём кубок
craft.setBlocks(cor.x+8, cor.y+2, cor.z+72, cor.x+12, cor.y+2, cor.z+72, 89)
craft.setBlocks(cor.x+10, cor.y+2, cor.z+72, cor.x+10, cor.y+4, cor.z+72, 89)
craft.setBlocks(cor.x+8, cor.y+5, cor.z+72, cor.x+12, cor.y+5, cor.z+72, 89)
craft.setBlocks(cor.x+7, cor.y+6, cor.z+72, cor.x+13, cor.y+6, cor.z+72, 89)
craft.setBlocks(cor.x+6, cor.y+7, cor.z+72, cor.x+14, cor.y+7, cor.z+72, 89)
craft.setBlocks(cor.x+6, cor.y+8, cor.z+72, cor.x+14, cor.y+8, cor.z+72, 89)
craft.setBlocks(cor.x+6, cor.y+9, cor.z+72, cor.x+14, cor.y+9, cor.z+72, 89)


z=z+5
z1=cor.z+20
z2 = cor.z+40
x1 = cor.x+15
x11 = cor.x +5
x22 = cor.x+10
z11 = cor.z+10
z22 = cor.z+30
y11 =cor.y +12
y22 = cor.y

x33 = cor.x
z33 = cor.z
while True:
    cor = craft.player.getTilePos()
    for i in range(8):
        cor = craft.player.getPos()
        for i in range(5):
            if craft.getBlock(cor.x-i, cor.y, cor.z)==5 or craft.getBlock(cor.x+i, cor.y, cor.z)==5:
                craft.player.setTilePos(x33, y, z33)
                craft.postToChat("Вы проиграли, начните заново")
        
        if craft.getBlock(cor.x, cor.y-1, cor.z)==11:
            craft.player.setTilePos(x33, y, z33)
            craft.postToChat("Вы проиграли, начните заново")
            
        elif craft.getBlock(cor.x-1, cor.y, cor.z)==89  or craft.getBlock(cor.x+1, cor.y, cor.z)==89 or craft.getBlock(cor.x, cor.y, cor.z-1)==89 or craft.getBlock(cor.x, cor.y, cor.z+1)==89:
            craft.postToChat("Вы ПОБЕДИЛИ")
        for i in range(10):
            if craft.getBlock(cor.x, cor.y+i, cor.z)==41:
                craft.player.setTilePos(x33, y, z33)
                craft.postToChat("Вы проиграли, начните заново")
            
        avto2(x,y,z)
        avto2(x1,y,z1)
        avto2(x,y,z2)
        
        dom_N(x11,y11,z11)
        dom_N(x22, y22, z22)
        
        x=x+2
        x1=x1-2
        y11 = y11 - 1
        y22 = y22 + 1
        
        time.sleep(0.5)
        craft.setBlocks(x-5, y, z, x, y+2, z+1, 0)
        craft.setBlocks(x1, y, z1, x1+10, y+2, z1+1, 0)
        craft.setBlocks(x-5, y, z2, x, y+2, z2+1, 0)
        
        craft.setBlocks(x11, y11+10, z11, x11+6, y11, z11+5, 0)
        craft.setBlocks(x22, y22-1, z22, x22+6, y22, z22+5, 0)

        
       
        
            
        
    for i in range(8):
        cor = craft.player.getTilePos()
       
        for i in range(5):
            if craft.getBlock(cor.x-i, cor.y, cor.z)==5 or craft.getBlock(cor.x+i, cor.y, cor.z)==5:
                craft.player.setTilePos(x33, y, z33)
                craft.postToChat("Вы проиграли, начните заново")
            
        if craft.getBlock(cor.x, cor.y-1, cor.z)==11:
            craft.player.setTilePos(x33, y, z33)
            craft.postToChat("Вы проиграли, начните заново")
        
        elif craft.getBlock(cor.x-1, cor.y, cor.z)==89  or craft.getBlock(cor.x+1, cor.y, cor.z)==89 or craft.getBlock(cor.x, cor.y, cor.z-1)==89 or craft.getBlock(cor.x, cor.y, cor.z+1)==89:
            craft.postToChat("Вы ПОБЕДИЛИ")
        for i in range(10):
            if craft.getBlock(cor.x, cor.y+i, cor.z)==41:
                craft.player.setTilePos(x33, y, z33)
                craft.postToChat("Вы проиграли, начните заново")
            
        avto2(x,y,z)
        avto2(x1,y,z1)
        avto2(x,y,z2)
        
        dom_N(x11,y11,z11)
        dom_N(x22, y22, z22)
        
        x=x-2
        x1=x1+2
        
        y11 = y11 + 1
        y22 = y22 - 1
        
        time.sleep(0.5)
        craft.setBlocks(x, y, z, x+10, y+2, z+1, 0)
        craft.setBlocks(x1-5, y, z1, x1, y+2, z1+1, 0)
        craft.setBlocks(x, y, z2, x+10, y+2, z2+1, 0)
        
        craft.setBlocks(x11, y11-1, z11, x11+6, y11, z11+5, 0)
        craft.setBlocks(x22, y22+10, z22, x22+6, y22, z22+5, 0)

        
    
        

   

    
    
