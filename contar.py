n = input()
inp = input()
array = [int(x) for x in inp.split()]
c = input()

n = int(n)
c = int(c)

respuestas = []


def comparar(x):
    contador = 0
    for i in range(0, n):
        if array[i] > x:
            contador = contador + 1
    return contador


# Pedir consultas
for i in range(0, c):
    x = input()
    x = int(x)
    res = comparar(x)
    respuestas.append(res)


# Mostrar resultados
for i in range(0, c):
    print(respuestas[i])
