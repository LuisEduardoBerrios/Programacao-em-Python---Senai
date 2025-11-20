import tkinter as tk
from tkinter import Canvas
from tkinter import messagebox


def display():
    print("\n========= DADOS DO CLIENTE =========")
    print("Nome:", entry_nome.get())
    print("Idade:", entry_idade.get())
    print("E-mail:", entry_email.get())
    print("Celular:", entry_celular.get())
    print("Endereço:", entry_endereco.get())
    print("Cidade:", entry_cidade.get())
    print("CEP:", entry_cep.get())
    print("Curso:", entry_curso.get())
    print("====================================\n")

    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")


# -------------------------- JANELA PRINCIPAL -------------------------- #
root = tk.Tk()
root.title("Sistema de Cadastro de Clientes")
root.geometry("1700x750")
root.configure(bg="#5A0099")  # Roxo elegante

# -------------------------- CARD CENTRAL COM SHADOW -------------------------- #
shadow = tk.Frame(root, bg="#3A0066")
shadow.place(relx=0.5, rely=0.5, anchor="center", width=1000, height=620)

card = tk.Frame(root, bg="white", bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center", width=980, height=600)

# -------------------------- TÍTULO EM GRADIENTE -------------------------- #
titulo_canvas = Canvas(card, width=980, height=80, bd=0, highlightthickness=0)
titulo_canvas.pack()

# Gradiente horizontal (pintado manualmente)
for i in range(980):
    r1, g1, b1 = (130, 10, 209)
    r2, g2, b2 = (200, 120, 255)
    r = int(r1 + (r2 - r1) * (i / 980))
    g = int(g1 + (g2 - g1) * (i / 980))
    b = int(b1 + (b2 - b1) * (i / 980))
    cor = f"#{r:02x}{g:02x}{b:02x}"
    titulo_canvas.create_line(i, 0, i, 80, fill=cor)

titulo_canvas.create_text(
    490, 40, text="Cadastro de Clientes", fill="white",
    font=("Segoe UI", 30, "bold")
)

# -------------------------- FRAME INTERNO -------------------------- #
form = tk.Frame(card, bg="white")
form.pack(pady=10)

# -------------------------- FUNÇÕES ESTÉTICAS -------------------------- #
def criar_label(texto):
    return tk.Label(
        form,
        text=texto,
        font=("Segoe UI", 14, "bold"),
        bg="white",
        fg="#4B0082"
    )


def criar_entry():
    e = tk.Entry(
        form,
        font=("Segoe UI", 14),
        bd=0,
        highlightthickness=2,
        relief="flat",
        width=35,
        highlightbackground="#D2D2D2",
        highlightcolor="#820AD1",
    )
    return e


# -------------------------- CAMPOS DO FORMULÁRIO -------------------------- #
labels = [
    "Nome", "Idade", "E-mail", "Celular",
    "Endereço", "Cidade", "CEP", "Curso"
]

entries = {}

for i, texto in enumerate(labels):
    criar_label(texto + ":").grid(row=i, column=0, sticky="w", pady=12, padx=20)
    campo = criar_entry()
    campo.grid(row=i, column=1, pady=12, padx=20)
    entries[texto] = campo

entry_nome = entries["Nome"]
entry_idade = entries["Idade"]
entry_email = entries["E-mail"]
entry_celular = entries["Celular"]
entry_endereco = entries["Endereço"]
entry_cidade = entries["Cidade"]
entry_cep = entries["CEP"]
entry_curso = entries["Curso"]

# -------------------------- BOTÃO COM ANIMAÇÃO -------------------------- #
def on_enter(event):
    btn.configure(bg="#9B34F0", fg="white")


def on_leave(event):
    btn.configure(bg="#820AD1", fg="white")


btn = tk.Button(
    card,
    text="Enviar Dados",
    font=("Segoe UI", 12, "bold"),
    bg="#820AD1",
    fg="white",
    activebackground="#9B34F0",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    width=15,
    height=20,
    command=display
)

btn.pack(pady=25)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# -------------------------- EXECUÇÃO -------------------------- #
root.mainloop()
