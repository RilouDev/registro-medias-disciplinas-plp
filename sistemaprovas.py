#Inicialização
cont = [0, 0, 0, 0]  # Contadores para cada disciplina
soma = [0, 0, 0, 0]  # Somas para cada disciplina
total_alunos = 0

while True:
    print( "+----------------------------------------------------------------+")
    print( "| Escolha sua disciplina:                                        |")
    print( "|                                                                |")
    print( "| [1] - Cálculo de uma variável                                  |")
    print( "| [2] - Bases de programação                                     |")
    print( "| [3] - Modelagem para novos negócios                            |")
    print( "| [4] - Paradigmas de linguagem de programação                   |")
    print( "|                                                                |")
    print( "+----------------------------------------------------------------+")

    opcao = int(input("Qual a sua escolha?"))

    if opcao < 1 or opcao > 4:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        continue

    media = float(input("Digite a média do aluno: "))
    
    cont[opcao - 1] += 1 #Incrementa o contador da disciplina escolhida
    soma[opcao - 1] += media #Soma a média do aluno à média informada para posterior calculo
    total_alunos += 1 #Incrementa o contador total de alunos

    continuar = input("Deseja continuar? (s/n): ").lower()
    if continuar != 's':
        break

#Relátorio
disciplinas = [
    "Cálculo de uma variável",
    "Bases de programação",
    "Modelagem para novos negócios",
    "Paradigmas de linguagem de programação"
]
print("\nRelatório de Médias por Disciplina:")
for i in range(4):
    mediafinal = soma[i] / cont[i] if cont[i] > 0 else 0 #Evita divisão por zero, caso não haja alunos em uma disciplina
    print(f"{disciplinas[i]}:") 
    print(f"total de alunos: {cont[i]}")
    print(f"Média da disciplina: {mediafinal:.2f}\n")

print(f"Total de alunos: {total_alunos}")
print(f"Disciplina com maior adesão: {disciplinas[cont.index(max(cont))]}") # max(cont): encontra o maior número de alunos | index: descobre a posição
