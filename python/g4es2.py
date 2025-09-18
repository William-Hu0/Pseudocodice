lista = []
for x in range(5):
    x = int(input())
    lista.append(x)
lista.sort()
print(lista[0], lista[-1])