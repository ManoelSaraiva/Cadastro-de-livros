"""
main
"""
import os

import claLivrosBD

livro = claLivrosBD.LivrosBD('LivrosBD.db3')

opcao = 0


def tela_inicial():
    print(
        '========================================================================================================='
    )
    print(
        '==================================== Cadastro de Livros ================================================='
    )
    print(
        '========================================================================================================='
    )
    print('')
    print('Digite uma opção:')
    print('')
    print('1 - Cadastrar')
    print('2 - Editar')
    print('3 - Excluir')
    print('4 - Listar')
    print('5 - Buscar')
    print('6 - Sair')
    print('')
    return int(input('Digite sua opção: '))


def tela_cadastro():
    print(
        '========================================================================================================='
    )
    print(
        '====================================      Cadastrar     ================================================='
    )
    print(
        '========================================================================================================='
    )
    titulo = input('Digite o titulo do livro: ')
    print('')
    autor = input('Digite o autor do livro: ')
    print('')
    editora = input('Digite a editora do livro: ')
    print('')
    edicao = input('Digite o edicao do livro: ')
    print('')
    ano_publ = input('Digite o ano de publicação: ')
    print('')
    local = input('Digite o local onde esta guardado: ')
    print('')
    data_compra = input('Digite a data de compra: ')
    livro.inserir(titulo, autor, editora, edicao, ano_publ, local, data_compra)


while opcao != 6:
    opcao = tela_inicial()

    if opcao == 1:
        print('1-')
        os.system('clear') or None
        tela_cadastro()

    elif opcao == 2:
        print('2-')
    elif opcao == 3:
        print('3')
    elif opcao == 4:
        livro.listar()
    elif opcao == 5:
        print('5')
    else:
        print('Bye')
