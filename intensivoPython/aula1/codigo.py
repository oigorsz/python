# 1 Abrir o sistema
# 2 Logar no sistema
# 3 Importar a base de dados
# 4 Cadastrar o produto
# 5 Repetir o processo

import pyautogui
import time
import pandas

#definir um tempo entre os códigos
pyautogui.PAUSE = 1

#1 Abrir o sistema
#usar a tecla windowns
pyautogui.press("Win")
#digitar o chrome
pyautogui.write("chrome")
#apetar enter
pyautogui.press("enter")

#colocando o link na barra de pesquisa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

#pressionar enter
pyautogui.press("enter")
time.sleep(3)

#2 Logar no sistema
#pegar a posição do login com arquivo auxiliar
#clicar na posição do login
pyautogui.click(x=611, y=350)
#escrever o login
pyautogui.write("monteiroigor@gmail.com")
#pressionar tab
pyautogui.press("tab")
#escrever a senha
pyautogui.write("minhasenha")
#pressionar tab
pyautogui.press("tab")
#pressionar enter
pyautogui.press("enter")

time.sleep(3)

#3 importar a base de dados
tabela = pandas.read_csv("produtos.csv")

#4 Cadastrat o produto

for linha in tabela.index:
    #clicar no codigo do produto
    pyautogui.click(x=566, y=253)
    #digitar o codigo do produto
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    #digitar a marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    #digitar o tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    #digitar categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    #digitar preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    #digitar o custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    #se não for um NaN
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        #digitar a obs
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    #pressionar enter
    pyautogui.press("enter")
    #volto para o inicio da pagina
    pyautogui.scroll(1000)
