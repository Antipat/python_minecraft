import mcpi.minecraft as minecraft

craft=minecraft.Minecraft.create()

while True:
    cor=craft.player.getTilePos()

    if cor.x==-472 and cor.y == 68 and cor.z == -547:
        craft.postToChat("Добро пожаловать домой")
    else:
        craft.postToChat("Иди домой")
    
