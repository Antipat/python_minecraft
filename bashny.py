import mcpi.minecraft as minecraft
import mcpi.block as block
craft=minecraft.Minecraft.create()
cor=craft.player.getTilePos ()
x=cor.x
y=cor.y
z=cor.z

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



