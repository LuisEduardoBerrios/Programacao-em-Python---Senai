import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk

# -------------------------------
# BANCO DE DADOS
# -------------------------------
def conectar():
    return sqlite3.connect('banco.db')

def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS perfil_investidor(
               cpf TEXT,
               experiencia TEXT,
               objetivo TEXT,
               risco TEXT
               )''')
    conn.commit()
    conn.close()

# CREATE
def inserir_perfil():
    cpf = CPF_entry.get()
    experiencia = experiencia_entry.get()
    objetivo = objetivo_entry.get()
    risco = risco_combobox.get()

    if cpf and experiencia and objetivo and risco:
        conn = conectar()
        c = conn.cursor()
        c.execute("INSERT INTO perfil_investidor VALUES(?,?,?,?)", 
                  (cpf, experiencia, objetivo, risco))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'PERFIL INSERIDO COM SUCESSO!')
        mostrar_perfis()
    else:
        messagebox.showwarning('', 'PREENCHA TODOS OS CAMPOS')

# READ
def mostrar_perfis():
    for row in tree.get_children():
        tree.delete(row)

    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM perfil_investidor')
    perfis = c.fetchall()
    for p in perfis:
        tree.insert("", "end", values=(p[0], p[1], p[2], p[3]))
    conn.close()

# UPDATE
def atualizar_perfil():
    selecao = tree.selection()
    if selecao:
        cpf_original = tree.item(selecao)['values'][0]

        novo_cpf = CPF_entry.get()
        nova_exp = experiencia_entry.get()
        novo_obj = objetivo_entry.get()
        novo_risco = risco_combobox.get()

        if novo_cpf and nova_exp and novo_obj and novo_risco:
            conn = conectar()
            c = conn.cursor()
            c.execute("""UPDATE perfil_investidor 
                         SET cpf = ?, experiencia = ?, objetivo = ?, risco = ?
                         WHERE cpf = ?""",
                      (novo_cpf, nova_exp, novo_obj, novo_risco, cpf_original))
            conn.commit()
            conn.close()
            messagebox.showinfo('', 'PERFIL ATUALIZADO!')
            mostrar_perfis()
        else:
            messagebox.showwarning('', 'TODOS OS CAMPOS DEVEM SER PREENCHIDOS')

# DELETE
def deletar_perfil():
    selecao = tree.selection()
    if selecao:
        cpf_del = tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute("DELETE FROM perfil_investidor WHERE cpf = ?", (cpf_del,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'PERFIL DELETADO!')
        mostrar_perfis()
    else:
        messagebox.showerror('', 'SELECIONE UM REGISTRO PARA DELETAR')


# -------------------------------
# INTERFACE GRÁFICA
# -------------------------------
janela = ctk.CTk()
janela.title("Perfil do Investidor - CRUD")
janela.geometry("900x700")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela.configure(bg="#7E4B8C")

titulo = ctk.CTkLabel(janela, text="PERFIL DO INVESTIDOR",
                      font=('Arial', 26, 'bold'),
                      text_color="white")
titulo.grid(row=0, column=0, pady=25)

# FRAME DE ENTRADA
frame = ctk.CTkFrame(janela, fg_color=("white", "#d9b0e6"))
frame.grid(row=1, column=0, padx=20, pady=20)

# CAMPOS
CPF_label = ctk.CTkLabel(frame, text="CPF", text_color="black", font=("Arial", 16))
CPF_label.grid(row=0, column=0, pady=10, padx=10)
CPF_entry = ctk.CTkEntry(frame, placeholder_text="Digite o CPF")
CPF_entry.grid(row=0, column=1, pady=10, padx=10)

experiencia_label = ctk.CTkLabel(frame, text="Experiência", text_color="black", font=("Arial", 16))
experiencia_label.grid(row=1, column=0, pady=10, padx=10)
experiencia_entry = ctk.CTkEntry(frame, placeholder_text="Ex: Iniciante, Intermediário...")
experiencia_entry.grid(row=1, column=1, pady=10, padx=10)

objetivo_label = ctk.CTkLabel(frame, text="Objetivo", text_color="black", font=("Arial", 16))
objetivo_label.grid(row=2, column=0, pady=10, padx=10)
objetivo_entry = ctk.CTkEntry(frame, placeholder_text="Ex: Aposentadoria, Estudos...")
objetivo_entry.grid(row=2, column=1, pady=10, padx=10)

risco_label = ctk.CTkLabel(frame, text="Tolerância ao Risco", text_color="black", font=("Arial", 16))
risco_label.grid(row=3, column=0, pady=10, padx=10)

risco_combobox = ctk.CTkComboBox(frame, values=["Baixo", "Moderado", "Alto"])
risco_combobox.grid(row=3, column=1, pady=10, padx=10)
risco_combobox.set("Baixo")

# BOTÕES
frame_botoes = ctk.CTkFrame(janela, fg_color="#7E4B8C")
frame_botoes.grid(row=2, column=0, pady=20)

btn_salvar = ctk.CTkButton(frame_botoes, text="SALVAR", fg_color="#9b59b6",
                           command=inserir_perfil)
btn_salvar.grid(row=0, column=0, padx=15, pady=10)

btn_atualizar = ctk.CTkButton(frame_botoes, text="ATUALIZAR", fg_color="#3498db",
                              command=atualizar_perfil)
btn_atualizar.grid(row=0, column=1, padx=15, pady=10)

btn_deletar = ctk.CTkButton(frame_botoes, text="DELETAR", fg_color="#e67e22",
                            command=deletar_perfil)
btn_deletar.grid(row=0, column=2, padx=15, pady=10)

# TABELA
frame_tabela = ctk.CTkFrame(janela, fg_color="#f5f5f5")
frame_tabela.grid(row=3, column=0, padx=20, pady=20)

colunas = ("CPF", "Experiência", "Objetivo", "Risco")
tree = ttk.Treeview(frame_tabela, columns=colunas, show="headings", height=18)
tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

for col in colunas:
    tree.heading(col, text=col)
    tree.column(col, anchor=tk.CENTER, width=200)

frame_tabela.grid_columnconfigure(0, weight=1)
frame_tabela.grid_rowconfigure(0, weight=1)

criar_tabela()
mostrar_perfis()

janela.mainloop()
