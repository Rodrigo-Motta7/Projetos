import customtkinter as ctk


def abrir_cadastro(login, limpar):
   
    login.withdraw()
    
    ctk.set_default_color_theme("dark-blue")

    def voltar_tela1():
        limpar()
        tela2.destroy()
        login.deiconify()

    def validar_cadastro():
        new_usu = entry_new_usu.get()
        new_email = entry_new_email.get()
        new_senha = entry_new_senha.get()
        if new_usu and new_email and new_senha:
            resultado_cadastro.configure(text='Cadastro Concluído', text_color='green')
            tela2.after(1000,voltar_tela1)
        
        else:
            resultado_cadastro.configure(text='Falha no cadastro', text_color='red')

    tela2 = ctk.CTkToplevel(login)
    tela2.title('Tela de cadastro')
    tela2.geometry('300x400')
    
    fonte = ctk.CTkFont(size=17)
    fonte2 = ctk.CTkFont(size=19)
    box_fonte = ctk.CTkFont(size=12)

    label_cadastro = ctk.CTkLabel(tela2,text='CADASTRO', font=fonte2)
    label_cadastro.pack(pady=7)
    
    label_new_usu = ctk.CTkLabel(tela2, text='Usuário:',font=fonte)
    label_new_usu.pack(pady=12)
    entry_new_usu = ctk.CTkEntry(tela2, placeholder_text='Digite o usuário',font=box_fonte)
    entry_new_usu.pack()

    label_new_email = ctk.CTkLabel(tela2, text='E-mail:', font=fonte)
    label_new_email.pack(pady=12)
    entry_new_email = ctk.CTkEntry(tela2, placeholder_text='Digite o E-mail',font=box_fonte)
    entry_new_email.pack()

    label_new_senha = ctk.CTkLabel(tela2, text='Senha:',font=fonte)
    label_new_senha.pack(pady=12)
    entry_new_senha = ctk.CTkEntry(tela2, placeholder_text='Digite a senha', font=box_fonte, show='*')
    entry_new_senha.pack()

    resultado_cadastro = ctk.CTkLabel(tela2,text='')
    resultado_cadastro.pack(pady=8)

    frame2 = ctk.CTkFrame(tela2)
    frame2.pack()
    concluir_cadastro = ctk.CTkButton(frame2,width=100,text='Concluir',command=validar_cadastro)
    concluir_cadastro.grid(row=0, column=0,padx=5)
    voltar = ctk.CTkButton(frame2,width=100, text='Voltar', command=voltar_tela1)
    voltar.grid(row=0, column=1,padx=5)


