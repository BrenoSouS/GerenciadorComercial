import tkinter
import tkinter.messagebox
import ttkbootstrap as tbk
import sqlite3 as bd

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import LabelFrame
from ttkbootstrap.style import Style 
from ttkbootstrap.constants import *

maisvendido = ''
def JanelaMain(root):
        
        main = root
        main.title('MAIN')
        Estilo  = Style('superhero')
        
        imagemBarras = PhotoImage(file = "iconbar.png")

        #-------------DIMENSIONAMENTO----------------------------#
        largura = 1000
        altura = 800
        larg_screen = main.winfo_screenwidth()
        alt_screen = main.winfo_screenheight()

        posX = larg_screen/2 - largura/2
        posY = alt_screen/2 - altura/2

        main.geometry('%dx%d+%d+%d' % (largura, altura,posX,posY))
        main.resizable(True ,True)

        #------------- BANCO DE DADOS---------------------------------------#
        # conexao = bd.connect('clientes.bd')
        # cursor = conexao.cursor()

        # #-------------MENU---------------------------------------#
        menu_principal = Menu(main)

        SubMenu_Opcoes = Menu(menu_principal , tearoff= 0)
        SubMenu_Opcoes.add_command(label='Opções')
        SubMenu_Opcoes.add_separator()

        menu_principal.add_cascade(label='Opções' , menu= SubMenu_Opcoes)

        main.config(menu = menu_principal)

        #-------------WIDGETS------------------------------------#
        top = tbk.Frame(main , style ='secondary' )
        mid = tbk.Frame(main , style = 'secondary')
        corner = tbk.Frame(main , style= 'secondary')
        sub = tbk.Notebook(mid , name= 'nsei' ,  )
        framesub1 = tbk.Frame(sub)
        framesub2 = tbk.Frame(sub)

        label_Cadastro_de_produto = tbk.Label(corner , text= 'Cadastrar novo produto' , background= '#32465a', style= 'sucess' ,font='Arial 15' , anchor= 'center')
        nome_produto = tbk.Label(corner , text='Nome:' , background='#4e5d6c')
        quantidade =tbk.Label(corner , text = 'quantidade:' , background='#4e5d6c')
        valor_venda = tbk.Label(corner , text= 'Valor de venda:' , background='#4e5d6c')
        valor_compra = tbk.Label(corner , text='valor de compra:' , background='#4e5d6c')
        label_btn_recomendar = tbk.Label(corner , text='Recomendar um valor?', background = '#4e5d6c' , anchor=CENTER)
        label_progresso = tbk.Label(framesub2 , text='Lucro do mês:' , background='#4e5d6c' , anchor=CENTER)
        label_grafico = tbk.Label(framesub2 ,text='item mais vendido:{maisvendido}')
        label_titulo_mid = tbk.Label(framesub1 , text='ESCOLHA UMA OPÇÃO DE BUSCA A BAIXO' , anchor=CENTER , font='Arial 15')
        label_procura_codigo = tbk.Label(framesub1 , text='Digite código de barras:' , background='#4e5d6c' , anchor=CENTER)
        label_procura_id = tbk.Label(framesub1 , text='Digite o id do produto:' , background='#4e5d6c' , anchor=CENTER)
        label_procurar_nome = tbk.Label(framesub1 , text='Digite o nome do produto:' , background='#4e5d6c' , anchor=CENTER)


        caixa_nome = tbk.Entry(corner , style = 'dark')
        caixa_quantidade = tbk.Entry(corner , style='dark')
        caixa_Vlr_venda = tbk.Entry(corner , style = 'dark')
        caixa_Vlr_compra = tbk.Entry(corner , style = 'dark')
        caixa_procura_codigo = tbk.Entry(framesub1 , style='info')
        caixa_procura_id = tbk.Entry(framesub1 ,style='info')
        caixa_procura_nome = tbk.Entry(framesub1 , style='info')

        botao_recomendar_valor = tbk.Checkbutton(corner ,style='info-round-toggle')
        botao_cadastro = tbk.Button(corner , text = 'Cadastrar produto' ,style='info-outline')
        botao_procurar = tbk.Button(framesub1  ,text='Procurar', style='info-outline' )
        botao_procurar_barras = tbk.Button(framesub1 , style='info' , image= imagemBarras)


        lista = ttk.Treeview(top,columns=('id' , "nome" , "cod. barras" , "preço"  ) )
        lista.heading("#0" ,text= "Id")
        lista.heading("#1" ,text= "Nome")
        lista.heading("#2" ,text= "Cod. Barras")
        lista.heading('#3' , text='Preço')
        lista.column("#0" , width=50)
        lista.column("#1" , width=200)
        lista.column("#2" , width=200)
        lista.column('#3' , width=50)

        rolagem = tbk.Scrollbar(top , orient= VERTICAL , style="info-round")
        lista.configure(yscrollcommand = rolagem)

        progresso = tbk.Progressbar(framesub2 , style='info' , maximum=100 , mode='determinate' , value=0)

        grafico_vendas = tbk.Meter(framesub2 ,bootstyle='info' , subtext='Variavel')
        grafico_itens_vendidos = tbk.Meter(framesub2 , bootstyle='info' , subtext='variavelitens')

        #-------------Organização--------------------------------#

        top.place(relx= 0.01 , rely= 0.01, relwidth=0.98 , relheight=0.26)
        mid.place(relx = 0.01 , rely= 0.28 , relwidth=0.66 , relheight= 0.70)
        corner.place(relx=0.69 , rely= 0.28 , relheight= 0.70 , relwidth= 0.30)
        sub.place(relx = 0.02 , rely=0.02 , relheight=0.95 , relwidth=0.95 )

        label_Cadastro_de_produto.place(relx = 0.05 ,rely=0.01 , relwidth=0.9 , relheight=0.08)
        nome_produto.place(relx = 0.02 , rely= 0.10)
        quantidade.place(relx = 0.02 , rely=0.25)
        valor_compra.place(relx = 0.02 , rely= 0.40)
        valor_venda.place(relx = 0.02 , rely = 0.55)
        label_progresso.place(relx = 0.40, rely = 0.12 , relheight= 0.06 , relwidth= 0.20)
        label_procura_codigo.place(relx=0.10 , rely=0.15 , relheight= 0.05 , relwidth=0.30)
        label_procura_id.place(relx=0.10 , rely= 0.35 , relheight=0.05 , relwidth=0.3)
        label_procurar_nome.place(relx = 0.10 , rely= 0.55 , relheight=0.05 , relwidth=0.3)
        label_grafico.place(relx = 0.15 , rely = 0.40)
        label_titulo_mid.place(relx= 0.05 , rely= 0.03)


        caixa_nome.place(relx = 0.02 , rely= 0.15 , relheight= 0.05 , relwidth= 0.95)
        caixa_quantidade.place(relx = 0.02 , rely = 0.30 , relheight = 0.05 , relwidth = 0.95)
        caixa_Vlr_compra.place(relx = 0.02 , rely = 0.45 , relheight= 0.05 , relwidth=0.95)
        caixa_Vlr_venda.place(relx = 0.02 , rely = 0.60 , relheight= 0.05 , relwidth= 0.95)
        caixa_procura_codigo.place(relx=0.05 , rely= 0.2 , relwidth= 0.7)
        caixa_procura_id.place(relx=0.05 , rely=0.4 , relwidth=0.7)
        caixa_procura_nome.place(relx = 0.05 , rely = 0.6 , relwidth=0.7)

        botao_recomendar_valor.place(relx = 0.02 , rely= 0.66 , relwidth=0.08 , relheight=0.03)
        label_btn_recomendar.place(relx = 0.1199 , rely = 0.657 , relheight=0.04)
        botao_cadastro.place(relx = 0.24 , rely= 0.87, relheight=0.10 , relwidth=0.50)
        botao_procurar.place(relx = 0.05, rely=0.7 , relheight=0.15 , relwidth=0.35)
        botao_procurar_barras.place(relx= 0.8 , rely= 0.3 , relwidth= 0.15 , relheight=0.3)

        lista.place(relx=0.01 , rely = 0.02 ,relheight=0.96 , relwidth= 0.95)
        rolagem.place(relx= 0.96 , rely = 0.02,relheight=0.955 , relwidth=0.03)

        progresso.place(relx=0.30 , rely= 0.20 , relheight= 0.03 , relwidth= 0.40)
        grafico_vendas.place(relx = 0.15 , rely= 0.45 )
        grafico_itens_vendidos.place(relx= 0.5 , rely=0.45)

        sub.add(framesub1 , text='procura de item')
        sub.add(framesub2 , text='Dados gerais')


        main.mainloop()


#########################################################################################################
#########################################################################################################
# #########################################################################################################

# main = Tk()
# main.title('MAIN')
# Estilo  = Style('superhero')

# imagemBarras = PhotoImage(file = "iconbar.png")

# #-------------DIMENSIONAMENTO----------------------------#
# largura = 1000
# altura = 800
# larg_screen = main.winfo_screenwidth()
# alt_screen = main.winfo_screenheight()

# posX = larg_screen/2 - largura/2
# posY = alt_screen/2 - altura/2

# main.geometry('%dx%d+%d+%d' % (largura, altura,posX,posY))
# main.resizable(True ,True)

# #------------- BANCO DE DADOS---------------------------------------#
# # conexao = bd.connect('clientes.bd')
# # cursor = conexao.cursor()


# #-------------MENU---------------------------------------#
# menu_principal = Menu(main)

# SubMenu_Opcoes = Menu(menu_principal , tearoff= 0)
# SubMenu_Opcoes.add_command(label='Opções')
# SubMenu_Opcoes.add_separator()

# menu_principal.add_cascade(label='Opções' , menu= SubMenu_Opcoes)

# main.config(menu = menu_principal)

# #-------------WIDGETS------------------------------------#
# top = tbk.Frame(main , style ='secondary' )
# mid = tbk.Frame(main , style = 'secondary')
# corner = tbk.Frame(main , style= 'secondary')
# sub = tbk.Notebook(mid , name= 'nsei' ,  )
# framesub1 = tbk.Frame(sub)
# framesub2 = tbk.Frame(sub)

# label_Cadastro_de_produto = tbk.Label(corner , text= 'Cadastrar novo produto' , background= '#32465a', style= 'sucess' ,font='Arial 15' , anchor= 'center')
# nome_produto = tbk.Label(corner , text='Nome:' , background='#4e5d6c')
# quantidade =tbk.Label(corner , text = 'quantidade:' , background='#4e5d6c')
# valor_venda = tbk.Label(corner , text= 'Valor de venda:' , background='#4e5d6c')
# valor_compra = tbk.Label(corner , text='valor de compra:' , background='#4e5d6c')
# label_btn_recomendar = tbk.Label(corner , text='Recomendar um valor?', background = '#4e5d6c' , anchor=CENTER)
# label_progresso = tbk.Label(framesub2 , text='Lucro do mês:' , background='#4e5d6c' , anchor=CENTER)
# label_grafico = tbk.Label(framesub2 ,text='item mais vendido:{maisvendido}')
# label_titulo_mid = tbk.Label(framesub1 , text='ESCOLHA UMA OPÇÃO DE BUSCA A BAIXO' , anchor=CENTER , font='Arial 15')
# label_procura_codigo = tbk.Label(framesub1 , text='Digite código de barras:' , background='#4e5d6c' , anchor=CENTER)
# label_procura_id = tbk.Label(framesub1 , text='Digite o id do produto:' , background='#4e5d6c' , anchor=CENTER)
# label_procurar_nome = tbk.Label(framesub1 , text='Digite o nome do produto:' , background='#4e5d6c' , anchor=CENTER)


# caixa_nome = tbk.Entry(corner , style = 'dark')
# caixa_quantidade = tbk.Entry(corner , style='dark')
# caixa_Vlr_venda = tbk.Entry(corner , style = 'dark')
# caixa_Vlr_compra = tbk.Entry(corner , style = 'dark')
# caixa_procura_codigo = tbk.Entry(framesub1 , style='info')
# caixa_procura_id = tbk.Entry(framesub1 ,style='info')
# caixa_procura_nome = tbk.Entry(framesub1 , style='info')

# botao_recomendar_valor = tbk.Checkbutton(corner ,style='info-round-toggle')
# botao_cadastro = tbk.Button(corner , text = 'Cadastrar produto' ,style='info-outline')
# botao_procurar = tbk.Button(framesub1  ,text='Procurar', style='info-outline' )
# botao_procurar_barras = tbk.Button(framesub1 , style='info' , image= imagemBarras)


# lista = ttk.Treeview(top,columns=('id' , "nome" , "cod. barras" , "preço"  ) )
# lista.heading("#0" ,text= "Id")
# lista.heading("#1" ,text= "Nome")
# lista.heading("#2" ,text= "Cod. Barras")
# lista.heading('#3' , text='Preço')
# lista.column("#0" , width=50)
# lista.column("#1" , width=200)
# lista.column("#2" , width=200)
# lista.column('#3' , width=50)

# rolagem = tbk.Scrollbar(top , orient= VERTICAL , style="info-round")
# lista.configure(yscrollcommand = rolagem)

# progresso = tbk.Progressbar(framesub2 , style='info' , maximum=100 , mode='determinate' , value=0)

# grafico_vendas = tbk.Meter(framesub2 ,bootstyle='info' , subtext='Variavel')
# grafico_itens_vendidos = tbk.Meter(framesub2 , bootstyle='info' , subtext='variavelitens')

# #-------------Organização--------------------------------#

# top.place(relx= 0.01 , rely= 0.01, relwidth=0.98 , relheight=0.24)
# mid.place(relx = 0.01 , rely= 0.28 , relwidth=0.66 , relheight= 0.70)
# corner.place(relx=0.69 , rely= 0.28 , relheight= 0.70 , relwidth= 0.30)
# sub.place(relx = 0.02 , rely=0.02 , relheight=0.95 , relwidth=0.95 )

# label_Cadastro_de_produto.place(relx = 0.05 ,rely=0.01 , relwidth=0.9 , relheight=0.08)
# nome_produto.place(relx = 0.02 , rely= 0.10)
# quantidade.place(relx = 0.02 , rely=0.25)
# valor_compra.place(relx = 0.02 , rely= 0.40)
# valor_venda.place(relx = 0.02 , rely = 0.55)
# label_progresso.place(relx = 0.40, rely = 0.12 , relheight= 0.06 , relwidth= 0.20)
# label_procura_codigo.place(relx=0.10 , rely=0.15 , relheight= 0.05 , relwidth=0.30)
# label_procura_id.place(relx=0.10 , rely= 0.35 , relheight=0.05 , relwidth=0.3)
# label_procurar_nome.place(relx = 0.10 , rely= 0.55 , relheight=0.05 , relwidth=0.3)
# label_grafico.place(relx = 0.15 , rely = 0.40)
# label_titulo_mid.place(relx= 0.05 , rely= 0.03)


# caixa_nome.place(relx = 0.02 , rely= 0.15 , relheight= 0.05 , relwidth= 0.95)
# caixa_quantidade.place(relx = 0.02 , rely = 0.30 , relheight = 0.05 , relwidth = 0.95)
# caixa_Vlr_compra.place(relx = 0.02 , rely = 0.45 , relheight= 0.05 , relwidth=0.95)
# caixa_Vlr_venda.place(relx = 0.02 , rely = 0.60 , relheight= 0.05 , relwidth= 0.95)
# caixa_procura_codigo.place(relx=0.05 , rely= 0.2 , relwidth= 0.7)
# caixa_procura_id.place(relx=0.05 , rely=0.4 , relwidth=0.7)
# caixa_procura_nome.place(relx = 0.05 , rely = 0.6 , relwidth=0.7)

# botao_recomendar_valor.place(relx = 0.02 , rely= 0.66 , relwidth=0.08 , relheight=0.03)
# label_btn_recomendar.place(relx = 0.1199 , rely = 0.657 , relheight=0.04)
# botao_cadastro.place(relx = 0.24 , rely= 0.87, relheight=0.10 , relwidth=0.50)
# botao_procurar.place(relx = 0.05, rely=0.7 , relheight=0.15 , relwidth=0.35)
# botao_procurar_barras.place(relx= 0.8 , rely= 0.3 , relwidth= 0.15 , relheight=0.3)

# lista.place(relx=0.01 , rely = 0.02 ,relheight=0.96 , relwidth= 0.95)
# rolagem.place(relx= 0.96 , rely = 0.02,relheight=0.955 , relwidth=0.03)

# progresso.place(relx=0.30 , rely= 0.20 , relheight= 0.03 , relwidth= 0.40)
# grafico_vendas.place(relx = 0.15 , rely= 0.45 )
# grafico_itens_vendidos.place(relx= 0.5 , rely=0.45)

# sub.add(framesub1 , text='procura de item')
# sub.add(framesub2 , text='Dados gerais')


# main.mainloop()