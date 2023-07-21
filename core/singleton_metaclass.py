import threading

lock = threading.Lock()


class Singleton(type):
    """
    this type class makes sure that any class uses it as a metaclass will be initialized only once
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
