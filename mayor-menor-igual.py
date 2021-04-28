numbers = input()
a, b = [int(x) for x in numbers.split()]

if a < b:
    print('<')
elif a == b:
    print('=')
else:
    print('>')
