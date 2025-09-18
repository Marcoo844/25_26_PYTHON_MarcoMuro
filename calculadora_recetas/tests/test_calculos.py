import unittest

class TestBasico(unittest.TestCase):
    def test_multiplicacion_basica(self):
        self.assertEqual(2 * 3, 6)

if __name__ == "__main__":
    unittest.main()
