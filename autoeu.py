import pyautogui as py
import webbrowser
import time
import pyperclip

#Codigo de automatización para la página de la comunidad europea (españa) https://www.lidl.es/

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
    webbrowser.open("https://www.lidl.es/")
    time.sleep(3)   
    #mover a IDENTIFICATE
    py.moveTo(1351, 166)
    time.sleep(4)

    py.click()
    time.sleep(3)
    #mover a REGISTRATE
    py.moveTo(628, 925)
    py.click()
    time.sleep(3)
    
    #mover a la sección E-mail
    py.moveTo(424, 724)
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
    py.keyDown('tab')

    #CONFIRMAR E-MAIL
    py.write(text0, interval=0.1)
    # Esto hace un caracter '@' dependiendo del idioma del teclado en windows, el '2' podría ser 'q' 
    py.keyDown('altright')
    py.keyDown('2')
    py.keyUp('altright')
    py.keyUp('2')

    py.write(text1, interval=0.1)
    time.sleep(1)
    py.keyDown('tab')

    #escribir CONTRASEÑA
    py.write('Ab1234567*', interval=0.1)
    py.keyDown('tab')
    #confirmar CONTRASEÑA
    py.write('Ab1234567*')
    py.keyDown('tab')
    #mover a condición(1)
    py.moveTo(372, 572)
    time.sleep(1)
    py.click()
    #mover a condición(2)
    py.moveTo(372, 650)
    time.sleep(1)
    py.click()

    #mover a CREAR CUENTA
    py.moveTo(423, 890)
    time.sleep(1)
    py.click()


def login():
    webbrowser.open("https://www.lidl.es/")
    time.sleep(3)
    
    py.moveTo(1356,180)
    time.sleep(4)
    
    py.click()
    time.sleep(3)
    
    py.moveTo(450,730)
    time.sleep(1)
    
    py.click()

    py.write('osaad.bahij.54', interval=0.1)

    # Esto hace un caracter '@' dependiendo del idioma del teclado en windows, el '2' podría ser 'q' 
    py.keyDown('altright')
    py.keyDown('2')
    py.keyUp('altright')
    py.keyUp('2')
    
    py.write('hogee.com', interval=0.1)

    time.sleep(1)

    py.keyDown('tab')

    py.write('Ab1234567*', interval=0.1)

    py.moveTo(450,920)

    py.click()

def resetPass():
    webbrowser.open("https://www.lidl.es/")
    time.sleep(3)   
    #mover a IDENTIFICATE
    py.moveTo(1351, 166)
    time.sleep(4)

    py.click()
    time.sleep(3)

    #mover a OLVIDADO CONTRASEÑA
    py.moveTo(436, 877)
    py.click()
    time.sleep(3)
    #mover a EMAIL
    py.moveTo(435, 677)
    py.click()

    #escribir EMAIL
    py.write('osaad.bahij.54', interval=0.1)

    # Esto hace un caracter '@' dependiendo del idioma del teclado en windows, el '2' podría ser 'q' 
    py.keyDown('altright')
    py.keyDown('2')
    py.keyUp('altright')
    py.keyUp('2')

    py.write('hogee.com', interval=0.1)
    time.sleep(1)

    #mover a RESTABLECER CONTRASEÑA
    py.moveTo(462, 801)
    py.click()
    time.sleep(10)
    #Ir a "correo"
    webbrowser.open("https://generator.email/osaad.bahij.54@hogee.com")
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
    py.moveTo(842, 558)
    py.click()
    time.sleep(3)
    #clickear en el link de restablecimiento
    py.moveTo(842, 967)
    py.click()
    time.sleep(3)

    #mover a CONTRASEÑA
    py.moveTo(471, 781)
    py.click()
    time.sleep(1)
    #escribir CONTRASEÑA
    py.write('Ab1234567*', interval=0.1)
    py.keyDown('tab')
    #confirmar CONTRASEÑA
    py.write('Ab1234567*')
    time.sleep(1)
    #mover a GUARDAR
    py.moveTo(415, 943)
    py.click()


def modPass():
    login()
    time.sleep(5)
    #mover a Datos de Acceso
    py.moveTo(450, 621)
    py.click()
    time.sleep(4)

    #mover a Modificar Contraseña
    py.moveTo(1101, 717)
    py.click()
    time.sleep(4)

    #mover a Contraseña
    py.moveTo(760, 731)
    py.click()
    #escribir contraseña actual
    py.write('Ab1234567*', interval=0.1)
    py.keyDown('tab')
    #escribir nueva contraseña
    py.write('Ab1234567*', interval=0.1)
    py.keyDown('tab')
    #confirmar nueva contraseña
    py.write('Ab1234567*', interval=0.1)
    py.keyDown('tab')
    time.sleep(1)
    #mover a MODIFICAR CONTRASEÑA
    py.moveTo(750, 568)
    py.click()
    time.sleep(1)


    
#newAccount()
#login()
#resetPass()
#modPass()
    
