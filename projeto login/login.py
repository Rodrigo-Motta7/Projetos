import customtkinter as ctk
from cadastro import abrir_cadastro

ctk.set_default_color_theme("dark-blue")


def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if usuario == 'Rodrigo' and senha == '1234':
        resultado_login.configure(text='Login feito com sucesso!',text_color='green')
    else:
        resultado_login.configure(text='Falha no login!', text_color='red')
def limpar():
    entry_usuario.delete(0,'end')
    entry_senha.delete(0,'end')
    resultado_login.configure(text="")


login = ctk.CTk()
fonte = ctk.CTkFont(size=18)
box_fonte = ctk.CTkFont(size=13)

login.title('Sistema de login')
login.geometry('300x300')

label_usuario = ctk.CTkLabel(login,text='Usuário:', font=fonte)
label_usuario.pack(pady=13)
entry_usuario = ctk.CTkEntry(login,placeholder_text='Digite o usuário',font=box_fonte)
entry_usuario.pack()

label_senha = ctk.CTkLabel(login,text='Senha:', font=fonte)
label_senha.pack(pady=13)
entry_senha = ctk.CTkEntry(login,placeholder_text='Digite a senha',font=box_fonte, show='*')
entry_senha.pack()

resultado_login = ctk.CTkLabel(login,text='')
resultado_login.pack(pady=9)

frame = ctk.CTkFrame(login)
frame.pack()
botao_login = ctk.CTkButton(frame,text='Entrar', width=90,command=validar_login)
botao_login.grid(row=0, column=0,padx=5)
botao_cadastro = ctk.CTkButton(frame,text='Cadastrar', width=90, command=lambda:abrir_cadastro(login, limpar))
botao_cadastro.grid(row=0, column=1,padx=5)



login.mainloop()