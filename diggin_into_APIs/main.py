import requests
import pandas as pd


def get_json():
    url = "https://catalog.chaldal.com/searchOld"

    payload = "{\n    \"apiKey\": \"e964fc2d51064efa97e94db7c64bf3d044279d4ed0ad4bdd9dce89fecc9156f0\",\n    \"storeId\": 1,\n    \"warehouseId\": 8,\n    \"pageSize\": 8000,\n    \"currentPageIndex\": 0,\n    \"metropolitanAreaId\": 1,\n    \"query\": \"\",\n    \"productVariantId\": -1,\n    \"canSeeOutOfStock\": \"true\",\n    \"filters\": []\n}"
    headers = {
        'authority': 'catalog.chaldal.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'accept': 'application/json',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'content-type': 'application/json, application/json',
        'origin': 'https://chaldal.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://chaldal.com/',
        'accept-language': 'en-US,en;q=0.9'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()


def save_to_csv(data):
    if data:
        df = pd.json_normalize(data)
        df.to_csv("chldal.csv")


def main():
    data = get_json()
    save_to_csv(data.get('hits'))
    print('Done')

if __name__ =='__main__':
    main()