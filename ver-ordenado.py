n = input()
array = input()

a = [int(x) for x in array.split()]
n = int(n)

flag = True

for x in range(1, n):
    if a[x] < a[x-1]:
        flag = False
        print('Desordenado')
        break

if flag == True:
    print('Ordenado')
