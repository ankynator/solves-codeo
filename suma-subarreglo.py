n = input()
input_array = input()
array = [int(x) for x in input_array.split()]
c = input()

n = int(n)
c = int(c)

outputs = []


def sumar(pq):
    d = pq[1] - pq[0]
    res = 0
    i = pq[0]
    while d >= 0:
        res = res + array[i]
        i = i+1
        d = d-1

    return res


for i in range(0, c):
    response = 0
    input_pq = input()
    pq = [int(r) for r in input_pq.split()]
    response = sumar(pq)
    outputs.append(response)

for k in range(0, c):
    print(outputs[k])
