import tkinter as tk
from tkinter import messagebox

def display():
    print("\nDados do cliente: ")

    nome = nomel.get()
    print(f"Nome do cliente: {nome}")

    idade = idadel.get()
    print(f"Idade do cliente: {idade}")

    email = emaill.get()
    print(f"E-mail do cliente: {email}")

    celular = celularl.get()
    print(f"Celular do cliente: {celular}")

    endereço = endereçol.get()
    print(f"Endereço do cliente: {endereço}")

    cidade = cidadel.get()
    print(f"Cidade do cliente: {cidade}")

    cep = cepl.get()
    print(f"CEP: {cep}")

    curso = cursol.get()
    print(f"Curso escolhido: {curso}")

    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

root = tk.Tk()
root.title("Sistema de Cadastro de Clientes")
root.geometry('1700x750')

nome =  tk.Label(root, text='Nome: ', font=('Times New Roman',12))
nome.grid(pady=5, column=1, row =1)
nomel = tk.Entry(root, font=('Times New Roman',12))
nomel.grid(row=1, column=2, padx=5)

idade =  tk.Label(root, text='Idade: ', font=('Times New Roman',12))
idade.grid(pady=5, column=1, row =2)
idadel = tk.Entry(root, font=('Times New Roman',12))
idadel.grid(row=2, column=2, padx=5)

email =  tk.Label(root, text='Email: ', font=('Times New Roman',12))
email.grid(pady=5, column=1, row =3)
emaill = tk.Entry(root, font=('Times New Roman',12))
emaill.grid(row=3, column=2, padx=5)

celular =  tk.Label(root, text='Celular: ', font=('Times New Roman',12))
celular.grid(pady=5, column=1, row =4)
celularl = tk.Entry(root, font=('Times New Roman',12))
celularl.grid(row=4, column=2, padx=5)

endereço =  tk.Label(root, text='Endereço: ', font=('Times New Roman',12))
endereço.grid(pady=5, column=1, row =5)
endereçol = tk.Entry(root, font=('Times New Roman',12))
endereçol.grid(row=5, column=2, padx=5)

cidade =  tk.Label(root, text='Cidade: ', font=('Times New Roman',12))
cidade.grid(pady=5, column=1, row =6)
cidadel = tk.Entry(root, font=('Times New Roman',12))
cidadel.grid(row=6, column=2, padx=5)

cep =  tk.Label(root, text='CEP: ', font=('Times New Roman',12))
cep.grid(pady=5, column=1, row =7)
cepl = tk.Entry(root, font=('Times New Roman',12))
cepl.grid(row=7, column=2, padx=5)

curso =  tk.Label(root, text='Curso: ', font=('Times New Roman',12))
curso.grid(pady=5, column=1, row =8)
cursol = tk.Entry(root, font=('Times New Roman',12))
cursol.grid(row=8, column=2, padx=5)

btn  =  tk.Button(root, text= 'Enviar dados', font=('Times New Roman',12), command=display)
btn.grid(padx=5, column=2)

root.mainloop()

