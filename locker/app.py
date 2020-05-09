from infi.systray import SysTrayIcon
from src.loader import load_config, load_token
from src.locker import Locker
import os


def set_password(*args): 

    # Define uma nova senha.
    locker.set_password()


def show_server_status(text): 

    # Mostra o status do Locker.
    systray.update(hover_text = text)


def stop_locker(*args): 

    # Para a execução do Locker.
    locker.stop()


# Obtém configuração.
config = load_config("config.json")
if not config: os._exit(1)

# Obtém token de acesso.
token = load_token("token.txt")

# Cria instância de Locker.
locker = Locker(config["host"], token)

# Cria menu para ícone de bandeja.
menu_options = (("Set Password", None, set_password),)

# Cria e inicializa o ícone de bandeja.
systray = SysTrayIcon("icon.ico", "Locker (OFFLINE)", menu_options, on_quit = stop_locker)
systray.start()

# Inicia o Locker.
locker.run(show_server_status, config["update"])

# Fecha o ícone de bandeja.
systray.shutdown()