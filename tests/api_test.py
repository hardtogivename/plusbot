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

    # def test_getContractScan(self):
    #     self.assertEqual(
    #         goplusapicaller.getContractScan(
    #             1, "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"),
    #         "Wallet: 0x1234")

    def langMatch(self):
        import nltk

        from nltk.util import ngrams

        # Define the list of NFT names
        nft_names = [
            "CryptoKitties", "Axie Infinity", "Bored Ape Yacht Club",
            "Pudgy Penguins", "Meebits", "Art Blocks", "World of Women",
            "Mutant Ape Yacht Club", "Cool Cats", "Loot"
        ]

        # Define the input string to search for fuzzy matches
        input_string = "Axie Infiniti"

        # Define the length of the ngrams to use for matching
        ngram_length = 3

        # Define a function to calculate the Jaccard similarity between two sets
        def jaccard_similarity(s1, s2):
            intersection = len(s1.intersection(s2))
            union = len(s1.union(s2))
            return intersection / union

        # Create an ngram set from the input string
        input_ngrams = set(ngrams(input_string.lower(), ngram_length))

        # Loop over the NFT names and calculate the Jaccard similarity of each name to the input string
        for name in nft_names:
            name_ngrams = set(ngrams(name.lower(), ngram_length))
            similarity = jaccard_similarity(input_ngrams, name_ngrams)
            print(f"{name}: {similarity}")
        
        self.assertEqual(goplusapicaller.hello(), 'hello')



if __name__ == '__main__':
    unittest.main()
