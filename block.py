import mcpi.minecraft as minecraft

import mcpi.block as block

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

craft.setBlock(cor.x+2, cor.y, cor.z, block.DIAMOND_BLOCK.id)

craft.setBlock(cor.x+2, cor.y+2, cor.z, block.WOOD.id)

craft.setBlock(cor.x+2, cor.y, cor.z+2, block.IRON_BLOCK.id)

craft.setBlock(cor.x+2, cor.y+2, cor.z+2, block.GOLD_BLOCK.id)

craft.setBlock(cor.x+2, cor.y-1, cor.z-2, block.WATER.id)
