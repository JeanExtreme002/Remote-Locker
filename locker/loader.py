import json
import os
import random


def get_config(filename = "config.json"):

    """
    Função para obter as configurações de um arquivo JSON.
    """

    # Configuração padrão.
    config = {
        "host": "http://localhost:5000"
        }

    # Tenta abrir o arquivo de configurações.
    try:
        file = open(filename)
        config.update(json.loads(file.read()))
        file.close()

        return config

    # Informa o erro.
    except FileNotFoundError as error:

        print(error)
        return None

    # Cria um novo arquivo com todas as configurações.
    finally:
        with open(filename, "w") as file:

            data = json.dumps(config)
            file.write(data)


def get_token(filename = "token.txt", size = 100):

    """
    Função para obter token de acesso.
    """

    if not os.path.exists(filename):

        # Obtém caracteres de [a-Z 0-9].
        chars = [chr(id_) for id_ in range(ord("A"), ord("Z") + 1)]
        chars.extend([chr(id_) for id_ in range(ord("a"), ord("z") + 1)])
        chars.extend([str(num) for num in range(0, 10)])

        # Obtém um token aleatório.
        token = "".join([random.choice(chars) for i in range(size)])

        # Escreve o token dentro do arquivo especificado.
        with open(filename, "w") as file:
            file.write(token)

        return token

    else:
        
        # Obtém o token do arquivo especificado.
        with open(filename) as file:
            token = file.read()

        return token
