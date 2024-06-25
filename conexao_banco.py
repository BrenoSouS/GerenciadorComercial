import sqlite3 as db
import tkinter
from tkinter import messagebox
from sqlite3 import *

class usuario:
    def __init__(self , nome , senha):
        self.nome = nome
        self.senha = senha

# conector = db.connect('index.db')
# curso = conector.cursor()

# curso.execute("""
# CREATE TABLE usuario(
# nome VARCHAR NOT NULL,
# id_usuario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
# senha VARCHAR NOT NULL )
# """
# )
# curso.fetchall()
# curso.close()
# conector.close()
def cadastro(nome ,senha):
    
    try:
        conexao = db.connect('index.db')
        cursordb = conexao.cursor()
        novo_usuario = usuario(nome ,senha)
        script ='''INSERT INTO usuario (nome , senha)
                          VALUES (:nome , :senha )'''
         
        cursordb.execute(script , vars(novo_usuario))


        cursordb.fetchall()

        conexao.commit()
    except db.DatabaseError as err:
        print('erro de banco de dados: {err}')
        messagebox.showerror(title='Erro de banco de dados' , message = err)
    except db.IntegrityError as err2:
        messagebox.showerror(title='Ocorreu um erro ' , message= err2)
    
    except db.OperationalError as err3:
        messagebox.showerror(title= 'Ocorreu um erro' , message= err3)
    except db.ProgrammingError as err4 :
        messagebox.showerror(title='erro de programação' , message=err4)
    
    finally:
        cursordb.close()
        conexao.close()

def login(nome , senha):
    db.Cursor.execute('''SELECT * FROM usuario Where nome = ? and senha = ?''' , (nome , senha))
    verificar = db.Cursor.fetchone()

    try:
        if nome in verificar and senha in verificar:
            messagebox.showinfo(title="aviso de login" , message='acesso confirmado')
    except:
        messagebox.showerror(title="login info" , message= 'acesso negado')