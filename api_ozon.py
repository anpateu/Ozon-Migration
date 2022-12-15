import requests

class OzonAPI:
    def __init__(self, client_id, api_key):
        self.client_id = client_id
        self.api_key = api_key

    def create_products(self, items):
        endpoint = 'https://api-seller.ozon.ru/v1/product/import-by-sku'
        headers = {
            "Client-Id": self.client_id,
            "Api-Key": self.api_key
            }
        data = {
            "items": items
            }
        response = requests.post(endpoint, headers=headers, json=data)

        if response.status_code == 200:
            print(response.json())

        else:
            print("Error: Request returned status code", response.status_code, "with message", response.reason)