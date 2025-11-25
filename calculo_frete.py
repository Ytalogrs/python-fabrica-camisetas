def escolha_modelo():   #Função para escolher modelo
    while True:
        print("Entre com o modelo desejado")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa")
        print("MLE - Manga Longa Com Estampa")
        modelo = input(">>").strip().upper()    #Modelo solicitado, com a reposta sem espaços e em letra maiúscula
        if modelo in ("MCS", "MLS", "MCE", "MLE"): #Validação da reposta dentro das opções
            return modelo
        else:
            print("Escolha inválida! Entre com o modelo novamente\n")

def num_camisetas(modelo):  #Função para escolher a quantidade
    while True:
        try:
            quantidade = int(input("Entre com o número de camisetas: "))
        except ValueError:
            print("Valor inválido! Digite um número inteiro")
            continue
        if quantidade <= 0:      #Validação para não usar valor igual/menor que zero
            print("Quantidade deve ser maior que zero.\n")
            continue

        if quantidade > 20000:   #Validação para não usar valor maior que 20000
            print("Não aceitamos tantas camisetas de uma vez.")
            print("Por favor, entre com o número de camisetas novamente.\n")
            continue

        #Tabela de valores unitário de acordo com cada modelo
        if modelo == "MCS":
            valorUnit = 1.80
        elif modelo == "MLS":
            valorUnit = 2.10
        elif modelo == "MCE":
            valorUnit = 2.90
        else:
            valorUnit = 3.20

        #Conta para conseguir o valor bruto do pedido solicitado
        valorBruto = quantidade * valorUnit

        #Tabela para validar descontos de acordo com a quantidade de peças solicitadas
        if 20 <= quantidade < 200:
            valorTotal = valorBruto * 0.95
        elif 200 <= quantidade < 2000:
            valorTotal = valorBruto * 0.93
        elif 2000 <= quantidade < 20000:
            valorTotal = valorBruto * 0.88
        else:
            valorTotal = valorBruto

        return quantidade, valorUnit, valorBruto, valorTotal

def frete_camisas():  #Função referente ao frete
    while True:
        print("\nEscolha o tipo de frete:")
        print("1 - Frete por transportadora - R$100.00")
        print("2 - Frete por Sedex - R$200.00")
        print("0 - Retirar pedido na fábrica - R$0.00")
        try:
            frete = int(input(">>"))    #Teste de possibilidade de erros
        except ValueError:
            print("Valor inválido! Digite 0, 1 ou 2.\n")
            continue

        #Tabela para valores de frete
        if frete == 0:
            valorFrete = 0.00
        elif frete == 1:
            valorFrete = 100.00
        elif frete == 2:
            valorFrete = 200.00

        if frete in (0, 1, 2):  #Validação de valores corretos inseridos
            return frete, valorFrete
        else:
            print("Escolha inválida! Digite 0, 1 ou 2. \n")
        continue

print("Bem-vindo a Fábrica de Camisetas do Ytalo Gabriel \n")

#Chamada pelas funções
modelo = escolha_modelo()
quantidade, valorUnit, valorBruto, valorTotal = num_camisetas(modelo)
frete, valorFrete = frete_camisas()
total = valorTotal + valorFrete   #Conta para receber o valor total da compra
qtdDesconto= valorTotal / valorUnit #Conta para receber o valor da quantidade com desconto

print(f"Total: R${total:.2f} (Modelo: {valorUnit:.2f} * Quantidade(com desconto): {qtdDesconto:.0f} + frete: {valorFrete:.2f})")
