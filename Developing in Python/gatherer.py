import time
import os
from gatherer_modules import inserir, create_db, consultar, remover


def main():
    create_db.create_database()
    while True:
        os.system('cls')
        print("*" * 10, "Gatherer", "*" * 10)
        print("*" * 30)
        print("1 - Cadastrar um Estado")
        print("2 - Cadastrar uma Cidade")
        print("3 - Cadastrar uma Pessoa")
        print("4 - Consultar uma Pessoa")
        print("5 - Consultar pessoa por Estado")
        print("6 - Consultar pessoa por Cidade")
        print("7 - Excluir uma pessoa")
        print("8 - Gerar relatório demográfico")
        print("9 - Sair do programa")
        opt = input(">: ")
        if opt == '1':
            inserir.inserir_estado()
            break
        elif opt == '2':
            inserir.inserir_cidade_estado()
            break
        elif opt == '3':
            inserir.inserir_pessoa()
            break
        elif opt == '4':
            consultar.busca_pessoa()
            break
        elif opt == '5':
            consultar.lista_pessoa_estado()
            break
        elif opt == '6':
            consultar.lista_pessoa_cidade()
            break
        elif opt == '7':
            remover.remover_pessoa()
            break
        elif opt == '8':
            consultar.gerar_relatorio()
            break
        elif opt == '9':
            print("Saindo do programa!")
            exit(0)
        else:
            print("Comando não reconhecido!")
            time.sleep(2)
            main()


if __name__ == '__main__':
    main()

