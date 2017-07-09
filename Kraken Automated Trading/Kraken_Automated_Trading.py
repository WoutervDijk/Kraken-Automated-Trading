import krakenex
import Keys
import pprint
import json


k = krakenex.API(Keys.APIKey,Keys.privateKey)
response = k.query_public('Depth', {'pair': 'XETHZEUR', 'count': '1'})
y = json.loads(response)
x = json.dumps(response['result'])
pprint.pprint(x)
print('block soon')
pprint.pprint(response)
print('end')