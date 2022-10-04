# Character Creator

def creator(name,characterclass):

    # Character STATS
    class STATS:
        def __init__(self,name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod):
            self.name = name
            self.HPmax = HPmax
            self.Manamax = Manamax
            self.strength = strength
            self.speed = speed
            self.dexterity = dexterity
            self.intelligence = intelligence
            self.armor = armor
            self.attack_mod = attack_mod
            self.spell_mod = spell_mod

    # Character Classes
    class FIGHTER(STATS):
        def __init__(self,name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod):
            STATS.__init__(name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod)
            name = ' '
            HPmax = 50
            Manamax = 0
            strength = 30
            speed = 60
            intelligence = 50
            armor = 0
            # increased unarmed damage

    class KNIGHT(STATS):
        def __init__(self,name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod):
            STATS.__init__(name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod)
            name = ' '
            HPmax = 50
            Manamax = 10
            strength = 40
            speed = 30
            intelligence = 50
            armor = 0
            # increased heavy meele damage
            
    class HUNTER(STATS):
        def __init__(self,name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod):
            STATS.__init__(name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod)
            name = ' '
            HPmax = 50
            Manamax = 20
            strength = 20
            speed = 50
            intelligence = 50
            armor = 0
            # increased ranged damage

    class WARLOCK(STATS):
        def __init__(self,name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod):
            STATS.__init__(name,HPmax,Manamax,strength,speed,dexterity,intelligence,armor,attack_mod,spell_mod)
            name = ' '
            HPmax = 50
            Manamax = 50
            strength = 10
            speed = 30
            intelligence = 50
            armor = 0
            # increased magic damage

            spell_mod = 1.5

    
    if characterclass == FIGHTER:
        player1 = FIGHTER()
        player1.name = name
    if characterclass == KNIGHT:
        player1 = KNIGHT()
        player1.name = name
    if characterclass == HUNTER:
        player1 = HUNTER()
        player1.name = name
    if characterclass == WARLOCK:
        player1 = WARLOCK()
        player1.name = name

    return player1       