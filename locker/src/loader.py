from src.util import get_token
import json
import os


def load_config(filename):

    # Configuração padrão.
    config = {"host": "http://localhost:5000", "update": 1000}

    try:
        # Tenta abrir o arquivo de configurações.
        with open(filename) as file:
            content = file.read()

        # Atualiza e retorna as configurações.
        config.update(json.loads(content))
        return config

    except FileNotFoundError as error:
        print(error)

    finally:
        # Cria um novo arquivo de configurações com todas as chaves atualizadas.
        with open(filename, "w") as file:
            file.write(json.dumps(config))


def load_token(filename):

    # Carrega o token de um arquivo se ele existir.
    if os.path.exists(filename):

        with open(filename) as file:
            token = file.read()

    else:
        # Cria um novo token.
        token = get_token(size = 100)

        # Salva o token dentro do arquivo.
        with open(filename, "w") as file:
            file.write(token)

    return token
