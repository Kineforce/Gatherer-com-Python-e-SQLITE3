import _sqlite3


def create_database():
    try:
        con = _sqlite3.connect('gatherer_database\\database.db')
        cur = con.cursor()

        sql = """
        CREATE TABLE estados (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              nome TEXT NOT NULL UNIQUE)"""

        sql1 = """
        CREATE TABLE cidades (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              nome TEXT NOT NULL,
                              nome_estado  TEXT NOT NULL)"""

        sql2 = """
        CREATE TABLE pessoas (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                              nome TEXT NOT NULL,
                              data_nascimento TEXT NOT NULL,
                              sexo TEXT NOT NULL,
                              cpf TEXT NOT NULL UNIQUE,
                              estado TEXT NOT NULL,
                              cidade TEXT NOT NULL)"""

        cur.execute(sql)
        cur.execute(sql1)
        cur.execute(sql2)
        con.commit()
        con.close()
    except _sqlite3.OperationalError:
        pass
