def fattoriale(a):
    if a < 0:
        return "Errore: fattoriale di numero negativo non definito."
    if a == 0:
        return 1
    
    risultato = 1
    for i in range(1, a + 1):
        risultato = risultato * i
    return risultato

numero = int(input())
print(fattoriale(numero))