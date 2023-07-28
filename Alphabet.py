import mcpi.minecraft as minecraft

import mcpi.block as block

craft = minecraft.Minecraft.create()

cor = craft.player.getTilePos() # получение

class alpha:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def A(self, color):
        Letter = [
        [0,0,0,0,0,1],
        [0,0,0,0,1,1],
        [0,0,0,1,0,1],
        [0,0,1,1,1,1],
        [0,1,0,0,0,1],
        [1,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def B(self, color):
        Letter = [
        [1,1,1,1,1,1],
        [1,0,0,0,0,0],
        [1,1,1,1,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,1,1,1,1,1],
        ]
        self.run(Letter, color)

    def V(self, color):
        Letter = [
        [1,1,1,1,0,0],
        [1,0,0,0,1,0],
        [1,0,0,0,1,0],
        [1,1,1,1,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,1,1,1,1,0],
        ]
        self.run(Letter, color)

    def G(self, color):
        Letter = [
        [1,1,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        ]
        self.run(Letter, color)

    def D(self, color):
        Letter = [
        [0,1,1,1,1,0],
        [0,1,0,0,1,0],
        [0,1,0,0,1,0],
        [0,1,0,0,1,0],
        [0,1,0,0,1,0],
        [1,1,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def E(self, color):
        Letter = [
        [1,1,1,1,1,1],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,1,1,1,1,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,1,1,1,1,1],
        ]
        self.run(Letter, color)

    def J(self, color):
        Letter = [
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [0,1,0,1,0,1,0],
        [0,1,1,1,1,1,0],
        [0,0,1,1,1,0,0],
        [0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0],
        [1,0,0,1,0,0,1],
        ]
        self.run(Letter, color)

    def Z(self, color):
        Letter = [
        [1,1,1,1,1,1],
        [1,0,0,0,0,1],
        [0,0,0,0,0,1],
        [0,1,1,1,1,1],
        [0,0,0,0,0,1],
        [0,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,1,1,1,1,1],
        ]
        self.run(Letter, color)

    def I(self, color):
        Letter = [
        [1,0,0,0,1,1],
        [1,0,0,0,1,1],
        [1,0,0,1,0,1],
        [1,0,0,1,0,1],
        [1,0,1,0,0,1],
        [1,0,1,0,0,1],
        [1,1,0,0,0,1],
        [1,1,0,0,0,1],
        ]
        self.run(Letter, color)

    def Ii(self, color):
        Letter = [
        [0,0,1,1,0,0],
        [1,0,0,0,0,1],
        [1,0,0,0,1,1],
        [1,0,0,1,0,1],
        [1,0,0,1,0,1],
        [1,0,1,0,0,1],
        [1,1,0,0,0,1],
        [1,1,0,0,0,1],
        ]
        self.run(Letter, color)

    def K(self, color):
        Letter = [
        [1,0,0,0,1,1],
        [1,0,0,1,0,0],
        [1,0,1,0,0,0],
        [1,1,0,0,0,0],
        [1,0,1,0,0,0],
        [1,0,0,1,0,0],
        [1,0,0,0,1,0],
        [1,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def L(self, color):
        Letter = [
        [0,0,0,1,1,1],
        [0,0,0,1,0,1],
        [0,0,1,0,0,1],
        [0,0,1,0,0,1],
        [0,1,0,0,0,1],
        [0,1,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        ]
        self.run(Letter, color)


    def M(self, color):
        Letter = [
        [1,1,0,0,0,1,1],
        [1,1,0,0,0,1,1],
        [1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def N(self, color):
        Letter = [
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,1,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def O(self, color):
        Letter = [
        [0,1,1,1,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [0,1,1,1,1,0],
        ]
        self.run(Letter, color)

    def P(self, color):
        Letter = [
        [1,1,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def R(self, color):
        Letter = [
        [1,1,1,1,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,1,1,1,1,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        ]
        self.run(Letter, color)

    def C(self, color):
        Letter = [
        [0,1,1,1,1,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,1],
        [0,1,1,1,1,1],
        ]
        self.run(Letter, color)


    def T(self, color):
        Letter = [
        [1,1,1,1,1,1],
        [1,0,1,1,0,1],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        ]
        self.run(Letter, color)

    def Y(self, color):
        Letter = [
        [1,0,0,0,0,1],
        [0,1,0,0,0,1],
        [0,1,0,0,1,0],
        [0,0,1,0,1,0],
        [0,0,1,1,0,0],
        [0,0,0,1,0,0],
        [0,0,1,0,0,0],
        [0,1,1,0,0,0],
        ]
        self.run(Letter, color)

    def F(self, color):
        Letter = [
        [0,1,1,0,1,1,0],
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [1,1,0,1,0,1,1],
        [0,1,1,1,1,1,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        ]
        self.run(Letter, color)

    def X(self, color):
        Letter = [
        [1,0,0,0,0,1],
        [0,1,0,0,1,0],
        [0,1,0,0,1,0],
        [0,0,1,1,0,0],
        [0,0,1,1,0,0],
        [0,1,0,0,1,0],
        [0,1,0,0,1,0],
        [1,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def Ca(self, color):
        Letter = [
        [0,0,0,0,0,0],
        [1,0,0,0,1,0],
        [1,0,0,0,1,0],
        [1,0,0,0,1,0],
        [1,0,0,0,1,0],
        [1,0,0,0,1,0],
        [0,1,1,1,1,1],
        [0,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def Ch(self, color):
        Letter = [
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [0,1,1,1,1,1],
        [0,0,0,0,0,1],
        [0,0,0,0,0,1],
        [0,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def Sh(self, color):
        Letter = [
        [1,0,0,0,0,0,1],
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [1,0,0,1,0,0,1],
        [1,1,1,1,1,1,1],
        ]
        self.run(Letter, color)

    def She(self, color):
        Letter = [
        [0,0,0,0,0,0,0],
        [1,0,0,1,0,1,0],
        [1,0,0,1,0,1,0],
        [1,0,0,1,0,1,0],
        [1,0,0,1,0,1,0],
        [1,0,0,1,0,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def TV(self, color):
        Letter = [
        [1,1,0,0,0,0],
        [0,1,0,0,0,0],
        [0,1,0,0,0,0],
        [0,1,0,0,0,0],
        [0,1,1,1,1,0],
        [0,1,0,0,0,1],
        [0,1,0,0,0,1],
        [0,1,1,1,1,0],
        ]
        self.run(Letter, color)

    def Yu(self, color):
        Letter = [
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,0,0,1],
        [1,0,0,0,1,0,1],
        [1,0,0,0,1,0,1],
        [0,1,1,1,0,0,1],
        ]
        self.run(Letter, color)

    def Mi(self, color):
        Letter = [
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,0,0,0,0,0],
        [1,1,1,1,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [0,1,1,1,1,0],
        ]
        self.run(Letter, color)

    def Ea(self, color):
        Letter = [
        [1,1,1,1,1,0],
        [1,0,0,0,0,1],
        [0,0,0,0,0,1],
        [0,1,1,1,1,1],
        [0,0,0,0,0,1],
        [0,0,0,0,0,1],
        [1,0,0,0,0,1],
        [1,1,1,1,1,0],
        ]
        self.run(Letter, color)

    def You(self, color):
        Letter = [
        [1,0,0,1,1,1,0],
        [1,0,1,0,0,0,1],
        [1,0,1,0,0,0,1],
        [1,0,1,0,0,0,1],
        [1,1,1,0,0,0,1],
        [1,0,1,0,0,0,1],
        [1,0,1,0,0,0,1],
        [1,0,0,1,1,1,0],
        ]
        self.run(Letter, color)

    def Ia(self, color):
        Letter = [
        [0,1,1,1,1,0],
        [1,0,0,0,0,1],
        [1,0,0,0,0,1],
        [0,1,1,1,1,1],
        [0,0,0,1,0,1],
        [0,0,1,0,0,1],
        [0,1,0,0,0,1],
        [1,0,0,0,0,1],
        ]
        self.run(Letter, color)

    def Space(self, color):
        Letter = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        ]
        self.run(Letter, color)


    def run(self, Letter, color):
        for j in range(len(Letter)):
            for i in range(len(Letter[0])):
                if Letter[j][i]==1:
                    craft.setBlock(self.x+i, self.y-j, self.z, color)
                else:   #elif n[j][i]==0:
                    craft.setBlock(self.x+i, self.y-j, self.z,0)

x = cor.x + 1
y = cor.y + 8
z = cor.z
Byk = alpha(x,y,z)

color =(35,0)
#Byk.A(color)

# словарь русского алфавита
'''Alpha = {"А": Byk.A(color), "Б": Byk.B(color), "В": Byk.V(color), "Г":Byk.G(color), "Д": Byk.D(color), "Е": Byk.E(color),
"Ж":Byk.J(color) , "З": Byk.Z(color), "И": Byk.I(color), "Й": Byk.Ii(color), "К": Byk.K(color), "Л":Byk.L(color),
"М": Byk.M(color), "Н": Byk.N(color), "О": Byk.O(color), "П": Byk.P(color), "Р": Byk.R(color), "С": Byk.C(color),
"Т": Byk.T(color), "У": Byk.Y(color), "Ф": Byk.F(color) , "Х": Byk.X(color) , "Ц": Byk.Ca(color), "Ч": Byk.Ch(color),
"Ш": Byk.Sh(color), "Щ": Byk.She(color), "Ъ": Byk.TV(color), "Ы": Byk.Yu(color), "Ь": Byk.Mi(color), "Э": Byk.Ea(color),
"Ю": Byk.You(color), "Я": Byk.Ia(color)}'''

Alpha1 = ("А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л","М", "Н", "О", "П", "Р", "С","Т", "У", "Ф", "Х",
"Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э","Ю", "Я")

Alpha2 = (Byk.A(color), Byk.B(color), Byk.V(color), Byk.G(color), Byk.D(color), Byk.E(color),
Byk.J(color), Byk.Z(color), Byk.I(color), Byk.Ii(color), Byk.K(color), Byk.L(color), Byk.M(color), Byk.N(color),
Byk.O(color), Byk.P(color), Byk.R(color), Byk.C(color), Byk.T(color), Byk.Y(color), Byk.F(color), Byk.X(color),
Byk.Ca(color), Byk.Ch(color), Byk.Sh(color), Byk.She(color), Byk.TV(color), Byk.Yu(color), Byk.Mi(color), Byk.Ea(color),
Byk.You(color), Byk.Ia(color))

#Alpha["А"]()
#Alpha.get("А")


# Ввод текста
Text = input()

for i in Text:
    ind = Alpha1.index(i)
    Alpha2[ind]
    x=x+9
    y = cor.y + 8
    z = cor.z
    Byk = alpha(x,y,z)



# 42 IRON_BLOCK ЖЕЛЕЗНЫЙ БЛОК
# 7 BEDROCK
# 5 WOOD_PLANKS ДЕРЕВЯННЫЕ ДОСКИ
# 3 DIRT ЗЕМЛЯ
# 35 WOOL ШЕРСТЬ
# 45 BRICK_BLOCK кИРПИЧНЫЙ БЛОК
# 57 DIAMOND_BLOCK АЛМАЗНЫЙ БЛОК












