x = [10, 20]
print(x)

print(x[0])

x = [10, 20, 30]
print(x[-1])

x = [1, 2]
print(x)

x[0] = 22
print(x)

# empty list
my_list = []

my_list = [101, 20, 10, 50, 60]
for item in my_list:
    print(item)

my_list = ['Spoon', 'Fork', 'Knife']
for item in my_list:
    print(item)

my_list = [[2, 3], [4, 3], [6, 7]]
for item in my_list:
    print(item)

my_list = [101, 20, 10, 50, 60]
for index in range(len(my_list)):
    print(my_list[index])

for index, value in enumerate(my_list):
    print(index, value)