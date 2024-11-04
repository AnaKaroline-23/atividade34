#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.
lista_num = []

for i in range(1,6):
    num = int(input(f"digite o numero {i}:  "))
    lista_num.append(num)
print(lista_num)
for item, p in enumerate(lista_num):
    print("o numero",p, "é o",item + 1, "°", "da lista!")


