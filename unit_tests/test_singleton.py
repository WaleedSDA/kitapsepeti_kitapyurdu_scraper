import unittest

from core.singleton_metaclass import Singleton


class TestSingleton(unittest.TestCase):
    """
    Test the Singleton metaclass with a simple class.
    """

    class SingletonClass(metaclass=Singleton):
        """
        A simple class using Singleton as its metaclass.
        """

    def test_singleton(self):
        """
        Test that two instances of SingletonClass are actually the same instance.
        """
        instance1 = self.SingletonClass()
        instance2 = self.SingletonClass()

        self.assertIs(instance1, instance2)


if __name__ == '__main__':
    unittest.main()
