def trova_massimo(lista):
    if not lista:
        return None  # Gestisce il caso di una lista vuota
        
    massimo = lista[0]
    for x in lista:
        if x > massimo:
            massimo = x
    return massimo

mia_lista = [5, 2, 9, 1, 7]
print(trova_massimo(mia_lista))