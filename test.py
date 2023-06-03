# Write unit tests for the API here for goplusapicaller

import unittest
import json

from helpers import chainmetacaller
class TestCM(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_1(self):
        p = chainmetacaller.searchMeta("ethereum_mainnet","0x3b3fef06edcd9eb4b93a6d22091a81974d040e77c")
        print(p)
        self.assertEqual('xxx'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()