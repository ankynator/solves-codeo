n = input()
input_array = input()
array = [int(x) for x in input_array.split()]
n = int(n)

for i in range(1, n):
    array[i] = array[i] + array[i-1]

c = input()
c = int(c)
outputs = []

for i in range(0, c):
    response = 0
    input_pq = input()
    pq = [int(r) for r in input_pq.split()]
    p, q = pq[0], pq[1]

    if p == 0:
        response = array[q]
    else:
        response = array[q] - array[p-1]

    outputs.append(response)

for k in range(0, c):
    print(outputs[k])
