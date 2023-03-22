temperature = int(input("What's the temperature in Fahrenheit? "))
if temperature > 110:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature > 90:
    print('It is hot outside!')
elif temperature < 30:
    print("It's cold outside!")
else:
    print("It's not hot outside.")
print('Done!')