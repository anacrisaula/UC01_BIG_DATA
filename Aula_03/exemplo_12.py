#Altura e peso ideal con definição de sexo
h = float(input("Qual a sua altura: "))
s = int(input("Informe M - para masculino e F - para feminino"))
if s == "M" or s == "m":
    m = (72.7 * h) - 58
    print(f"O seu peso ideal é {m:.2f}")
elif s == "F" or s == "f":
    f = (62.1 * h) - 44.7
    print(f"O seu peso ideal é {f:.2f}")
else:
    print("Verifique o Sexo Informado")   