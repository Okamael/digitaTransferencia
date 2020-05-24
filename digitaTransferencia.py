#########################################################################
#Criado com o objetivo de  digitar transferencias  e auxiliar o fiscal  #
#na digitação dos produtos                                              #
#autor Murilo Ramos da SILVA                                            #
#data 20/05/2020                                                        #
##########################################################################


import time

import pyautogui as pg
from uteis import uteis as ut



def digitaTransferencia(filialOrigem,filialDestino,ltProdutos,ltaQuantidade):
    filOrigem = filialOrigem
    filDesti  = filialDestino
    listaProduto = ltProdutos
    listaQuantidade = ltaQuantidade
    produtos = listaProduto.split(',')
    quantidade = listaQuantidade.split(',')
    time.sleep(3)

    contador = 0

    for produto in produtos:
        time.sleep(2)
        print("Inicio producesso produto {} quantidade:{}".format(produto,quantidade[contador]))
    
        #executa a primeira parte Buscando o produto na filial de origem
        ut.buscaProduto(filOrigem,produto)
        time.sleep(1)
        #busca produto na filial destino
        ut.buscaProdutoDestino(filDesti,produto)
        time.sleep(2)

        #valida se  deu erro na  busca do produto na filial destino
        if(pg.locateOnScreen("./imagens/naoencontrado.png")):
            print('O produto:{} não possui saldo inicial na filial {}'.format(produto,filDesti))
            print('passando para o proximo da lista!')
            pg.press('enter')
            #incrmenta contador
            contador += 1
            pg.click(x=547, y=291)
            continue
        else:
            ut.clickOutrasAcoes()
            time.sleep(2)
            ut.clickRelacao()
            pg.write(quantidade[contador])
            time.sleep(1)
            ut.clickConfirmar()
            #perta sim 1
            ut.clickSim()
            contador += 1
            pg.click(x=547, y=291)

