#Projeto: Satisfação do Atendimento.

# 1-Contador/Ter controle da repetição e usar o resultado ao final do código.
excelente = 0
bom = 0
ruim = 0

# 2-Base/Comando para criar a repetição e solicitar os dados do usuário. 
for entrevistado in range(1, 51):
    nome = input("\nDigite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nEscolha uma avaliação:")
    print("1 -- Excelente")
    print("2 -- Bom")
    print("3 -- Ruim\n")

# 3-Contagem das opniões dos clientes.
    opiniao = int(input("Digite sua opinião: "))

#Nesse trecho se o usuário escolher "excelente" ele ira guarda caso contrario,
#ele ira guarda a avaliação "ruim".
    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    else:
        ruim += 1

# 4-Nessa etapa e o final do código, mostrando a quantidade de avaliações "excelente" e "ruim".  
print("\nResultado da avaliação dos clientes.")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas BOM:", bom)
print("Quantidade de respostas RUIM:", ruim)