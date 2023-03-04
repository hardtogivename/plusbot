# https://docs.gopluslabs.io/

import requests


def hello():
    return "hello"


def getsupportChain():
    # send a get request to this url https://api.gopluslabs.io/api/v1/supported_chains?name=nft_securit
    # and get the response
    response = requests.get(
        "https://api.gopluslabs.io/api/v1/supported_chains")
    if response.status_code != 200:
        raise Exception("Error: " + response.text)
    response = response.json()
    return dict(map(lambda x: (x["name"], x["id"]), response["result"]))


def getNFTSecurity(network, address):
    if network is None:
        network = 1

    url = "https://api.gopluslabs.io/api/v1/nft_security/{}?contract_addresses={}".format(
        network, address)
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        raise Exception("Error: " + response.text)
    return response.json()["result"]


def getWalletDescriotion(walletaddr):
    return "Wallet: " + walletaddr


def getContractScan(network, address) -> dict:
    if network is None:
        network = 1

    url = "https://api.gopluslabs.io/api/v1/token_security/{}?contract_addresses={}".format(
        network, address)
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        raise Exception("Error: " + response.text)
    return response.json()["result"]


def extractSafeyVector(address, contractResult):
    firstItem = contractResult[address.lower()]
    # print(firstItem)
    return {
        "is_blacklisted": bool(int(firstItem["is_blacklisted"])),
        "is_honeypot": bool(int(firstItem["is_honeypot"])),
        "is_in_dex": bool(int(firstItem["is_in_dex"])),
        "is_open_source": bool(int(firstItem["is_open_source"])),
        "is_proxy": bool(int(firstItem["is_proxy"])),
        "can_take_back_ownership":
        bool(int(firstItem["can_take_back_ownership"])),
        "buy_tax": (firstItem["buy_tax"]),
    }


if __name__ == "__main__":
    import json
    print(dict(getsupportChain()))
    print("--------")
    print(getWalletDescriotion("0x1234"))
    print("--------")
    print(
        json.dumps(getContractScan(
            1, "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"),
                   indent=2))
    print("--------")
    print(
        json.dumps(getNFTSecurity(
            1, "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"),
                   indent=2))
