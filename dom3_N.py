import mcpi.minecraft as minecraft

import mcpi.block as block

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos()

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

