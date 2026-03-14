Nota1 = float(input("Digite a nota 1: "))
Nota2 = float(input("Digite a nota 2: "))
Nota3 = float(input("Digite a nota 3: "))

media = (Nota1+Nota2+Nota3) / 3
print('Média:', media)

if media>= 6:
    print("Aprovado")
else:
    print("Reprovado")
