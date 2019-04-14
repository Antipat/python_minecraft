import mcpi.minecraft as minecraft
craft=minecraft.Minecraft.create()

cor=craft.player.getTilePos()

print(cor.x, cor.y, cor.z)
