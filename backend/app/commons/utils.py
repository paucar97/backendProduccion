import smtplib
import threading
def convertDatetime(tiempo):
    tiempo = tiempo.__str__()
    tiempo = tiempo.replace("T"," ")
    tiempo = tiempo[:-6]
    return tiempo

correoSistemaSec = "florestacksistemasec2@gmail.com"
contrasenaSistemaSec = "florestack123"

def envioCorreo(destinatarios,asunto,mensage):
    def funcion():
        try:
            me = 'Subject: {}\n\n{}'.format(asunto,mensage)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(correoSistemaSec,contrasenaSistemaSec)
            server.sendmail(correoSistemaSec,destinatarios,me)
            server.quit()
            print("ENVIO CORREOS")
        except Exception as ex:
            print("NO ENVIO CORREOS")
            print(str(ex))
        return

    x = threading.Thread(target=funcion)
    x.start()

    return


