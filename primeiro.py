import pymysql

try:
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='cleber123',
                           database='firma',
                           port=3306)
    print('Conectado com sucesso')

    nome = input("Informe o nome do cliente: ")
    endereco = input("Informe o endereço do cliente: ")
    telefone = input("Informe o telefone do cliente:")
    limite = input("Informe o limite do cliente: ")
    status = input("Informe o status do cliente (1-Ruim; 2-Médio; 3-Bom):")

    query = """insert into cliente(nome, endereco, telefone,
                limite, status_cliente_codigo)
                values(%s, %s, %s, %s, %s)"""
    
    conn.cursor().execute(query, 
                          (nome, endereco, telefone, limite, status))
    conn.commit()
    print('Cadastrado com sucesso')
except:
    print('Erro ao conectar')
finally:
    print('Fim')