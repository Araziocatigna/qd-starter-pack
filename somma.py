num1 = int(input("Inserisci il primo numero:  "))
num2 = int(input("Inserisci il secondo numero:  "))
def somma (num1: int, num2: int) -> int:
    return num1 + num2

print (f'La somma di {num1} e {num2} è: {somma(num1, num2)}')