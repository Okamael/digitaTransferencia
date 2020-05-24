import pyautogui as pg
import time
def compoemBusca (fil,produto):
    textTratado = fil+produto
    return textTratado

def clickOutrasAcoes():
    pg.click(x=1655, y=158)
    

def clickPesquisar():
    pg.click(x=1680, y=349)
   


def clickOk():
    pg.click(x=1053, y=653)
    

def clickDestino():
    pg.click(x=831, y=618)
    

def clickRelacao():
   pg.click(x=1658, y=285)
   
def clickConfirmar():
    pg.click(x=1247, y=379)

def clickSim():
    while (True):
        atencao = pg.locateCenterOnScreen("./imagens/atencao.png")
        if(atencao is not None):
            break
    pg.press("s",presses=3,interval=2)

def buscaProduto(filial,produto):
    clickOutrasAcoes()
    time.sleep(2)
    #clicar pesquisar
    clickPesquisar()
    time.sleep(2)
    pg.press('enter')
    #digita a pesquisa fil origem e produto
    pg.write(compoemBusca(filial,produto))
    clickOk()
    pg.press('enter')

def buscaProdutoDestino(filial,produto):
    clickOutrasAcoes()
    time.sleep(2)
    #clicar pesquisar
    clickPesquisar()
    time.sleep(2)
    pg.press('enter')
    #digita a pesquisa fil origem e produto
    pg.write(compoemBusca(filial,produto))
    clickDestino()
    clickOk()
    pg.press('enter')