import requests
from utilities.payloads import *
from utilities.configurations import *
from utilities.resources import *

url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
query = 'select * from Books'
add_resp = requests.post(url, json=buildPayloadFromDB(query), headers=headers)
print(add_resp.json())
resp_json = add_resp.json()
bookId = resp_json['ID']
print(bookId)

url = getConfig()['API']['endpoint'] + ApiResources.delBook
del_resp = requests.post(url, json={"ID": bookId}, headers=headers)

assert del_resp.status_code == 200
print(del_resp.json())
print(del_resp.json()['msg'])
assert 'deleted' in del_resp.json()['msg']

# Authentication
#
# se = requests.session()
# se.headers = getAccessToken()
#
# url = 'https://api.github.com/user'
# git_resp = requests.get(url, headers=getAccessToken())
# print(git_resp.status_code)
#
# url2 = 'https://api.github.com/user/repos'
# response = se.get(url2)
# print(response.status_code)
# print(response.json())
