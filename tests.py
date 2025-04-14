import unittest

class TestHello(unittest.TestCase):
    def test_say_hello(self):
        from main import say_hello
        self.assertEqual(say_hello("Gunasri"), "Hello, Gunasri!")

if __name__ == '__main__':
    unittest.main()
