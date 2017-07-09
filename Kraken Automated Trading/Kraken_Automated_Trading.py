import krakenex
import Keys
import pprint
import json


k = krakenex.API(Keys.APIKey,Keys.privateKey)
response = k.query_public('Depth', {'pair': 'XETHZEUR', 'count': '1'})
pprint.pprint(json.dumps(response))
x = json.dumps(response['result'])
print(response['result']['XETHZEUR']['bids'][0][0])
