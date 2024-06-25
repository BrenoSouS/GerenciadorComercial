import tkinter
import ttkbootstrap as ttk

from tkinter import *
from tkinter import messagebox
from ttkbootstrap.style import Style 
from ttkbootstrap.constants import *

#___________________________________________________________________



def criarUser():

    def confirmar():
        from conexao_banco import cadastro
        __nome = caixaNome.get()
        __senha = caixaSenha.get()
        if __nome != "" and __senha != " " and __senha == caixaConf.get():
            cadastro(__nome , __senha)
            messagebox.showinfo(title='cadastro' , message="cadastro realizado com sucesso.")
            JanelaCadastro.destroy()
        else:
            messagebox.showerror(title='Ocorreu um erro' , message='cheque as informações e tente novamente.')
    # from login import form_login

    JanelaCadastro = Toplevel()
    Estilo = Style("superhero")
    JanelaCadastro.title("Faça seu cadastro")
    JanelaCadastro.focus_force()

    ########-----------Dimensionamento--------##########
    JanelaCadastro.geometry("400x400+1150+300")
    JanelaCadastro.resizable(False ,False)

    ########--------------WIDGETS-------------##########
    labelNome = ttk.Label(JanelaCadastro , text= 'Nome:' , style='info')
    labelSenha = ttk.Label(JanelaCadastro , text= 'Senha:' ,  style='info')
    label_conf_senha = ttk.Label(JanelaCadastro , text= 'Confirme sua Senha:' ,  style='info')
    label_msg = ttk.Label(JanelaCadastro , text= "Adicione as informações acima" , style = 'Info' , font="100")
    
    caixaNome = ttk.Entry(JanelaCadastro ,style= 'info')
    caixaSenha = ttk.Entry(JanelaCadastro ,style= 'info')
    caixaConf = ttk.Entry(JanelaCadastro , style= 'info')

    btn_confirmar = ttk.Button(JanelaCadastro , text = 'Confirmar' , style='outline-primary' , command=confirmar)
    btn_voltar = ttk.Button(JanelaCadastro , text = 'Cancelar' ,command = JanelaCadastro.destroy, style= "outline-danger")

    ########--------------Grid-------------##########
    labelNome.grid(row = 0 , column =0 , pady= 10)
    labelSenha.grid(row = 2 , column =0 , pady= 10)
    label_conf_senha.grid( row = 4, column = 0 , pady= 10 , padx= 40)
    label_msg.grid(row = 8 , pady= 30)

    caixaNome.grid(row = 1 , column = 0 , ipadx=90 , padx = 45)
    caixaNome.focus()
    caixaSenha.grid(row = 3 , column = 0 ,  ipadx=90 , padx = 45)
    caixaConf.grid(row = 5 , column = 0 ,  ipadx=90 , padx = 45)

    btn_confirmar.grid(row = 6 , pady = 20 , ipadx= 66)
    btn_voltar.grid( row = 7 , ipadx= 68 )

    


