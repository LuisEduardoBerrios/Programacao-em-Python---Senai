# 4. SITUAÇÃO PROBLEMA: CÁLCULO DE IMC E CADASTRO DE PACIENTES EM UMA CLÍNICA DE SAÚDE

# A CLÍNICA "SAÚDE & BEM-ESTAR" ENFRENTA DIFICULDADES EM GERENCIAR
# O CADASTRO DE SEUS PACIENTES E CALCULAR O IMC (ÍNDICE DE MASSA CORPORAL) DURANTE AS CONSULTAS. OS DADOS SÃO REGISTRADOS MANUALMENTE,
# O QUE PODE LEVAR A ERROS E DIFICULDADE NA CONSULTA DOS DADOS. ALÉM DISSO, O CÁLCULO DO IMC É FEITO DE MANEIRA ARCAICA, SEM SER AUTOMATIZADO.

# Solução proposta: Criar um sistema de cadastro de pacientes que permita registrar dados como nome, idade, peso e altura. O sistema calculará
# automaticamente o IMC de cada paciente com base nos dados fornecidos. Além disso, será possível consultar, editar ou excluir os registros dos pacientes.

import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk

def conectar():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conn =  conectar()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS usuarios(
              
              nome  TEXT,
              idade TEXT,
              peso TEXT
              altura TEXT
              )   
              ''')
    conn.commit()
    conn.close() 

def inserir_usuario():
    nome  =  nome_entry.get()
    idade = idade_entry.get()
    peso = peso_entry.get()
    altura = altura_entry.get()

    if nome and idade and peso and altura:
        conn =  conectar()
        c = conn.cursor()
        c.execute("INSERT INTO usuarios VALUES(?,?,?,?)", (nome, idade, peso, altura))
        conn.commit()
        conn.close()   
        messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO!')  
        mostrar_usuario()
    else:
        messagebox.showwarning('','INSIRA OS DADOS SOLICITADOS')

# read 
def mostrar_usuario(): 
    for row in tree.get_children():
        tree.delete(row)
        
    conn =  conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios')
    usuario = c.fetchall()
    for us in usuario:
        tree.insert("", "end",values = (us[0], us[1],us[2], us[3]))
    conn.close()    

# atualizar
def atualizar():
    selecao = tree.selection()
    if selecao:
        dado_edit = tree.item(selecao)['values'][0]
        novo_nome = nome_entry.get()
        novo_idade = idade_entry.get()
        novo_peso = peso_entry.get()
        novo_altura = altura_entry.get()

        if novo_nome and novo_idade and  novo_peso and novo_altura:
            conn =  conectar()
            c = conn.cursor()
            c.execute("UPDATE usuarios SET  nome = ?, email = ? , cpf =?  WHERE cpf = ? ", (novo_nome, novo_idade, novo_peso, novo_altura, dado_edit))
            conn.commit()
            conn.close()   
            messagebox.showinfo('', 'DADOS ATUALIZADOS COM SUCESSO!')  
            mostrar_usuario()
        else:
            messagebox.showwarning('','TODOS OS DADOS PRECISAM SER PREENCHIDOS ')

# delete 
def delete_usuario():
    selecao = tree.selection()
    if selecao:
        user_del = tree.item(selecao)['values'][0]
        conn =  conectar()
        c = conn.cursor()     
        c.execute("DELETE FROM usuarios WHERE cpf = ?", (user_del,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADO DELETADO COM SUCESSO')
        mostrar_usuario()
    else:
        messagebox.showerror('', 'ERRO AO DELETAR O DADO')    





janela = ctk.CTk()
janela.configure(fg_color= "blue")
janela.title("Formulário IMC")
janela.geometry("700x630")
caminho = "ico.ico"
janela.iconbitmap(caminho)

tk.Label(janela, text = 'Calculo de IMC', font=('arial', 15)).grid(row=0, column=2, pady=10, padx=10)

fr0 =  ctk.CTkFrame(janela )
fr0.grid(columnspan=3)

nome_label =  tk.Label(fr0, text='Nome', font=('arial', 15))
nome_label.grid(row=2, column=1, pady=10, padx=10)
nome_entry = tk.Entry(fr0, font=('arial', 15))
nome_entry.grid(row=2, column=2, pady=10, padx=10)

idade_label =  tk.Label(fr0, text='Idade', font=('arial', 15))
idade_label.grid(row=3, column=1, pady=10, padx=10)
idade_entry = tk.Entry(fr0, font=('arial', 15))
idade_entry.grid(row=3, column=2, pady=10, padx=10)

peso_label =  tk.Label(fr0, text='Peso', font=('arial', 15))
peso_label.grid(row=4, column=1, pady=10, padx=10)
peso_entry = tk.Entry(fr0, font=('arial', 15))
peso_entry.grid(row=4, column=2, pady=10, padx=10)

altura_label =  tk.Label(fr0, text='Altura', font=('arial', 15))
altura_label.grid(row=5, column=1, pady=10, padx=10)
altura_entry = tk.Entry(fr0, font=('arial', 15))
altura_entry.grid(row=5, column=2, pady=10, padx=10)


fr =  ctk.CTkFrame(janela)
fr.grid(column=2)



fr2 = ctk.CTkFrame(janela)
fr2.grid( columnspan=1)

colunas = ('CPF', 'NOME', 'E-MAIL')
tree =  ttk.Treeview(fr2, columns=colunas, show='headings', height=40)
tree.grid(row=6, column=0,padx=5, sticky='nsew')


for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor= tk.CENTER)

criar_tabela()
mostrar_usuario()


janela.mainloop()