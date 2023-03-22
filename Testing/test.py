class Monster():
    def __init__(self, name, health):
        self.name = name
        self.health = health

monster1 = Monster("Punk", 100)

print(monster1.name, 'has health of', monster1.health)