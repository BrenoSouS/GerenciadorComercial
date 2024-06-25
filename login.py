import tkinter
import tkinter.messagebox
import ttkbootstrap as tbk
import sqlite3 as bd

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap.style import Style 
from ttkbootstrap.constants import *
from utilitarios import criarUser 
from main import JanelaMain
import sqlite3 as db

def login():
    conexao = db.connect('index.db')
    cursor = conexao.cursor()
    senha_usada = caixaSenha.get()
    nome_usado = caixaNome.get()
    cursor.execute('''SELECT * FROM usuario Where nome = ? and senha = ?''' , (nome_usado , senha_usada))
    verificar = cursor.fetchone()

    try:
        if nome_usado in verificar and senha_usada in verificar:
            messagebox.showinfo(title="aviso de login" , message='acesso confirmado')
            JanelaMain(form_login)
    except:
        messagebox.showerror(title="login info" , message= 'acesso negado')
    finally:
        cursor.close()
        conexao.close()

########-----------Janela Login--------##########

form_login = Tk()
Estilo = Style('superhero')
form_login.title('Faça seu login')

########-----------Dimensionamento--------##########
largura = 400
altura = 500

larg_screen = form_login.winfo_screenwidth()
alt_screen = form_login.winfo_screenheight()

posX = larg_screen/2 - largura/2
posY = alt_screen/2 - altura/2

form_login.geometry('%dx%d+%d+%d' % (largura, altura,posX,posY))
form_login.resizable(False ,False)

########--------------WIDGETS-------------##########
#------------------------------------------------------
lat1 = Frame(form_login, width=50).grid(column=0)
lat2 = Frame(form_login,width=50).grid(column=6)
Top = Frame(form_login , height=50).grid(row=0 , columnspan=3)
bot = Frame(form_login , height=50 ).grid(row = 6 , columnspan=3)
 
container = tbk.Frame(form_login  , height=400 , width=300 ,style='dark' ).grid(row = 1 , column=1 , rowspan=5 , columnspan=5)
#------------------------------------------------------

labeltitulo = tbk.Label(container ,style = 'inverse-dark', text='Login' , font= 'Moder 30' ).grid(row = 1 , column=1  ,padx = 100 )
labelNome = tbk.Label(container ,style = 'inverse-dark', text = 'Nome:' , font = 'Arial 11').grid(row =2 , column = 1 ,sticky=W ,  padx= 10)
labelSenha = tbk.Label(container ,style = 'inverse-dark', text = 'Senha:' , font = 'Arial 11').grid(row =3 , column = 1 , sticky= W , padx=10)

caixaNome = Entry(container)
caixaSenha = Entry(container,show='*')

caixaNome.grid( row = 2 , column=1 , columnspan=2, ipadx=30)
caixaNome.focus()
caixaSenha.grid(row = 3 , column=1 , columnspan=2 ,ipadx=27)


botaoEntrar = Button(container , text='Entrar' , font= 'Arial' ,command = login).grid(row = 4 , column=1 , ipadx=27)
botaoCadastrar = tbk.Button(container ,style= 'info-outline',  text='Cadastrar' , command=criarUser ).grid(row = 5 , column=1  ,sticky=N)
Checar = tbk.Checkbutton(bot , style= "info-round-toggle" , text= 'Lembrar dados?').grid(row=6 , column=1 , sticky=W , padx=90)

form_login.mainloop()


