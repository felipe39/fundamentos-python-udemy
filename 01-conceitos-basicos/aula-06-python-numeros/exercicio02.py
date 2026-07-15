#Entrada do preço do produto e do desconto
preco = float((input("Digite o preço do produto: R$")))
desconto = float(input("Digite a porcentagem de desconto (%): "))

#Calculo do produto com desconto
valor_desconto = preco * (desconto / 100)
valor_final = preco - valor_desconto

#Saída do preço sem o desconto, do desconto aplicado e do valor final
print("\nResultado Final")
print("-" * 20)
print("Preço original: R$ ", round(preco, 2))
print("Desconto aplicado: ", desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Valor final: R$", round(valor_final, 2))

input("Digite ENTER para sair")



