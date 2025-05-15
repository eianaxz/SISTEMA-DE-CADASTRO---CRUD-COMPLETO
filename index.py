# Sistema de cadastro, onde o usuário pode cadastrar, visualizar, editar e excluir sua conta (CRUD COMPLETO).
#Essa parte do código é o front-end, o back-end está sendo implementado para eu adicionar no repositório. 
# Importando as bibliotecas necessárias

import os
from tkinter import *  # esse asterisco é para importar tudo
# o messagebox é uma biblioteca que permite criar caixas de mensagem
from tkinter import messagebox

# Criar a janela principal
janela = Tk()  # cria a janela principal
# o que é janela? é uma variável que representa a janela principal do aplicativo.
# o que é variável? é um espaço na memória do computador que armazena um valor.
# o que é Tk? é uma classe da biblioteca tkinter que representa a janela principal do aplicativo.
# define o título da janela principal
janela.title("Na Pele e na Consciência - Cadastro")
janela.geometry("1540x800")  # define o tamanho da janela principal
janela.configure(bg="white")  # define a cor de fundo da janela principal
# define se a janela pode ser redimensionada ou não. O primeiro parâmetro é para largura e o segundo para altura.
janela.resizable(False, False)
# o que é resizable? é um método da classe Tk que define se a janela pode ser redimensionada ou não.
# define o ícone da janela principal

caminho_arquivo = os.path.join(os.path.dirname(__file__), "logo.ico")
janela.iconbitmap(caminho_arquivo)  # define o ícone da janela principal

# define o ícone da janela principalsse método mantém a janela aberta até que o usuário a feche.
janela.mainloop()
