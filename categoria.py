import pymysql

try:
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='cleber123',
                           database='firma',
                           port=3306)

    print('Conectado com sucesso')

    nome = input("Informe o nome da categoria: ")

    query = """insert into categoria(nome) values (%s)"""
    
    conn.cursor().execute(query,(nome))
    conn.commit()
    print('Cadastrado com sucesso')

except:
    print('Erro ao conectar')
finally:
    print('Fim')