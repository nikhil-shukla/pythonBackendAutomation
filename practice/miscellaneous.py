import requests

cookie = {"first-name": "nikhil"}
res = requests.get(url="https://httpbin.org/cookies", cookies=cookie)
print(res.text)

se = requests.session()
se.cookies.update({"last-name": "shukla"})
res = se.get(url="https://httpbin.org/cookies", cookies={"my-id": "9"})
print(res.text)

# Allow Redirects
cookie = {"visit-month": "January"}
res = requests.get(url="http://rahulshettyacademy.com", allow_redirects=False, cookies=cookie, timeout=5, verify=False)
print(res.status_code)
print(res.history)

# Attachments

url = "https://petstore.swagger.io/v2/pet/9223372016854895000/uploadImage"
file = {'file': open("C://Users//shukl//OneDrive//Desktop//wolf_PNG23190.png", 'rb')}
res = requests.post(url=url, files=file)
print(res.status_code)
print(res.text)