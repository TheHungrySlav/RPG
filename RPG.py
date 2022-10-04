# RPG game

def RPG():
    # Functions
    import random
    from Weapons_RPG import Weapons
    import battle
    from Character_creator import creator

    # Create character
    name = input('Youre finally awake, what is your name?: ')
    print('Classes:')
    print('Fighter - A master of unarmed combat whose speed is unmatched')
    print('Knight - Trained in Heavy meele weapons, has the strength of an ox')
    print('Hunter - Proficient in all ranged weapons')
    print('Warlock - knowledgable in all forms of magic')
    character_class = input('What is your class?: ').upper()
    # background = input('What is your background?: ')
    player = creator(name,character_class)

    print(player)

RPG()