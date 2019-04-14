import mcpi.minecraft as minecraft

craft=minecraft.Minecraft.create()

while True:
    cor=craft.player.getTilePos()
    craft.postToChat("x = "+str(cor.x)+" y = "+ str(cor.y)+" z = "+str(cor.z))
    
