#Pyautogui.press – Serve para pressionar uma tecla do seu teclado
#Pyautogui.write – Serve para escrever com o teclado (como se fosse você digitando)
#Pyautogui.click – Serve para clicar com o mouse
#pyautogui.hotkey - Aperta
#pyautogui.scroll - Rolar ex:pyautogui.scroll(+-1000) o numero é a qtde
#positivo e negativo é a direcao
#pyautogui.PAUSE - a cada comando de pyautogui espera o tempo determinado
#esses comandos funcionam mesmo sem mouse nem teclado. Se o teclado tiver fodido, da certo

#importando base de dados
import pandas
tabela = pandas.read_csv(r'C:\Users\alvar\OneDrive\Área de Trabalho\Data Science\Jornada Python\produtos.csv')
print(tabela)

import pyautogui
import time

pyautogui.PAUSE = 0.5

#aperta o botao windows
pyautogui.press('win')

#digita o nome do programa (chrome)
pyautogui.write('chrome')

#aperta enter
pyautogui.press('enter')

#Cria funcao para printar posicao do mouse depois de uma pausa de 5 segundos
#def checkMouse():
#    t.sleep(5)
#    print(p.position())

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.write('emailficticio@fakeemail.com')
pyautogui.press('tab')
pyautogui.write('senhafake123')
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab')
for linha in tabela.index: #index significa linha, column iria trazer coluna
    pyautogui.click(x=702, y=328)
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo'])) #tem que ta como string
    pyautogui.press('tab')
    if not pandas.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha, 'obs']))
#se obs tiver vazio, segue, se nao estiver vazio, digita o que esta no obs
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(5000)
