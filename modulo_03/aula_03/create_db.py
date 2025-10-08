import sqlite3

conn = sqlite3.connect('dados.db')
print("Banco de dados 'dados.db' criado com sucesso!")
conn.close()