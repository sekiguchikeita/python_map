import requests
import json

#レストラン検索APIのURL
url = "https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=a0a7fa96a0b160ac8df433901ccdee0a&latitude=35.67961390000001&freeword=カフェ&range=3&longitude=139.8649759"

#パラメータの設定
# params={}
# params["keyid"] = "a0a7fa96a0b160ac8df433901ccdee0a"
# params["freeword"] = "cafe"
# params["wifi"] = "1"
# params["coordinates_mode"]= 1
# params["coordinates_mode"] = "1"

# params["range"] = 3


#リクエスト結果
result_api = requests.get(url)
result_api = result_api.json()

#リクエスト結果出力
count = len(result_api['rest'])
for count in range(count):
    print(result_api['rest'][count]['name'])
    print(result_api['rest'][count]['category'])
    print(result_api['rest'][count]['address'])
    print(result_api['rest'][count]["url"])
    print('----------------------------------------------------')