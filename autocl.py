import pyautogui as py
import webbrowser
import time
import pyperclip

#Codigo de automatización para la página de Chile.
#Este sitio no tiene la opción de modificar contraseña estando dentro de la sesión.
#la resolución de pantalla para las coordenadas de este código son 1920x1080

def newAccount():
    #obtener un correo
    webbrowser.open("https://generator.email/")
    time.sleep(4)
    py.moveTo(885, 313)
    py.click()
    time.sleep(3)
    py.moveTo(885, 388)
    py.click()
    time.sleep(3)
    py.moveTo(1268, 292)
    py.click()
    time.sleep(1)

    text = pyperclip.paste()

    #como pyautogui no puedo escribir el @ se debe separar el correo en dos strings
    split = text.split("@")
    text0 = split[0]
    text1 = split[1]

    #ir a la pagina a registrar
    webbrowser.open("https://www.flow.cl/")
    time.sleep(3)

    #mover a REGISTRATE
    py.moveTo(1311, 133)
    py.click()
    time.sleep(3)

    #mover a la sección E-mail
    py.moveTo(546, 347)
    time.sleep(1)

    py.click()
    #escribir el correo
    py.write(text0, interval=0.1)
    # Esto hace un caracter '@' dependiendo del idioma del teclado en windows, el '2' podría ser 'q' 
    py.keyDown('altright')
    py.keyDown('2')
    py.keyUp('altright')
    py.keyUp('2')

    py.write(text1, interval=0.1)
    time.sleep(1)
    py.press('tab')

    #CONFIRMAR E-MAIL
    py.write(text0, interval=0.1)
    # Esto hace un caracter '@' dependiendo del idioma del teclado en windows, el '2' podría ser 'q' 
    py.keyDown('altright')
    py.keyDown('2')
    py.keyUp('altright')
    py.keyUp('2')

    py.write(text1, interval=0.1)
    time.sleep(1)
    py.press('tab')

    #escribir CONTRASEÑA
    py.write('Ab1234567*', interval=0.1)
    py.press('tab')
    #confirmar CONTRASEÑA
    py.write('Ab1234567*')
    py.press('tab')
    #mover a condiciónes
    py.moveTo(400, 743)
    time.sleep(1)
    py.click()

    #mover a ENVIAR
    py.moveTo(1010, 830)
    py.click()


def login():
    webbrowser.open("https://www.flow.cl/")
    time.sleep(5)
    
    py.moveTo(1455,133)
    time.sleep(4)
    py.click() 

    time.sleep(3)
    py.moveTo(1181,413)
    py.click()
    py.click()
    py.click()
    #escribir el correo
    py.write('moataz_4124', interval=0.1)
    # Esto hace un caracter '@' dependiendo del idioma del teclado en windows, el '2' podría ser 'q' 
    py.keyDown('altright')
    py.keyDown('2')
    py.keyUp('altright')
    py.keyUp('2')

    py.write('utime.space', interval=0.1)
    time.sleep(1)
    py.press('tab')
    #escribir CONTRASEÑA
    py.write('Ab1234567*', interval=0.1)
    py.press('enter')



def resetPass():
    webbrowser.open("https://www.flow.cl/")
    time.sleep(5)
    #mover a INGRESA
    py.moveTo(1455,133)
    time.sleep(4)
    py.click()
    time.sleep(3)
    #mover a "no recuerdo mi password"
    py.moveTo(836,609)
    time.sleep(1)
    py.click()
    time.sleep(3)

    #mover a correo
    py.moveTo(1183,495)
    py.click()
    #escribir el correo
    py.write('moataz_4124', interval=0.1)
    # Esto hace un caracter '@' dependiendo del idioma del teclado en windows, el '2' podría ser 'q' 
    py.keyDown('altright')
    py.keyDown('2')
    py.keyUp('altright')
    py.keyUp('2')

    py.write('utime.space', interval=0.1)
    time.sleep(1)
    py.press('enter')
    #Ir a "correo"
    webbrowser.open("https://generator.email/moataz_4124@utime.space")
    time.sleep(10)
    #mover a REFRESH
    py.moveTo(1045, 313)
    py.click()
    time.sleep(4)
    
    #mover al correo correspondiente
    py.moveTo(1000, 530)
    py.click()
    time.sleep(1)
    #clickear en el link de restablecimiento
    py.moveTo(947, 540)
    time.sleep(3)
    py.click()
    time.sleep(5)

    #mover a CONTRASEÑA
    py.moveTo(998, 415)
    py.click()
    time.sleep(1)
    #escribir CONTRASEÑA
    py.write('Ab1234567*', interval=0.1)
    py.keyDown('tab')
    #confirmar CONTRASEÑA
    py.write('Ab1234567*')
    time.sleep(1)
    py.press('enter')

#newAccount()
#login()
#resetPass()


