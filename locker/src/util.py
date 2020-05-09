import ctypes
import random


def get_token(size = 100):

    # Obtém caracteres de [A-z 0-9].
    chars = [chr(id_) for id_ in range(ord("A"), ord("Z") + 1)]
    chars.extend([chr(id_) for id_ in range(ord("a"), ord("z") + 1)])
    chars.extend([str(num) for num in range(0, 10)])

    # Retorna um token com os caracteres obtidos.
    return "".join([random.choice(chars) for i in range(size)])


def lock_user_account():

    # Bloqueia a conta do usuário.
    ctypes.windll.user32.LockWorkStation()