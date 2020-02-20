import os
import gatherer
import _sqlite3


def remover_pessoa():
    os.system('cls')
    con = _sqlite3.connect("gatherer_database\\database.db")
    cur = con.cursor()

    sql = """
    SELECT id
    FROM pessoas"""

    cur.execute(sql)
    data = cur.fetchall()

    if not data:
        opt = input("Não há pessoas cadastradas! Enter para voltar ao menu: ")
        con.close()
        gatherer.main()

    print("Para remover uma pessoa, insira o CPF correspondente no formato ###.###.###-##: ")
    cpf = input(">: ").strip()
    new_cpf = ""

    for num in cpf:
        if num.isnumeric():
            new_cpf += num

    new_cpf = "%s.%s.%s-%s" % (new_cpf[0:3], new_cpf[3:6], new_cpf[6:9], new_cpf[9:11])

    sql = f"""
    DELETE FROM pessoas 
    WHERE cpf = '{new_cpf}'"""

    cur.execute(sql)
    if con.total_changes > 0:
        print("A pessoa cadastrada no banco de dados está prestes a ser removida! S para continuar, N para cancelar: ")
        opt = input(">: ").strip().upper()
        if opt == 'N':
            con.rollback()
            opt = input("Mudanças foram desfeitas! Enter para voltar ao menu: ")
        else:
            con.commit()
            opt = input("Mudanças foram feitas! Enter para voltar ao menu: ")
    else:
        opt = input("CPF não encontrado no banco de dados! Nenhum dado foi alterado! Enter para voltar ao menu: ")
    con.close()
    gatherer.main()




