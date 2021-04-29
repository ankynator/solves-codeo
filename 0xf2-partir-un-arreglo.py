n = input()
n = int(n)
array_input = input()

array = [int(x) for x in array_input.split()]
left = array
right = array[::-1]

b_left = []
b_right = []

j = n - 1
for i in range(0, n):
    if i == 0:
        left[i] = array[i]
    else:
        left[i] = left[i] + left[i-1]
        right[i] = right[i] + right[i-1]

    if left[i] > 0:
        b_left.append(i)
    if right[i] < 0:
        b_right.append(j)
    j -= 1

b_right = b_right[::-1]

if b_right and b_left:
    c = 0
    while c < len(b_right):
        if b_right[c] in b_left:
            print(b_right[c])
            break
        else:
            print('Impossible')
        c += 1
else:
    print('Impossible')
