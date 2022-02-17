import pyautogui
import time
#Iniciando o codigo
pyautogui.alert("Iniciando o procedimento para abrir o Whatsapp Pessoal.")
pyautogui.PAUSE = 0.5
# abrir o Chrome
pyautogui.press('winleft')
pyautogui.write('Crhome')
pyautogui.press('enter')
time.sleep(1)
#Abrir WHATSAPP no Chrome
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(1)
#Whatsapp Pessoal está aberto.
time.sleep(5)
#pyautogui.alert("Whatsapp Pessoal está aberto!")
time.sleep(1)
#pyautogui.press('enter')
#Abrir o Edge
#pyautogui.alert("Iniciando o procedimento para abertura dos mensageiros de trabalho!!")
pyautogui.PAUSE = 0.5
#Abrir o Edge
pyautogui.press('winleft')
pyautogui.write('Edge')
pyautogui.press('enter')
time.sleep(1)
#Abrir do SKYPE
pyautogui.write('https://web.skype.com/')
pyautogui.press('enter')
time.sleep(1)
#Abrir uma aba
time.sleep(1)
pyautogui.hotkey('ctrl', 't')
#Abrir Whatsapp do trabalho
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(1)
#Abrir uma aba
time.sleep(1)
pyautogui.hotkey('ctrl', 't')
#Abrir Email do trabalho.
pyautogui.write('https://webmail-seguro.com.br/')
pyautogui.press('enter')
time.sleep(1)
#Abrir uma aba
time.sleep(1)
pyautogui.hotkey('ctrl', 't')
#Abrir ONDOCS.
pyautogui.write('https://ondocs.aspin.com.br/acesso-restrito/')
pyautogui.press('enter')
time.sleep(1)
#Abrir uma aba
time.sleep(1)
pyautogui.hotkey('ctrl', 't')
#Abrir o Gmail pessoal.
pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
pyautogui.press('enter')
time.sleep(2.5)

#Area de trabalho está aberta.
#pyautogui.alert("Mensageiros de trabalho estão abertos")
time.sleep(1)
pyautogui.press('enter')

#Abrindo o Teams
time.sleep(2.5)
pyautogui.press('winleft')
pyautogui.write('Teams')
pyautogui.press('enter')
time.sleep(5)

#Abrindo o Parallels
#pyautogui.hotkey('win', 'r')
#pyautogui.write('D:\Parallels\Client\APPServerClient.exe')
#pyautogui.press('enter')
#Clicando no Paralells para abrir o server.
#time.sleep(2.5)
#pyautogui.position(482, 292)
#pyautogui.mouseDown(button= 'right' )
#pyautogui.mouseUp()
#pyautogui.mouseDown()
#pyautogui.mouseUp()
#Automatização finalizada
pyautogui.alert("Sua automatização foi finalizada. Tudo funcionando como planejado. Parabéns!!")
time.sleep(1)
pyautogui.press('enter')