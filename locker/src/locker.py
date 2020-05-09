from pyautogui import alert, password
from src.util import lock_user_account
import requests
import time


class Locker(object):

    def __init__(self, host, token):

        self.__host = host
        self.__token = token


    def __get_status(self, response):

        # Informa que o Locker está funcionando.
        if response.ok: 
            return "Locker (online : {})".format(response.status_code)

        # Informa que o Locker não está funcionando mas o servidor continua ativo.
        else:
            return "Locker (offline : {})".format(response.status_code)


    def get_offline_message(self):

        # Informa que o servidor não está funcionando.
        return "Locker (OFFLINE)"


    def run(self, status_callback, update = 1000):

        self.__stop = False
        self.__status = -1

        while not self.__stop:

            # Espera um tempo a cada volta do bloco while.
            time.sleep(update / 1000)

            try:
                # Obtém a resposta do servidor.
                response = requests.post(self.__host, json = {"token": self.__token})

                # Envia o novo status do servidor
                if response.status_code != self.__status:
                    self.__status = response.status_code
                    status_callback(self.__get_status(response))

                # Bloqueia o computador caso a resposta seja "true".
                if response.content.decode() == "true":
                    lock_user_account()

            except:
                # Informa que o servidor está offline.
                if self.__status != -1:
                    status_callback(self.get_offline_message())
            
                self.__status = -1


    def set_password(self):

        # Obtém um nova senha para ser registrada.
        pwd = password("Enter the new password.", "Password")
        if not pwd: return

        try:
            # Envia a nova senha junto com o token de acesso.
            response = requests.post(self.__host + "/new", json = {"token": self.__token, "password": pwd})

            # Verifica se houve um erro com o token de acesso.
            if response.status_code == 403:
                alert("Invalid access token.", "Error")

            # Verifica se a senha foi registrada com sucesso.
            elif response.ok:
                alert("Your new password has been successfully registered.", "Success")

            # Informa que houve algum problema ao registrar a senha.
            else:
                alert("Oops, it looks like something is wrong.")

        except:
            # Informa que não foi possível realizar a comunicação com o servidor.
            alert("Failed to attempt to send data to the server.", "Error")


    def stop(self):

        # Interrompe a execução do Locker.
        self.__stop = True
