import customtkinter as ctk
conta = ""
ctk.set_default_color_theme('dark-blue')

app = ctk.CTk()
app.title('Calculadora')
app.geometry('300x300')

def limpar():
    global conta
    resultado.configure(text='')
    conta = ""

def adicionar(valor):
    global conta
    conta+= str(valor)
    resultado.configure(text=conta)

def calcular():
    global conta
    try:
        conta = str(eval(conta))
        resultado.configure(text=conta)
    except:
        resultado.configure(text='Erro!')
        conta=""

resultado = ctk.CTkLabel(app,text='', font=('Arial',26)) 
resultado.pack(pady=10)

frame = ctk.CTkFrame(app)
frame.pack(pady=10)

clear_button = ctk.CTkButton(frame,text='limpar', width=40, command=lambda:limpar())
clear_button.grid(row=0, column=2, pady=5)
zero_button = ctk.CTkButton(frame,text='0',width=40,command=lambda:adicionar(0))
zero_button.grid(row=1, column=0, padx=5)
one_button = ctk.CTkButton(frame,text='1',width=40,command=lambda:adicionar(1))
one_button.grid(row=1, column=1, padx=5)
two_button = ctk.CTkButton(frame,text='2', width=40, command=lambda:adicionar(2))
two_button.grid(row=1, column=2, padx=5)
three_button = ctk.CTkButton(frame,text='3', width=40, command=lambda:adicionar(3))
three_button.grid(row=2, column=0, padx=5, pady=5)
four_button = ctk.CTkButton(frame, text='4', width=40, command=lambda:adicionar(4))
four_button.grid(row=2, column=1, padx=5, pady=5)
five_button = ctk.CTkButton(frame, text='5', width=40, command=lambda:adicionar(5))
five_button.grid(row=2, column=2, padx=5, pady=5)
six_button = ctk.CTkButton(frame, text='6', width=40, command=lambda:adicionar(6))
six_button.grid(row=3, column=0, padx=5)
seven_button = ctk.CTkButton(frame, text='7', width=40, command=lambda:adicionar(7))
seven_button.grid(row=3, column=1, padx=5)
eight_button = ctk.CTkButton(frame, text='8', width=40, command=lambda:adicionar(8))
eight_button.grid(row=3, column=2, padx=5)
nine_button = ctk.CTkButton(frame, text='9', width=40, command=lambda:adicionar(9))
nine_button.grid(row=4, column=1, pady=5)

virg_button = ctk.CTkButton(frame,text=',', width=40, command=lambda:adicionar('.'))
virg_button.grid(row=4, column=2, padx=5)
soma_button = ctk.CTkButton(frame, text='+', width=40, command=lambda:adicionar('+'))
soma_button.grid(row=0, column=3, padx=5)
sub_button = ctk.CTkButton(frame, text='-', width=40, command=lambda:adicionar('-'))
sub_button.grid(row=1, column=3, padx=5, pady=5)
mult_button = ctk.CTkButton(frame, text='x', width=40, command=lambda:adicionar('*'))
mult_button.grid(row=2, column=3, padx=5)
div_button = ctk.CTkButton(frame, text='/',width=40, command=lambda:adicionar('/'))
div_button.grid(row=3, column=3, padx=5, pady=5)
resul_button = ctk.CTkButton(frame, text='=', width=40, command=lambda:calcular())
resul_button.grid(row=4, column=3,padx=5)

app.mainloop()
