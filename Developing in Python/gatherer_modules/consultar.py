import os
import gatherer
import _sqlite3
from datetime import date


def busca_pessoa():
    os.system('cls')

    print("Digite o nome da pessoa que deseja pesquisar: ")
    nome_pessoa = input(">: ").strip().upper()

    con = _sqlite3.connect("gatherer_database\\database.db")
    cur = con.cursor()

    sql = f"""
    SELECT nome, data_nascimento, sexo, cpf, estado, cidade
    FROM pessoas
    WHERE nome LIKE '%{nome_pessoa}%'"""

    cur.execute(sql)
    data = cur.fetchall()

    if not data:
        opt = input("Não foram encontrados resultados! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()
    else:
        # new_lista = [item for t in data for item in t]
        for i in range(len(data)):
            nome_db, data_nascimento_db, sexo_db, cpf_db, estado_db, cidade_db = data[i]
            ano, mes, dia = data_nascimento_db.split('-')
            print(f"NOME               = {nome_db}.")
            print(f"SEXO               = {sexo_db}.")
            print(f"CPF                = {cpf_db}. ")
            print(f"ESTADO/CIDADE      = {estado_db}/{cidade_db}.")
            print(f"DATA DE NASCIMENTO = {dia}/{mes}/{ano}.\n" + 50*"-")
    con.close()
    out = input("Pressione uma tecla para voltar ao menu: ")
    gatherer.main()


def lista_pessoa_estado():
    os.system('cls')

    print("Digite o nome do estado a ser escaneado: ")
    nome_estado = input(">: ").strip().upper()

    con = _sqlite3.connect("gatherer_database\\database.db")
    cur = con.cursor()

    sql = f"""
    SELECT nome, data_nascimento, sexo, cpf, estado, cidade
    FROM pessoas
    WHERE '{nome_estado}' = estado"""

    cur.execute(sql)
    data = cur.fetchall()

    if not data:
        opt = input("Estado não encontrado ou não há pessoas cadastradas nele! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()
    else:

        for i in range(len(data)):
            nome_db, data_nascimento_db, sexo_db, cpf_db, estado_db, cidade_db = data[i]
            ano, mes, dia = data_nascimento_db.split('-')
            print(f"NOME               = {nome_db}.")
            print(f"SEXO               = {sexo_db}.")
            print(f"CPF                = {cpf_db}. ")
            print(f"ESTADO/CIDADE      = {estado_db}/{cidade_db}.")
            print(f"DATA DE NASCIMENTO = {dia}/{mes}/{ano}.\n" + 50 * "-")
    con.close()
    opt = input("Pressione uma tecla para voltar ao menu: ")
    gatherer.main()


def lista_pessoa_cidade():
    os.system('cls')
    print("Digite o nome do estado: ")
    nome_estado = input(">: ").strip().upper()
    print("Digite o nome da cidade: ")
    nome_cidade = input(">: ").strip().upper()

    con = _sqlite3.connect("gatherer_database\\database.db")
    cur = con.cursor()

    sql = f"""
    SELECT nome, data_nascimento, sexo, cpf, estado, cidade
    FROM pessoas
    WHERE '{nome_estado}' = estado AND '{nome_cidade}' = cidade"""

    cur.execute(sql)
    data = cur.fetchall()

    if not data:
        opt = input("Estado e cidade não encontrada, ou não há pessoas cadastradas neste! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()
    else:
        for i in range(len(data)):
            nome_db, data_nascimento_db, sexo_db, cpf_db, estado_db, cidade_db = data[i]
            ano, mes, dia = data_nascimento_db.split('-')
            print(f"NOME               = {nome_db}.")
            print(f"SEXO               = {sexo_db}.")
            print(f"CPF                = {cpf_db}. ")
            print(f"ESTADO/CIDADE      = {estado_db}/{cidade_db}.")
            print(f"DATA DE NASCIMENTO = {dia}/{mes}/{ano}.\n" + 50 * "-")
    con.close()
    out = input("Pressione uma tecla para voltar ao menu: ")
    gatherer.main()


def gerar_relatorio():
    os.system('cls')

    con = _sqlite3.connect("gatherer_database\\database.db")
    cur = con.cursor()

    sql = f"""
    SELECT data_nascimento, sexo
    FROM pessoas"""

    cur.execute(sql)
    data = cur.fetchall()

    if not data:
        opt = input("Não há dados a serem mostrados! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()

    datas_db = []
    data_nascimento = []

    homens = 0
    mulheres = 0
    zero_cinco = 0
    seis_dez = 0
    onze_vinte = 0
    vinteum_quaren = 0
    quarum_sess = 0
    acimasess = 0

    for i in range(len(data)):
        for j in data[i]:
            datas_db.append(j)

    for i in datas_db:
        if i == 'F':
            mulheres += 1
        elif i == 'M':
            homens += 1
        else:
            data_nascimento.append(i)

    for i in data_nascimento:
        ano, mes, dia = int(i[0:4]), int(i[5:7]), int(i[8:10])
        data = date(ano, mes, dia)
        hoje = date.today()
        idade = hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))
        if idade <= 5:
            zero_cinco += 1
        elif 6 <= idade <= 10:
            seis_dez += 1
        elif 11 <= idade <= 20:
            onze_vinte += 1
        elif 21 <= idade <= 40:
            vinteum_quaren += 1
        elif 41 <= idade <= 60:
            quarum_sess += 1
        else:
            acimasess += 1

    print(f"Relatorio demográfico gerado com sucesso!!\n")
    print(f"Pessoas com idade entre 0 a 5:   {zero_cinco}")
    print(f"Pessoas com idade entre 6 a 10:  {seis_dez}")
    print(f"Pessoas com idade entre 11 a 20: {onze_vinte}")
    print(f"Pessoas com idade entre 21 a 40: {vinteum_quaren}")
    print(f"Pessoas com idade entre 41 a 60: {quarum_sess}")
    print(f"Pessoas com idade superior a 60: {acimasess}")
    print(f"Pessoas com o sexo feminino: {mulheres}")
    print(f"Pessoas com o sexo masculino: {homens}")
    opt = input("Pressione qualquer tecla para retornar ao menu: ")
    con.close()
    gatherer.main()





