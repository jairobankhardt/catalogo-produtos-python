import json
import os.path
import sys


def obter_dados():
    """
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários,
    onde cada dicionário representa um produto.
    """
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados


def listar_categorias(dados):
    """
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    """
    categorias = []
    for i in range(len(dados)):
        if dados[i]["categoria"] not in categorias:
            categorias.append(dados[i]["categoria"])
    return categorias


def listar_por_categoria(dados, categoria):
    """
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    """
    produtos = []
    for i in range(len(dados)):
        if dados[i]["categoria"] == categoria:
            produtos.append(dados[i])
    return produtos
    

def produto_mais_caro(dados, categoria):
    """
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    """
    lista_produtos_ordenados = sorted(listar_por_categoria(dados, categoria), key=lambda k: float(k['preco']),
                                      reverse=True)
    return lista_produtos_ordenados[0]


def produto_mais_barato(dados, categoria):
    """
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    """
    lista_produtos_ordenados = sorted(listar_por_categoria(dados, categoria), key=lambda k: float(k['preco']))
    return lista_produtos_ordenados[0]


def top_10_caros(dados):
    """
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    """
    lista_10_caros = sorted(dados, key=lambda k: float(k['preco']), reverse=True)
    return lista_10_caros[:10]


def top_10_baratos(dados):
    """
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    """
    lista_10_baratos = sorted(dados, key=lambda k: float(k['preco']))
    return lista_10_baratos[:10]


def menu(dados):
    """
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo.
    O loop encerra quando a opção do usuário for 0.
    """
    opcao = 1
    while opcao != "0":
        exibir_menu()
        opcao = input("\nEscolha uma opção do menu: ")
        if not verifica_valor_digitado(opcao):
            continue
        if opcao == "1":  # 1. Listar categorias
            lista_categorias_ordenada = sorted(listar_categorias(dados))
            exibir_categorias(lista_categorias_ordenada)
        elif opcao == "2":  # 2. Listar produtos de uma categoria
            opcao_categoria = 1
            while opcao_categoria != "0":
                lista_categorias_ordenada = sorted(listar_categorias(dados))
                exibir_categorias(lista_categorias_ordenada)
                opcao_categoria = input("Digite o número da categoria para exibir seus produtos "
                                        "(0 para voltar ao menu principal): ")
                if not verifica_valor_digitado(opcao_categoria, len(lista_categorias_ordenada)):
                    continuar_com_enter()
                    continue
                categoria = lista_categorias_ordenada[int(opcao_categoria) - 1]
                lista_produtos_da_categoria = listar_por_categoria(dados, categoria)
                exibir_produtos_da_categoria(lista_produtos_da_categoria, categoria)
                break
        elif opcao == "3":  # 3. Produto mais caro por categoria
            opcao_categoria = 1
            while opcao_categoria != "0":
                lista_categorias_ordenada = sorted(listar_categorias(dados))
                exibir_categorias(lista_categorias_ordenada)
                opcao_categoria = input("Digite o número da categoria para exibir seu produto mais caro "
                                        "(0 para voltar ao menu principal): ")
                if not verifica_valor_digitado(opcao_categoria, len(lista_categorias_ordenada)):
                    continuar_com_enter()
                    continue
                categoria = lista_categorias_ordenada[int(opcao_categoria) - 1]
                mais_caro = produto_mais_caro(dados, categoria)
                print(f'\nO produto mais caro de {categoria} é {mais_caro["id"]} '
                      f'(R$ {mais_caro["preco"].replace(".", ",")}).\n')
                break
        elif opcao == "4":  # 4. Produto mais barato por categoria
            opcao_categoria = 1
            while opcao_categoria != "0":
                lista_categorias_ordenada = sorted(listar_categorias(dados))
                exibir_categorias(lista_categorias_ordenada)
                opcao_categoria = input("Digite o número da categoria para exibir seu produto mais barato "
                                        "(0 para voltar ao menu principal): ")
                if not verifica_valor_digitado(opcao_categoria, len(lista_categorias_ordenada)):
                    continuar_com_enter()
                    continue
                categoria = lista_categorias_ordenada[int(opcao_categoria) - 1]
                mais_barato = produto_mais_barato(dados, categoria)
                print(
                    f'\nO produto mais barato de {categoria} é {mais_barato["id"]} '
                    f'(R$ {mais_barato["preco"].replace(".", ",")}).\n')
                break
        elif opcao == "5":  # 5. Top 10 produtos mais caros
            print("\n> > >  OS 10 PRODUTOS MAIS CAROS  < < <\n")
            for k, v in enumerate(top_10_caros(dados)):
                print(f'{k + 1:02} - {v["id"]} (R$ {v["preco"].replace(".", ",")}) de {v["categoria"]}')
        elif opcao == "6":  # 6. Top 10 produtos mais baratos
            print("\n> > >  OS 10 PRODUTOS MAIS BARATOS  < < <\n")
            for k, v in enumerate(top_10_baratos(dados)):
                print(f'{k + 1:02} - {v["id"]} (R$ {v["preco"].replace(".", ",")}) de {v["categoria"]}')

    print("\n\n*** Programa finalizado. ***")


# %%%%% FUNÇÕES AUXILIARES (by Jairo)

def exibir_menu():
    """
    Imprime na tela as opções do menu.
    """
    print("\n=#=#=#=#=#=#=#=#=#=  M E N U  =#=#=#=#=#=#=#=#=#=\n")
    numero_espacos = 3
    print(f'{" ":{numero_espacos}}{"1. Listar categorias"}')
    print(f'{" ":{numero_espacos}}{"2. Listar produtos de uma categoria"}')
    print(f'{" ":{numero_espacos}}{"3. Produto mais caro por categoria"}')
    print(f'{" ":{numero_espacos}}{"4. Produto mais barato por categoria"}')
    print(f'{" ":{numero_espacos}}{"5. Top 10 produtos mais caros"}')
    print(f'{" ":{numero_espacos}}{"6. Top 10 produtos mais baratos"}')
    print(f'{" ":{numero_espacos}}{"0. Sair":>5}')


def verifica_valor_digitado(opcao, limite=6):
    """
    Verifica se a opção digitida é válida.
    :param opcao: Opção digitada pelo usuário.
    :param limite: Valor limite de opções.
    :return: Booleano da verificação.
    """
    if not opcao.isdigit():
        print("\n##### ERRO: VOCÊ NÃO DIGITOU UM NÚMERO INTEIRO. TENTE NOVAMENTE\n")
        return False
    opcao = int(opcao)
    if 0 < opcao > limite:
        print("\n##### ERRO: OPÇÃO INVÁLIDA. TENTE NOVAMENTE\n")
        return False
    return True


def continuar_com_enter():
    """
    Pausa o script até o usuário apertar a tecla <Enter>
    """
    input("Digite <enter> para continuar. ")


def exibir_categorias(lista_categorias):
    """
    Exibe na tela todas as categorias.
    :param lista_categorias: Lista de categorias
    """
    print("\n> > >  L I S T A R   C A T E G O R I A S  < < <\n")
    for k, v in enumerate(lista_categorias):
        print(f'{k + 1:02} - {v}')
    print()


def exibir_produtos_da_categoria(lista_produtos, categoria):
    """
    Exibe na tela os produtos da categoria escolhida pelo usuário.
    :param lista_produtos: Lista de produtos da categoria escolhida.
    :param categoria: Categoria escolhida
    """
    print(f"\n> > >  PRODUTOS DE {categoria.upper()}  < < <\n")
    lista_produtos.sort(key=lambda p: float(p["preco"]))
    for k, v in enumerate(lista_produtos):
        print(f'{k + 1:02} - {v["id"]} (R$ {v["preco"].replace(".", ",")})')


#   P R O G R A M A   P R I N C I P A L

d = obter_dados()
menu(d)
