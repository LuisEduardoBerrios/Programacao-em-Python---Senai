import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk

def conectar():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios(
               cpf TEXT,
               nome TEXT,
               email TEXT
               )''')
    conn.commit()
    conn.close()

# create
def inserir_usuario():
    cpf = CPF_entry.get()
    nome = nome_entry.get()
    email = email_entry.get()

    if cpf and nome and email:
        conn = conectar()
        c = conn.cursor()
        c.execute("INSERT INTO usuarios VALUES(?,?,?)", (cpf, nome, email))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO!')
        mostrar_usuario()
    else:
        messagebox.showwarning('', 'INSIRA OS DADOS SOLICITADOS')

# read 
def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)

    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuario = c.fetchall()
    for us in usuario:
        tree.insert("", "end", values=(us[0], us[1], us[2]))
    conn.close()

# atualizar
def atualizar():
    selecao = tree.selection()
    if selecao:
        dado_edit = tree.item(selecao)['values'][0]
        novo_cpf = CPF_entry.get()
        novo_nome = nome_entry.get()
        novo_email = email_entry.get()

        if novo_cpf and novo_nome and novo_email:
            conn = conectar()
            c = conn.cursor()
            c.execute("UPDATE usuarios SET nome = ?, email = ?, cpf = ? WHERE cpf = ?", 
                      (novo_nome, novo_email, novo_cpf, dado_edit))
            conn.commit()
            conn.close()
            messagebox.showinfo('', 'DADOS ATUALIZADOS COM SUCESSO!')
            mostrar_usuario()
        else:
            messagebox.showwarning('', 'TODOS OS DADOS PRECISAM SER PREENCHIDOS')

# delete
def delete_usuario():
    selecao = tree.selection()
    if selecao:
        user_del = tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute("DELETE FROM usuarios WHERE cpf = ?", (user_del,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADO DELETADO COM SUCESSO')
        mostrar_usuario()
    else:
        messagebox.showerror('', 'ERRO AO DELETAR O DADO')

# Interface gráfica com customtkinter
janela = ctk.CTk()  # Janela usando CustomTkinter
janela.title('CRUD - FORM')
janela.geometry('800x630')
janela.iconbitmap('ico.ico')

# Definir tema
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue")  # Tema azul

# Cor de fundo roxo Nubank
janela.configure(bg="#7E4B8C")  # Cor roxa vibrante do Nubank

# Título
titulo_label = ctk.CTkLabel(janela, text='FORMULÁRIO', font=('Arial', 24, 'bold'), text_color="white")
titulo_label.grid(row=0, column=0, pady=30, padx=10)

# Frame de entrada
frame_entrada = ctk.CTkFrame(janela, fg_color=("white", "#d9b0e6"))  # Degradê suave do roxo
frame_entrada.grid(row=1, column=0, padx=20, pady=20)

# Labels e entradas
CPF_label = ctk.CTkLabel(frame_entrada, text='CPF', font=('Arial', 16), text_color="black")
CPF_label.grid(row=1, column=0, pady=10, padx=15)
CPF_entry = ctk.CTkEntry(frame_entrada, font=('Arial', 16), placeholder_text="Digite o CPF", placeholder_text_color="gray")
CPF_entry.grid(row=1, column=1, pady=10, padx=15)

nome_label = ctk.CTkLabel(frame_entrada, text='Nome', font=('Arial', 16), text_color="black")
nome_label.grid(row=2, column=0, pady=10, padx=15)
nome_entry = ctk.CTkEntry(frame_entrada, font=('Arial', 16), placeholder_text="Digite o nome", placeholder_text_color="gray")
nome_entry.grid(row=2, column=1, pady=10, padx=15)

email_label = ctk.CTkLabel(frame_entrada, text='E-mail', font=('Arial', 16), text_color="black")
email_label.grid(row=3, column=0, pady=10, padx=15)
email_entry = ctk.CTkEntry(frame_entrada, font=('Arial', 16), placeholder_text="Digite o e-mail", placeholder_text_color="gray")
email_entry.grid(row=3, column=1, pady=10, padx=15)

# Frame de botões
frame_botoes = ctk.CTkFrame(janela, fg_color="#7E4B8C")  # Mantendo o fundo roxo para os botões
frame_botoes.grid(row=2, column=0, padx=10, pady=20)

# Botões com bordas arredondadas e cores harmoniosas
btn_salvar = ctk.CTkButton(frame_botoes, text='SALVAR', font=('Arial', 16, 'bold'), command=inserir_usuario, fg_color="#9b59b6", hover_color="#8e44ad", text_color="white")
btn_salvar.grid(row=0, column=0, padx=15, pady=15)

btn_atualizar = ctk.CTkButton(frame_botoes, text='ATUALIZAR', font=('Arial', 16, 'bold'), command=atualizar, fg_color="#3498db", hover_color="#2980b9", text_color="white")
btn_atualizar.grid(row=0, column=1, padx=15, pady=15)

btn_delete = ctk.CTkButton(frame_botoes, text='DELETAR', font=('Arial', 16, 'bold'), command=delete_usuario, fg_color="#f39c12", hover_color="#e67e22", text_color="white")
btn_delete.grid(row=0, column=2, padx=15, pady=15)

# Frame da Tabela
frame_tabela = ctk.CTkFrame(janela, fg_color="#f5f5f5")
frame_tabela.grid(row=3, column=0, padx=10, pady=10)

# Configuração da Tabela
colunas = ('CPF', 'NOME', 'E-MAIL')
tree = ttk.Treeview(frame_tabela, columns=colunas, show='headings', height=20)
tree.grid(row=0, column=0, padx=10, sticky='nsew')

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER)

# Configurar a tabela para se expandir
frame_tabela.grid_rowconfigure(0, weight=1)
frame_tabela.grid_columnconfigure(0, weight=1)

criar_tabela()
mostrar_usuario()

# Iniciar a aplicação
janela.mainloop()
