import json
import requests as re

# resp = re.request(method="GET",url="http://216.10.245.166/Library/GetBook.php",params={"ID":"bcd5656"})
resp = re.get(url="http://216.10.245.166/Library/GetBook.php",params={"AuthorName":"John foe"})
print(resp.text)

#first way - here loads method returns dict where internally it changes to list
dict_resp = json.loads(resp.text)
print(dict_resp)
print(type(dict_resp))
print(dict_resp[0]['isbn'])

#another way

json_resp = resp.json()
print(json_resp)
print(json_resp[0]['aisle'])

assert resp.status_code==200
print(resp.headers)
assert 'application/json' in resp.headers['Content-Type']

print(resp.cookies)

for book in json_resp:
    if book['isbn'] == 'vsanh':
        print(book)
        break

expect_book ={
        "book_name": "Learn Appium Automation with Java",
        "isbn": "vsanh",
        "aisle": "3255"
    }

assert book == expect_book