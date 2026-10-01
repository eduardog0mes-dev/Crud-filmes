import sqlite3

def conectar():
    return sqlite3.connect('filmes.db')

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            ano INTEGER,
            genero TEXT,
            nota REAL
        )
    """)
    conexao.commit()
    conexao.close()

def listar_filmes():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT id,titulo,ano,genero,nota FROM filmes')
    filmes = cursor.fetchall()
    conexao.close()
    return filmes

def cadastrar_filme(titulo,ano,genero,nota):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO filmes(titulo,ano,genero,nota) VALUES (?,?,?,?)",
                ( titulo, ano , genero , nota))
    conexao.commit()
    conexao.close()

def atualizar_nota(id_filme, nova_nota):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE filmes SET nota = ? WHERE id = ?",
        (nova_nota, id_filme),
    )
    conexao.commit()
    conexao.close()

def apagar_filme(id_filme):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM filmes WHERE id = ?", (id_filme,)
    )
    conexao.commit()
    conexao.close()

def mostrar_filmes():
    filmes = listar_filmes()
    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")
    for filme in filmes:
        print(f"{filme[0]} | {filme[1]} ({filme[2]}) | {filme[3]} | nota {filme[4]}")


def menu():
    while True:
        print()
        print("1 - Listar filmes")
        print("2 - Cadastrar filme")
        print("3 - Atualizar nota")
        print("4 - Apagar filme")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                mostrar_filmes()
            elif opcao == "2":
                titulo = input("Título: ")
                ano = int(input("Ano: "))
                genero = input("Gênero: ")
                nota = float(input("Nota: "))
                cadastrar_filme(titulo, ano, genero, nota)
                print("Filme cadastrado.")
            elif opcao == "3":
                id_filme = int(input("ID do filme: "))
                nova_nota = float(input("Nova nota: "))
                atualizar_nota(id_filme, nova_nota)
                print("Nota atualizada.")
            elif opcao == "4":
                id_filme = int(input("ID do filme: "))
                apagar_filme(id_filme)
                print("Filme apagado.")
            elif opcao == "0":
                print("Até mais!")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Valor inválido. Use números onde for ano, ID ou nota.")


criar_tabela()
menu()


    
