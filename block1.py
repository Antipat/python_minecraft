import mcpi.minecraft as minecraft

import mcpi.block as block

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

for i in range(10):
    craft.setBlock(cor.x+2, cor.y, cor.z, block.DIAMOND_BLOCK.id)
    cor.x = cor.x+1



