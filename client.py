import requests
import sys
url = sys.argv[1]
myobj = {'data': ''}
myobj['data']=sys.argv[2]
x = requests.post(url, json = myobj)
print(x.text)
