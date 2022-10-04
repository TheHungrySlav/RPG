class Weapons:
    def __init__(self,cost_num,type,damage,weight):
        self.cost = cost_num
        self.type = type
        self.damage = damage
        self.weight = weight



# Weapons List
# Light Meele
kunai = Weapons(2,'light meele',3,1)
handaxe = Weapons(5,'light meele',3,2)
javelin = Weapons(5,'light meele',3,2)
light_hammer = Weapons(2,'light meele',4,2)
mace = Weapons(5,'light meele',4,4)
quarterstaff = Weapons(2,'light meele',4,4)
sickle = Weapons(1,'light meele',5,2)
spear = Weapons(1,'light meele',5,3)
kanata = Weapons(5,'light meele',5,3)
shortsword = Weapons(5,'light meele',5,2)

# Heavy Meele
battleaxe = Weapons(10,'Heavy Meele',6,4)
flail = Weapons(10,'Heavy Meele',6,2)
glaive = Weapons(20,'Heavy Meele',6,6)
greataxe = Weapons(30,'Heavy Meele',6,7)
greatsword = Weapons(50,'Heavy Meele',6,6)
halberd = Weapons(20,'Heavy Meele',6,6)
longsword = Weapons(15,'Heavy Meele',6,3)
morningstar = Weapons(15,'Heavy Meele',6,4)
rapier = Weapons(25,'Heavy Meele',6,2)
scimitar = Weapons(25,'Heavy Meele',6,3)
warhammer = Weapons(15,'Heavy Meele',6,2)
Naginata = Weapons(20,'Heavy Meele',7,4)

# Light Ranged
# crossbow_light = Weapons(25,'Light Ranged'4,5)
shortbow = Weapons(25,'Light Ranged',4,2)
shuriken = Weapons(3,'Light Ranged',2,1)

# Heavy Ranged
crossbow_heavy = Weapons(50,'Heavy Ranged',6,18)
longbow = Weapons(50,'Heavy Ranged',6,2)
