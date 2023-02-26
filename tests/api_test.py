# Write unit tests for the API here for goplusapicaller

import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_hello(self):
        from helpers import goplusapicaller
        self.assertEqual(goplusapicaller.hello(), 'hello')


if __name__ == '__main__':
    unittest.main()