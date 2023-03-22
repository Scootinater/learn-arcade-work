'''
Practice writing code
'''
newline = '\n'
for i in range(10):
    print('Hi')
print(newline)

for i in range(5):
    print('Hello')
print('There')
print(newline)

for i in range(5):
    print("Hello")
    print('There')
print(newline)

for i in range(10):
    print(i)
print(newline)

for i in range(1, 11):
    print(i)
print(newline)

for i in range(10):
    print(i + 1)
print(newline)

for i in range(2, 12, 2):
    print(i)
print(newline)

for i in range(5):
    print((i + 1) * 2)
print(newline)

for i in range(10, 1, -1):
    print(i)
print(newline)

for items in [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8]:
    print(items)
print(newline)

a = 0
for i in range(10):
    a = a + 1
print(a)
print(newline)

a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)
print(newline)

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)
print(newline)

total = 0
for i in range(1, 101):
    total = total + i
print(total)