lista = []
for i in range(10):
    y = int(input())
    lista.append(y)
    
numero_da_contare = int(input("Inserisci il numero da contare: "))
conteggio = lista.count(numero_da_contare)
print(conteggio)