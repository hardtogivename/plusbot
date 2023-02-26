 # https://docs.gopluslabs.io/

import requests

def hello():
    return "hello"

def GetsupportChain():
    # send a get request to this url https://api.gopluslabs.io/api/v1/supported_chains?name=nft_securit
    # and get the response
    response = requests.get("https://api.gopluslabs.io/api/v1/supported_chains?name=nft_securit")
    return response.json()


def getWalletDescriotion(walletaddr):
    return "Wallet: " + walletaddr

def getContractDescriotion(contractaddr):
    return "Contract: " + contractaddrpython