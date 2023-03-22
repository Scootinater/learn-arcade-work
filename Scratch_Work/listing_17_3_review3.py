'''
Work in progress... still stuck in infinite loop
'''

class Monster():
    def __init__(self):
        self.name = 'Spiky'
        self.health = 100

    def decrease_health(self, damage):
        damage = self.health - damage
        if self.health == 0:
            print(self.name, 'has perished... so long and thanks for all the fish!')

enemy = Monster()
done = False
def main():
    done = False
    while not done:
        enemy.decrease_health(10)
        print(enemy.name, 'has sustained damage!')
        if done:
            break

main()
