import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        letras = 'valorant'
        primero = letras[0]
        ultimo = letras[len(letras)-1]

        self.assertEqual('v', primero)
        self.assertEqual('t', ultimo)



if __name__ == '__main__':
    unittest.main()
