# CRUD: create -  read -  update  - delete

import sqlite3

con = sqlite3.connect("Banco de dados.db") # cria o banco de dados e a conexão
cursor = con.cursor() #cria o cursor

cursor.execute(''' CREATE TABLE IF NOT EXISTS tabela(
               Nome TEXT,
               Idade INTEGER)
''')

cursor.execute("INSERT INTO tabela VALUES (?,?)", ("Julia",20))
con.commit() # envia os dados para o banco de dados "con"

cursor.close
