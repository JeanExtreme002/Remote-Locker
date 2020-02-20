from infi.systray import SysTrayIcon
from loader import *
from pyautogui import alert, password
import ctypes
import json
import os
import requests
import time


def close(*args):

    """
    Função para fechar o programa.
    """

    global stop
    stop = True


def set_password(*args):

    """
    Função para registrar uma nova senha.
    """

    # Obtém a senha.
    pwd = password("Enter the new password.", "Password")
    if not pwd: return

    try:
        response = requests.post(host + "/new", json = {"token": token, "password": pwd})

        # Verifica se a senha foi registrada com sucesso.
        if response.status_code == 403:
            alert("Invalid access token.", "Error")

        elif response.content.decode() == "OK":
            alert("Your new password has been successfully registered.", "Success")

    except:
        alert("Failed to attempt to send data to the server.", "Error")


# Obtém configuração.
config = get_config("config.json")
if not config: os._exit(1)

host = config["host"]
update = config["update"]

# Obtém token de acesso.
token = get_token("token.txt")

status = -1
stop = False

# Cria um ícone de bandeja.
systray = SysTrayIcon("icon.ico", "Locker (OFFLINE)", (("Set Password", None, set_password),), on_quit = close )
systray.start()

# Executa enquanto não for pedido para fechar o programa.
while not stop:

    # Espera um tempo a cada volta do bloco while.
    time.sleep(update / 1000)

    try:
        response = requests.post(host, json = {"token": token})

        # Verifica se o servidor está funcionando.
        if response.status_code in [200, 403] and status != response.status_code: 
            systray.update(hover_text = "Locker (online : {})".format(response.status_code))

        elif status != response.status_code:
            systray.update(hover_text = "Locker (offline : {})".format(response.status_code))

        status = response.status_code

        # Bloqueia o computador caso a resposta for "true".
        if response.content.decode() == "true":
            ctypes.windll.user32.LockWorkStation()

    except:

        # Informa que o servidor está offline.
        if status != -1:
            systray.update(hover_text = "Locker (OFFLINE)")
            status = -1

systray.shutdown()