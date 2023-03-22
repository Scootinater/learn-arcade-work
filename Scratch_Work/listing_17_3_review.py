class Cat():
    def __init__(self):
        self.name = ''
        self.color = ''
        self.weight = 0

    def meow(self):
        print('Meow!')

cat1 = Cat()
cat1.name = "Midnight"
cat1.color = "black"
cat1.weight = 10

cat1.meow()
print('Hello! My name is,', cat1.name + '.', 'I am a', cat1.color, 'cat. I only weigh',
       str(cat1.weight) + '!',end=" "), cat1.meow()