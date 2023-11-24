#funçoes
# Aqui pegamos a linha que estão as colunas do arquivo
#2 Mostrar os principais principios ativos
#PRODUTO, PEGAR AS LINHAS, A QAUNTIDADE, PEGAR A TARJA

# Abrir o arquivo CSV
with open('TA_PRECO_MEDICAMENTO_GOV.csv', 'r') as arquivo:
    linhas = arquivo.readlines()

#função 3 em prints
def espacamento1():
    print("_" * 200)

def espacamento2():
    print("-" * 45)

def espacamento3():
    print(" " * 200)


# Pego a linha que está a coluna do arquivo
def linhaDasColunas():
    # Procuro a linha que contém as colunas
    linhaColunas = None
    for linha in linhas:
        if 'PRINCÍPIO ATIVO' in linha:
            if 'PRODUTO' in linha:
                if 'LABORATÓRIO' in linha:
                    linhaColunas = linhas.index(linha)
                    break
    return linhaColunas

numeroLinha = linhaDasColunas()
#print("A LINHA DAS COLUNAS É:", numeroLinha)

#funcao1, pegar as linhas e o nome das colunas

#mostrar as colunas
def nomeColunas():
    linha = linhas[numeroLinha].strip()  # pega linha correspondente ao número informado
    colunas = linha.split(',')  # divide a linha em uma lista de colunas

    nomes = []  #armazenar os nomes das colunas

    # Percorre as colunas e adiciona o número da linha e o nome da coluna à lista
    for i in range(len(colunas)):
        coluna = colunas[i].strip()
        if coluna != "" and coluna != "." and coluna != ",":
            nome = f"{i+1} {coluna}"
            nomes.append(nome)

    return '\n'.join(nomes)

#mostrar a quantidade linhas 
def qtdLinhas():
    qtd = 0
    for linha in linhas[numeroLinha+1:]:
        if linha.strip() != "" and linha.strip() != "." and linha.strip() != ",":
            qtd += 1
    return qtd


print("-------------------------------------")
#print("A QUANTIDADE LINHAS É :", qtdLinhas())#28893

 
#função 2
#mostrar percentual de remedios por tarjas
def mostrarPercentualTarjas():
    contadorTarjaPreta = 0
    contadorTarjaAmarela = 0
    contadorTarjaVermelha = 0
    contadorSemTarja = 0
    totalLinhas = 0

    for linha in linhas[numeroLinha + 1:]:
        if 'vermelha' in linha.lower():
            contadorTarjaVermelha += 1
        elif 'preta' in linha.lower():
            contadorTarjaPreta += 1
        elif 'amarela' in linha.lower():
            contadorTarjaAmarela += 1
        else:
            contadorSemTarja += 1

        totalLinhas += 1

    print("Total de tarjas pretas encontradas:", contadorTarjaPreta)
    print("Total de tarjas amarelas encontradas:", contadorTarjaAmarela)
    print("Total de tarjas vermelhas encontradas:", contadorTarjaVermelha)
    print("Total de linhas sem tarja encontradas:", contadorSemTarja)
  
    percentualPreta = (contadorTarjaPreta / totalLinhas) * 100
    percentualAmarela = (contadorTarjaAmarela / totalLinhas) * 100
    percentualVermelha = (contadorTarjaVermelha / totalLinhas) * 100
    percentualSemTarja = (contadorSemTarja / totalLinhas) * 100
    espacamento3()
    print("Percentual de tarjas pretas: {:.2f}%".format(percentualPreta))
    print("Percentual de tarjas amarelas: {:.2f}%".format(percentualAmarela))
    print("Percentual de tarjas vermelhas: {:.2f}%".format(percentualVermelha))
    print("Percentual de linhas sem tarja: {:.2f}%".format(percentualSemTarja))



#função 3
def removerAcentos(palavra):
    acentos = ['á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'î', 'ô', 'û', 'à', 'è', 'ì', 'ò', 'ù', 'ã', 'õ', 'ñ', 'ç', 'ü', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Â', 'Ê', 'Î', 'Ô', 'Û', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Ã', 'Õ', 'Ñ', 'Ç', 'Ü']
    semAcentos = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'o', 'n', 'c', 'u', 'A', 'E', 'I', 'O', 'U', 'A', 'E', 'I', 'O', 'U', 'A', 'E', 'I', 'O', 'U', 'A', 'O', 'N', 'C', 'U']

    for i in range(len(acentos)):
        palavra = palavra.replace(acentos[i], semAcentos[i])

    return palavra

def verificarNome(nome):
    nome = nome.replace(" ", "").replace(",", "").replace(".", "")  # Remover espaços em branco, vírgulas e pontos
    while len(nome) < 2 or nome == "":
        nome = removerAcentos(input("Digite um nome válido (pelo menos 2 caracteres): ").lower())
        nome = nome.replace(" ", "").replace(",", "").replace(".", "")  # Remover espaços em branco, vírgulas e pontos
    return nome


#realizar busca no arquivo

def realizarBuscaArquivo():
    nomeProcurado = verificarNome(removerAcentos(input("Digite o nome a ser procurado no arquivo: ").lower()))

    arquivoCsv = "TA_PRECO_MEDICAMENTO_GOV.csv"
    linhasPular = 66
    linhasEncontradas = []
    contador = 0  # Inicializar o contador

    with open(arquivoCsv, 'r') as arquivo:
        for _ in range(linhasPular):
            arquivo.readline()

        for linha in arquivo:
            linhaSemAcentos = removerAcentos(linha.lower())
            if nomeProcurado in linhaSemAcentos:
                contador += 1  # Incrementar o contador

                palavraDestaque = nomeProcurado.upper()
                linhaDestaque = linha.lower().replace(nomeProcurado, palavraDestaque)
                linhasEncontradas.append(linhaDestaque.strip())

    if contador == 0:
        espacamento3()
        print("A palavra não foi encontrada no arquivo.")
        espacamento3()
    else:
        for resultado in linhasEncontradas:
            print(resultado)
            espacamento2()

    return contador

#nomeProcurado = realizarBuscaArquivo()
#print(f"A palavra '{nomeProcurado}' foi encontrada {nomeProcurado} vez(es) no arquivo.")



#função 4
#calcular o preco de fábrica de um medicamento
def calcularPrecoFabrica():
    precoCusto = float(input("DIGITE O VALOR DO PREÇO DE CUSTO DO PRODUTO : "))

    while True:
        UF = input("DIGITE A UF PARA CALCULO DE ICMS\n\n AC, AL, AP, AM, BA, CE, DF\n ES, GO, MA, MT, MS, MG, PA\n PB, PR, PE, PI, RJ, RN, RS \n RO, RR SC, SP, SE, TO  \n\n")

        if len(UF) != 2 or UF.strip() == "":
            print("SIGLA INVÁLIDA")
        else:
            break

    # Verificar a alíquota de ICMS com base no estado
    if UF == "RJ":
        aliquotaICMS = 0.20
    elif UF in ["AM", "AP", "BA", "CE", "MA", "MG", "PB", "PI", "RR", "RN", "SE", "SP", "TO"]:
        aliquotaICMS = 0.18
    elif UF == "RO":
        aliquotaICMS = 0.175
    else:
        aliquotaICMS = 0.17

    # Calcular o preço de fábrica
    precoFabrica = precoCusto + (precoCusto * aliquotaICMS)
    print("                               ")
    print("O PREÇO DE FÁBRICA  É :", precoFabrica)
    print("                               ")



#função 5
def calcularModaPrincipiosAtivos():
    principiosAtivos = []
    

    # Extrair os princípios ativos
    for linha in linhas:
        colunas = linha.split(',')
        principiosAtivos.append(colunas[0])
    
    # Calcular a moda dos princípios ativos
    contadorPrincipiosAtivos = {}
    for principioAtivo in principiosAtivos:
        if principioAtivo in contadorPrincipiosAtivos:
            contadorPrincipiosAtivos[principioAtivo] += 1
        else:
            contadorPrincipiosAtivos[principioAtivo] = 1
    
    # Encontrar o princípio ativo mais comum
    principiosModa = []
    maxOcorrencias = 0
    for principioAtivo, ocorrencias in contadorPrincipiosAtivos.items():
        if ocorrencias > maxOcorrencias:
            principiosModa = [principioAtivo]
            maxOcorrencias = ocorrencias
        elif ocorrencias == maxOcorrencias:
            principiosModa.append(principioAtivo)
    
    # Imprimir o princípio ativo mais comum e a quantidade de vezes que ele se repete
    for principioAtivo in principiosModa:
     print("O PRINCIPIO ATIVO QUE MAIS SE REPETE NO ARQUIVO É O")
    
     print(principioAtivo)
     espacamento2()
    print("A QUANTIDADE DE VEZES QUE SE REPETE É ", maxOcorrencias, " VEZES")

#final função 5
def principaisLaboratorios():
    laboratorios = set()  # Conjunto para armazenar os laboratórios já adicionados
    principais_laboratorios = []

    for linha in linhas[numeroLinha+1:]:
        colunas = linha.split(',')

        if len(colunas) >= 3:
            laboratorio = colunas[2].strip()
            if laboratorio not in laboratorios:  # Verifica se o laboratório já foi adicionado
                laboratorios.add(laboratorio)  # Adiciona o laboratório ao conjunto
                principais_laboratorios.append(laboratorio)  # Adiciona o laboratório à lista de principais laboratórios

    return principais_laboratorios


def totalLaboratorios():
    laboratorios = principaisLaboratorios()
    return len(laboratorios)


 #print(" TOTAL DE LABORÁTORIOS :",totalLaboratorios())

def exibirLaboratorios():
    laboratorios = principaisLaboratorios()
    total= totalLaboratorios()
    #print("Principais laboratórios:")
    espacamento3()
   
    for i, laboratorio in enumerate(laboratorios, start=1):
        print(f"{i}. {laboratorio}")
        
   # print(f"Total de laboratórios: {total}")

   #exibirLaboratorios()



def criarArquivoInformacoes():
    with open("informacoes.txt", "w") as arquivo:
        arquivo.write("Nome das colunas:\n")
        arquivo.write(nomeColunas())
    print("Informações salvas com sucesso no arquivo 'informacoes.txt'!")
    
criarArquivoInformacoes()
