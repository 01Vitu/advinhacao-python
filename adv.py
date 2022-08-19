import os
import random

numeroTentativas=1
numero=random.randrange(0,100)

os.system("cls")
tentativa=int(input("Digite um número: "))

while tentativa != numero:
    numeroTentativas+=1
    os.system("cls")
    if numero > tentativa:
        print("Errado número sorteado é maior")
    elif numero < tentativa:
        print("Errado O número sorteado é menor")
    
    tentativa=int(input("\nDigite um número: "))

os.system("cls")
print("Parabéns você acertou! O número sorteado é o",numero)
print("\nVocê precisou de",numeroTentativas,"tentativas para adivinhar.")