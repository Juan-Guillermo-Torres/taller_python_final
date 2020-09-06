import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        primeraPoblacion = 35
        segundaPoblacion = 19.9
        primeraTasa = 0.02
        segundaTasa = 0.03

        while primeraPoblacion > segundaPoblacion:
            primeraPoblacion = primeraPoblacion + (primeraPoblacion * primeraTasa)
            segundaPoblacion = segundaPoblacion + (segundaPoblacion * segundaTasa)

        self.assertTrue(segundaPoblacion>primeraPoblacion)


if __name__ == '__main__':
    unittest.main()
