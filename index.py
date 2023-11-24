
import funcoes

#PRODUTO, PEGAR AS LINHAS, A QAUNTIDADE, PEGAR A TARJA

# Abrir o arquivo CSV
with open('TA_PRECO_MEDICAMENTO_GOV.csv', 'r') as arquivo:
    linhas = arquivo.readlines()



while True:
    valor = int(input("DIGITE A OPÇÃO DESEJADA:\n\n0 - SAIR\n1 - MOSTRAR A QUANTIDADE DE LINHAS E OS NOMES DAS COLUNAS DO ARQUIVO\n2 - MOSTRAR PERCENTUAL DE PRODUTOS POR TARJA \n3 - PROCURAR POR UM NOME NO ARQUIVO \n4 - CALCULAR O PREÇO DE FÁBRICA DE UM MEDICAMENTO \n5 - CALCULAR A MODA DE UM PRINCÍPIO ATIVO\n6 - MOSTRAR LABORÁTORIOS\n7 - CRIAR ARQUIVO TXT COM AS COLUNAS DO ARQUIVO\n\n----> "))

    if valor == 0:
        print("-------------")
        print("SAINDO")
        print("-------------")
        break

    if valor == 1:
        funcoes.espacamento3()
        print("A QUANTIDADE LINHAS DO ARQUIVO É:", funcoes.qtdLinhas())#28893
        funcoes.espacamento3()
        print("O NOME DAS COLUNAS É:\n\n",funcoes.nomeColunas())
        funcoes.espacamento3()
        
    elif valor == 2:
       funcoes.mostrarPercentualTarjas()
    elif valor == 3:
     funcoes.realizarBuscaArquivo()
    elif valor == 4:
        funcoes.calcularPrecoFabrica()
    elif valor == 5:
         funcoes.espacamento3()
         funcoes.calcularModaPrincipiosAtivos()
         funcoes.espacamento3()
    elif valor == 6:
        funcoes.exibirLaboratorios()
        funcoes.espacamento2()
        print(" TOTAL DE LABORÁTORIOS :",funcoes.totalLaboratorios() - 1)
        funcoes.espacamento2()
    elif valor == 7:
          funcoes.criarArquivoInformacoes()
    else:
     print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
