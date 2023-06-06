import json
import requests

# return a json object

def searchMeta(network : str, address : str) -> str:
    if network is None:
        network = "ethereum_mainnet"
    headers = {}
    payload = {}
    url = f"https://chainmeta.chaintool.ai/api/search_chainmeta?address={address}&chain={network}"
    response = requests.get(url, headers=headers, data=payload)

    if response.status_code != 200:
        raise Exception("Error: " + response.text)
    if response.text == "[]":
        return response.text
    return response.json()
class Label:
    def __init__(self, chain, address, entity, name, categories, source, submitted_by, submitted_on):
        self.chain = chain
        self.address = address
        self.entity = entity
        self.name = name
        self.categories = categories
        self.source = source
        self.submitted_by = submitted_by
        self.submitted_on = submitted_on

    def __str__(self):
        return f"""
        Entity: {self.entity}
        Chain: {self.chain}
        Address: {self.address}
        Name: {self.name}
        Categories: {", ".join(self.categories)}
        Source: {self.source}
        Submitted By: {self.submitted_by}
        Submitted On: {self.submitted_on}
        """

class LabelParser:
    @staticmethod
    def parse_labels(json_payloads: list) -> list:
        data = json_payloads
        labels = []
        for item in data:
            label = Label(
                item['chain'],
                item['address'],
                item['entity'],
                item['name'],
                item['categories'],
                item['source'],
                item['submitted_by'],
                item['submitted_on']
            )
            labels.append(label)
        return labels


if __name__ == "__main__":
    print ("hello")
    a = searchMeta("ethereum_mainnet", "0x0")
    print (a)