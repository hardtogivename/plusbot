# Write unit tests for the API here for goplusapicaller

import unittest

from helpers import goplusapicaller
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_hello(self):
        self.assertEqual(goplusapicaller.hello(), 'hello')

    def test_getContractScan(self):
        self.assertEqual(
            goplusapicaller.getContractScan(
                1, "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"),
            "Wallet: 0x1234")


if __name__ == '__main__':
    unittest.main()