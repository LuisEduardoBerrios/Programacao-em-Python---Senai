import tkinter as tk

def mostrar_resultado_soma():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma  = n1_ +  n2_
    resultado.config(text=soma) 

def mostrar_resultado_subtração():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma  = n1_ -  n2_
    resultado.config(text=soma) 

def mostrar_resultado_multiplicação():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma  = n1_ *  n2_
    resultado.config(text=soma) 

def mostrar_resultado_divisão():
    n1_ = float(n1.get())
    n2_ = float(n2.get())
    soma  = n1_ /  n2_
    resultado.config(text=soma) 

root = tk.Tk()
root.geometry('250x250')

n1_label =  tk.Label(root, text='N1', font=('Times New Roman',12))
n1_label.grid(pady=5, column=1, row =1 )

n1 =  tk.Entry(root, font=('Times New Roman',12))
n1.grid(row=1, column=2, padx=5)

n2_label =  tk.Label(root, text='N2', font=('Times New Roman',12))
n2_label.grid(pady=5, column=1, row =3 )

n2 =  tk.Entry(root, font=('Times New Roman',12))
n2.grid(row=3, column=2, padx=5)



btn_soma =  tk.Button(root, text= '+', font=('Times New Roman',15), command=mostrar_resultado_soma)
btn_soma.grid(row=5, column= 1, pady=5, padx= 10)

btn_soma =  tk.Button(root, text= '-', font=('Times New Roman',15), command=mostrar_resultado_subtração)
btn_soma.grid(row=5, column= 2, pady=5)

btn_soma =  tk.Button(root, text= 'x', font=('Times New Roman',15), command=mostrar_resultado_multiplicação)
btn_soma.grid(row=7, column= 1, pady=5, padx= 10)

btn_soma =  tk.Button(root, text= '/', font=('Times New Roman',15), command=mostrar_resultado_divisão)
btn_soma.grid(row=7, column= 2, pady=5)


resultado =  tk.Label(root, text = 'Resultado é: ', font=('Times New Roman',12))
resultado.grid(row = 10, column=2)

root.mainloop()
