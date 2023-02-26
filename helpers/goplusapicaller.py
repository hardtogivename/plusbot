# https://docs.gopluslabs.io/

import requests

def hello():
    return "hello"

def getsupportChain():
    # send a get request to this url https://api.gopluslabs.io/api/v1/supported_chains?name=nft_securit
    # and get the response
    response = requests.get("https://api.gopluslabs.io/api/v1/supported_chains?name=nft_securit")
    return response.json()


def getWalletDescriotion(walletaddr):
    return "Wallet: " + walletaddr

def getContractDescriotion(contractaddr):
    return "Contract: " + contractaddr


if __name__ == "__main__":
    print(getsupportChain())
    print(getWalletDescriotion("0x1234"))
    print(getContractDescriotion("0x1234"))