n = input()
n = int(n)
array_input = input()

array = [int(x) for x in array_input.split()]
middles = []


for i in range(1, n):
    array[i] = array[i] + array[i-1]

for i in range(1, n):
    if array[i-1] > 0 and (array[n - 1] - array[i - 1]) < 0:
        middles.append(i)


if middles:
    print(middles[0])
else:
    print('Impossible')
