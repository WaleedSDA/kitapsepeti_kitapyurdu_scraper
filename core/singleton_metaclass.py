import threading

lock = threading.Lock()


class Singleton(type):
    """
    Singleton is a metaclass that ensures only one instance of a class is created.

    Singleton uses Python's metaclass mechanism to override the standard object
    creation process. When a class uses Singleton as its metaclass, calling the class
    will return an existing instance of the class if it exists; otherwise, a new instance
    is created.

    This is implemented using a dictionary to hold instances of classes, with the classes
    themselves as keys.

    Singleton uses a threading.Lock to ensure that the singleton instance creation is
    thread-safe.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override the __call__ method to control object creation.

        If an instance of this class does not exist, create one and store it in the
        _instances dictionary. Otherwise, return the existing instance.

        Use a threading lock to ensure this operation is thread-safe.
        """
        if cls not in cls._instances:
            with lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



