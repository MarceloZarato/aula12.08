import pymysql

def conectar ():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='programa'
    )

def inserir ():
    con = conectar ()
    cur = con.cursor ()
    nome_item = input ("Nome do Produto: ")
    status = input("Status: ")
    nome_cliente = input("Nome do Cliente: ")
    cur.execute("INSERT INTO reservas (nome_item, status, nome_item) VALUES (%s,%s,%s)", (nome_item, status, nome_item))
    con.commit ()
    con.close()

def listar ():
    con = conectar ()
    cur = con.cursor()
    cur.execute("SELECT * FROM reservas")
    for p in cur.fetchall():
        print (p)
    con.close()

def reservar():
    con = conectar()
    cur = con.cursor()
    id = input("ID do produto: ")
    if "status" == "Disponível":
            print("Item Reservado")
    else:
            print ("Item Indisponível")
    cur.execute ("INSERT INTO reservas SET status = %s WHERE id = %s", (status, id))
    con.commit()
    con.close()
    
def cancelar():
    con = conectar()
    cur = con.cursor()
    id = input("Cancelar reserva do item: ")
    cur.execute ("DELETE FROM reservas WHERE id= %s", (id))
    con.commit()
    con.close()

def adicionar():
    con = conectar()
    cur = con.cursor()
    id = input("Insira o ID do item: ")
    cur.execute ("INSERT INTO reservas WHERE id= %s", (id))
    con.commit()
    con.close()

def menu ():
    while True:
        print ('1 - Listar Recursos')
        print ('2 - Reservar Recurso')
        print ('3 - Cancelar Reserva')
        print ('4 - Adicionar Reserva')
        print ('5 - Sair')

        opcao = input ("Escolha: ")

        if opcao == "1":
            listar ()
        elif opcao == "2":
            reservar ()
        elif opcao == "3":
            cancelar ()
        elif opcao == "4":
            adicionar ()
        elif opcao == "5":
            break


menu ()