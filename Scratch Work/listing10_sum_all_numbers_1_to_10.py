# what is the value of sum
total = 0
for i in range(1, 101):
    total = total + i
print(total)

print('\n')

total = 0
for i in range(5):
    new_number = int(input('Enter a number: '))
    if new_number == 0:
        total += 1
print('You entered a total of', total, 'zeroes.')