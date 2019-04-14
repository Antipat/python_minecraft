import mcpi.minecraft as minecraft
import mcpi.block as block
import math

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

x=cor.x
y=cor.y
z=cor.z

d1 = []
d2 = []

for i in range(-10, 30):
    y1=-0.5*i+10
    craft.setBlock(x+i, y+y1, z, 35, 0)
    d1.append(x+i)
    d1.append(y+y1)
    
for i in range(-10, 30):
    y1=0.5*i-10
    craft.setBlock(x+i, y+y1, z, 35, 1)
    d2.append(x+i)
    d2.append(y+y1)
    
i=0

for j in range (int(len(d1)/2)):
    if d1[i]==d2[i] and d1[i+1]==d2[i+1]:
        print("Найдена общая точка "+ "A("+str(d1[i])+","+str(d1[i+1])+")")
        print("Найдена общая точка "+ "A("+str(d1[i]-x)+","+str(d1[i+1]-y)+")")
    else:
        print("Поиск общих точек")
    i=i+2

