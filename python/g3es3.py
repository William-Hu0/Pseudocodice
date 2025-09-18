X = 0
A = 0
while True:
    Y = int(input("Inserisci un numero: "))
    A += Y
    if Y != 0:
        X += 1
    else:
        break
if X > 0:
    media = A / X
    print(f"La media dei numeri inseriti è: {media}")
else:
    print("Non è stato inserito alcun numero valido per il calcolo della media.")