import tkinter as tk

def mostrar_resultado_soma():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma = n1_ + n2_
    resultado.config(text=soma)

def mostrar_resultado_subtração():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    subtracao = n1_ - n2_
    resultado.config(text=subtracao)

def mostrar_resultado_multiplicação():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    multiplicacao = n1_ * n2_
    resultado.config(text=multiplicacao)

def mostrar_resultado_divisão():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    if n2_ == 0:
        resultado.config(text="Erro: Divisão por zero")
    else:
        divisao = n1_ / n2_
        resultado.config(text=divisao)

root = tk.Tk()
root.geometry('200x200')
root.config(bg='#800080')  # Cor de fundo roxa para a janela

# Labels e campos de entrada
n1_label = tk.Label(root, text='N1', font=('Times New Roman', 12), bg='#800080', fg='white')
n1_label.grid(pady=5, column=1, row=1)

n1 = tk.Entry(root, font=('Times New Roman', 12))
n1.grid(row=1, column=2, padx=5)

n2_label = tk.Label(root, text='N2', font=('Times New Roman', 12), bg='#800080', fg='white')
n2_label.grid(pady=5, column=1, row=3)

n2 = tk.Entry(root, font=('Times New Roman', 12))
n2.grid(row=3, column=2, padx=5)

# Frame para os botões
frame_botoes = tk.Frame(root, bg='#800080')
frame_botoes.grid(row=5, column=1, columnspan=2, pady=10)

# Botões
btn_soma = tk.Button(frame_botoes, text='+', font=('Times New Roman', 15), command=mostrar_resultado_soma, bg='white', fg='black')
btn_soma.grid(row=0, column=0, padx=10)

btn_sub = tk.Button(frame_botoes, text='-', font=('Times New Roman', 15), command=mostrar_resultado_subtração, bg='white', fg='black')
btn_sub.grid(row=0, column=1, padx=10)

btn_mul = tk.Button(frame_botoes, text='x', font=('Times New Roman', 15), command=mostrar_resultado_multiplicação, bg='white', fg='black')
btn_mul.grid(row=1, column=0, padx=10)

btn_div = tk.Button(frame_botoes, text='/', font=('Times New Roman', 15), command=mostrar_resultado_divisão, bg='white', fg='black')
btn_div.grid(row=1, column=1, padx=10)

# Label de resultado
resultado = tk.Label(root, text='Resultado é: ', font=('Times New Roman', 12), bg='#800080', fg='white')
resultado.grid(row=8, column=1, columnspan=2)

root.mainloop()