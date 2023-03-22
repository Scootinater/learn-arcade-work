plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(c, end=' ')

print('\n')

for c in plain_text:
    print(ord(c), end=' ')

print('\n')

for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end=' ')