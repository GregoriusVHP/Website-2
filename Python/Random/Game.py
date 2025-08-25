import time

class Character:
    health = 10
    attack = 5
    defence = 5
    def __init__(self, name, weapon, item):
        self.name = name
        self.weapon = weapon
        self.item = item

'''class creep:
    health = 5
    attack = 2
    defence = 2
    name = "Creep"
    def __init__(self, name):
        self.name = name '''

p1 = Character("Nara", "Sword", "Potion")
'''c = creep.name()'''
print(f"Nama: {p1.name}.\nSenjata: {p1.weapon}\n Barang: {p1.item}")