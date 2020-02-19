from infi.systray import SysTrayIcon
import ctypes
import json
import os
import requests


def close(*args):
    """
    Função para fechar o programa.
    """

    global stop

    stop = True


# Tenta abrir o arquivo de configurações.
try:
    file = open("config.json")

    config = json.loads(file.read())
    host = config.get("host", "http://localhost:80")

    file.close()

# Se não for possível, o programa é fechado.
except FileNotFoundError as error:
    print(error)
    os._exit(1)


status = False
stop = False

# Cria um ícone de bandeja.
systray = SysTrayIcon("icon.ico", "Locker (OFFLINE)", on_quit = close )
systray.start()

# Executa enquanto não for pedido para fechar o programa.
while not stop:

    try:
        response = requests.get(host)

        # Verifica se o servidor está funcionando.
        if response.status_code != 200: 
            raise ConnectionError

        # Informa que o servidor está online.
        elif not status:
            systray.update(hover_text = "Locker (ONLINE)")
            status = True

        # Bloqueia o computador caso a resposta for "true".
        if response.content.decode() == "true":
            ctypes.windll.user32.LockWorkStation()

    except:

        # Informa que o servidor está offline.
        if status:
            systray.update(hover_text = "Locker (OFFLINE)")
            status = False

