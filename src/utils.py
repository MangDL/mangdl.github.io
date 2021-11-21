import socket

from .exceptions import ConnectionError


def net_test(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    raise ConnectionError


def req_net(func):
    def wrapper(*argss, **kwargs):
        try:
            net_test("1.1.1.1")
            func()
        except ConnectionError:
            raise ConnectionError(
                "Please ensure connection to the internet before running this script.")

    return wrapper


def dict_merge(*dicts):
    return {k: d[k] for d in dicts for k in d}


def dict_extr(d, keys):
    return {k: d[k] for k in keys}
