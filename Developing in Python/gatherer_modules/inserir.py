import _sqlite3
import os
from datetime import datetime
import gatherer


def inserir_estado():
    os.system('cls')
    print("Insira o nome do estado a ser cadastrado: ")
    nome_estado = input(">: ").strip().upper()

    con = _sqlite3.connect("gatherer_database\\database.db")
    cur = con.cursor()

    try:
        sql = f"""
            INSERT INTO estados (nome)
            VALUES('{nome_estado}')"""
        cur.execute(sql)
        con.commit()
        con.close()
        opt = input("Estado cadastrado com sucesso! Enter para voltar ao menu: ")
        gatherer.main()
    except _sqlite3.IntegrityError:
        opt = input("Estado já cadastrado no banco de dados! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()


def inserir_cidade_estado():
    os.system('cls')

    con = _sqlite3.connect("gatherer_database\\database.db")
    cur = con.cursor()
    val = True

    sql = """
        SELECT id, nome
        FROM estados"""

    cur.execute(sql)
    data = cur.fetchall()
    if not data:
        opt = input("Não há estados cadastrados! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()

    new_lista = []
    data = dict(data)

    print("Escolha o estado digitando seu ID: ")
    for chave in data:
        print(chave, " - " + data[chave])

    opt = input(">: ")

    if opt.isnumeric():
        opt = int(opt)
    else:
        val = False

    for chave in data:
        if opt == chave:
            new_lista.append(data[chave])
            val = True
            break
        else:
            val = False
    if val:
        os.system('cls')
        nome_estado = new_lista[0]
        print("ID encontrado com sucesso, por favor digite o nome da cidade a ser cadastrada: ")
        nome_cidade = input(">: ").strip().upper()

        sql = f"""
            SELECT nome, nome_estado
            from cidades
            WHERE nome = '{nome_cidade}' AND nome_estado = '{nome_estado}'"""

        cur.execute(sql)
        data = cur.fetchall()

        verificador = False

        new_data = [item for t in data for item in t]
        nome_cidade_db, nome_estado_db = "", ""

        try:
            nome_cidade_db, nome_estado_db = new_data  # Se der ValueError, quer dizer que podemos cadastrar
        except ValueError:
            verificador = True

        if verificador is True:
            sql = f"""
                  INSERT INTO cidades(nome, nome_estado)
                  VALUES('{nome_cidade}','{nome_estado}')"""
            cur.execute(sql)
            con.commit()
            con.close()
            opt = input("Cidade cadastrada com sucesso! Enter para voltar ao menu: ")
            gatherer.main()
        else:
            opt = input("Cidade já cadastrada neste estado! Enter para voltar ao menu: ")
            con.close()
            gatherer.main()

    else:
        opt = input("ID não encontrado! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()


def inserir_pessoa():
    os.system('cls')

    con = _sqlite3.connect("gatherer_database\\database.db")
    cur = con.cursor()

    cidade_selecionada = ""
    estado_selecionado = ""
    ids_estados = []

    sql = """
          SELECT id, nome
          FROM estados"""

    val = True
    cur.execute(sql)
    data = cur.fetchall()
    data = list(data)

    if not data:
        opt = input("Não há estados e cidades cadastrados! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()

    print("Digite o ID do estado em que deseja cadastrar a pessoa: ")

    for itens in data:
        print(itens[0], " - ", itens[1])
        ids_estados.append(itens[0])

    opt = input(">: ")

    if opt.isnumeric():
        opt = int(opt)
    else:
        val = False

    for item in data:
        if opt == item[0]:
            val = True
            estado_selecionado = item[1]
            break
        else:
            val = False

    sql = f"""
          SELECT id, nome
          FROM cidades
          WHERE '{estado_selecionado}' = nome_estado"""

    cur.execute(sql)
    data = cur.fetchall()
    data = list(data)

    x = True
    for i in ids_estados:
        if opt == i:
            if not data:
                x = False

    if not x:
        opt = input("Não há cidades cadastradas neste estado! Pressione enter para voltar ao menu: ")
        con.close()
        gatherer.main()

    if val:
        os.system("cls")
        print("Agora digite o ID da cidade onde deseja cadastrar a pessoa: ")
        for itens in data:
            print(itens[0], " - ", itens[1])

        opt = input(">: ")
        if opt.isnumeric():
            opt = int(opt)
        else:
            val = False

        if val:
            for item in data:
                if opt == item[0]:
                    val = True
                    cidade_selecionada = item[1]
                    break
                else:
                    val = False

    if val:
        os.system('cls')
        print("Digite o nome da pessoa a ser cadastrada: ")
        nome_pessoa = input(">: ").strip().upper()
        print("Digite a data de nascimento da pessoa no formato: 'DD/MM/YY': ")
        data_nascimento = input(">: ")
        n_data_nascimento = ""
        for num in data_nascimento:
            if num.isnumeric():
                n_data_nascimento += num

        dia, mes, ano = n_data_nascimento[0:2], n_data_nascimento[2:4], n_data_nascimento[4:8]
        n_data_nascimento = "%s/%s/%s" % (dia, mes, ano)

        try:
            datetime.strptime(n_data_nascimento, '%d/%m/%Y')
        except ValueError:
            opt = input("Data inválida! Enter para voltar ao menu: ")
            con.close()
            gatherer.main()

        print("Digite o sexo da pessoa 'm' ou 'f': ")
        sexo = input(">: ").upper().strip()
        if sexo != 'M' and sexo != 'F':
            opt = input("Sexo inválido! Enter para voltar ao menu: ")
            con.close()
            gatherer.main()

        print("Digite o CPF da pessoa no formato ###.###.###-##: ")
        old_cpf = input(">: ")

        # cpf = [int(digit) for digit in old_cpf if digit.isnumeric()]
        cpf = []
        for digit in old_cpf:
            if digit.isnumeric():
                cpf.append(int(digit))

        if len(cpf) != 11:
            opt = input("Erro na validação do CPF! Enter para voltar ao menu: ")
            con.close()
            gatherer.main()

        sum_of_products = sum(a * b for a, b in zip(cpf[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if cpf[9] != expected_digit:
            opt = input("Erro na validação do CPF! Enter para voltar ao menu: ")
            con.close()
            gatherer.main()

        sum_of_products = sum(a * b for a, b in zip(cpf[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if cpf[10] != expected_digit:
            opt = input("Erro na validação do CPF! Enter para voltar ao menu: ")
            con.close()
            gatherer.main()

        new_cpf = ""
        for i in cpf:
            new_cpf = new_cpf + str(i)

        new_cpf = "%s.%s.%s-%s" % (new_cpf[0:3], new_cpf[3:6], new_cpf[6:9], new_cpf[9:11])

        dia, mes, ano = n_data_nascimento.split('/')
        data_nascimento_invertida = (ano + "-" + mes + "-" + dia).strip()

        try:
            sql = f"""
                    INSERT INTO pessoas(nome, data_nascimento, sexo, cpf, cidade, estado)
                    VALUES('{nome_pessoa}','{data_nascimento_invertida}','{sexo}','{new_cpf}',
                    '{cidade_selecionada}','{estado_selecionado}')"""
            cur.execute(sql)
            con.commit()
            con.close()
            opt = input("Pessoa cadastrada com sucesso! Enter para voltar ao menu: ")
            gatherer.main()
        except _sqlite3.IntegrityError:
            opt = input("CPF já cadastrado no banco de dados! Enter para voltar ao menu: ")
            con.close()
            gatherer.main()

    else:
        opt = input("ID não encontrado! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()