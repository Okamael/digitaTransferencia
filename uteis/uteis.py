import pyautogui as pg
import time
def compoemBusca (fil,produto):
    textTratado = fil+produto
    return textTratado

def clickOutrasAcoes():
    pg.click(x=1368, y=148)
    

def clickPesquisar():
    pg.click(x=1353, y=320)
   


def clickOk():
    pg.click(x=878, y=557)
    

def clickDestino():
    pg.click(x=665, y=527)
    

def clickRelacao():
   pg.click(x=1359, y=257)

def clickConfirmar():
    pg.click(x=1096, y=290)

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