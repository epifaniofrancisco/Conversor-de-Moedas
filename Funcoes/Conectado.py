"""

Módulo criado para verificar a conexão de internet no dispostivo.

"""

import socket


def conexao():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
