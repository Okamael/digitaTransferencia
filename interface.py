from tkinter import *
import digitaTransferencia as dt
import time

class Interface:
    def __init__(self,master=None):
        self.fontePadrao = ("Arial","10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"]= 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(master)
        self.sextoContainer["pady"] =  20
        self.sextoContainer.pack()



        self.titulo = Label(self.primeiroContainer,text="Digita Taransferencias")
        self.titulo["font"]= ("Arial","10","bold")
        self.titulo.pack()

        #Construção filial de Origem
        self.FilialOrigem = Label(self.segundoContainer,text="Filial de Origem:", font=self.fontePadrao)
        self.FilialOrigem.pack(side=LEFT)

        self.filOrigem = Entry(self.segundoContainer)
        self.filOrigem["width"]= 20
        self.filOrigem["font"] = self.fontePadrao
        self.filOrigem.pack(side=LEFT)

        self.FilialDestino = Label(self.terceiroContainer,text="Filial de Destino:", font=self.fontePadrao)
        self.FilialDestino.pack(side=LEFT)

        self.filDestino = Entry(self.terceiroContainer)
        self.filDestino["width"] = 20
        self.filDestino["font"] = self.fontePadrao
        self.filDestino.pack(side=LEFT)

        self.Produtos = Label(self.quartoContainer,text="Lista de Produtos:", font=self.fontePadrao)
        self.Produtos.pack(side=LEFT)

        self.listProdutos = Entry(self.quartoContainer)
        self.listProdutos["width"] = 100
        self.listProdutos["font"] = self.fontePadrao
        self.listProdutos.pack(side=LEFT)

        self.Quantidade = Label(self.quintoContainer,text="Quantidade a  ser transferida:", font=self.fontePadrao)
        self.Quantidade.pack(side=LEFT)

        self.listQuantidade = Entry(self.quintoContainer)
        self.listQuantidade["width"] = 100
        self.listQuantidade["font"] = self.fontePadrao
        self.listQuantidade.pack(side = LEFT)

        self.btIniciar = Button(self.sextoContainer)
        self.btIniciar["text"] = "Iniciar digitação"
        self.btIniciar["font"] = ("Calibri","9")
        self.btIniciar["width"]= 20
        self.btIniciar["command"] = self.iniciaDigitação
        self.btIniciar.pack()

        self.mensagem = Label(self.sextoContainer,text="",font=self.fontePadrao)
        self.mensagem.pack()

    def iniciaDigitação(self):
        filialOri = self.filOrigem.get()
        filialDes = self.filDestino.get()
        listProd  = self.listProdutos.get()
        listQuan  = self.listQuantidade.get()
        #passa para inciar o processo de digitação da transferencia.
        self.mensagem["text"] = "Processo Inicia em 5 segundos, clique no protheus"
        dt.digitaTransferencia(filialOri,filialDes,listProd,listQuan)










root = Tk()
Interface(root)
root.mainloop()