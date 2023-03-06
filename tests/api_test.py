# Write unit tests for the API here for goplusapicaller

import unittest
import json

from helpers import goplusapicaller
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_hello(self):
        self.assertEqual(goplusapicaller.hello(), 'hello')

    def test_getContractScan_good(self):
        # good address
        json_string = json.dumps(goplusapicaller.getContractScan(
            1, "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"), indent=2)
        print("good address")

        #print(json_string)
        self.assertEqual(goplusapicaller.hello(), 'hello')

    def test_getContractScan_bad(self):
        # bad address
        addr ="0xe20747ac34e5e481c6cb6b687512258e5b534f6e"
        ret = goplusapicaller.getContractScan(56, addr)
        print("bad address")

        print(goplusapicaller.extractSafeyVector(addr, ret))
        # print(json_string)
        self.assertEqual(goplusapicaller.hello(), 'hello')
    def test_networkId(self):
        ret = goplusapicaller.getsupportChain()
        print(goplusapicaller.getsupportChain())
        # print(json_string)
        self.assertEqual(goplusapicaller.hello(), 'hello')   

if __name__ == '__main__':
    unittest.main()