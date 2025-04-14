import unittest
from main import say_hello

class TestSayHello(unittest.TestCase):
    def test_say_hello(self):
        result = say_hello("Gunasri")
        self.assertEqual(result, "Hello, Gunasri")
        
if __name__ == "__main__":
    unittest.main()
