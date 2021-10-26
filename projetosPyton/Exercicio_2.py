comparador = 0
num1 = 0
num2 = 1
numero = int(input("digite um numero"))
while comparador < numero:
    num1 = comparador + num2
    comparador = num2
    num2 = num1
if comparador == numero:
    print("numero esta na sequencia de fibonacci")
else:
    print("numero nao esta na sequencia de fibonacci")