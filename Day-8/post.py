import requests

data = {
    "username": "user",
    "password": "pass"
}
url = "https://httpbin.org/post"
response = requests.post(url, data)

if(response.status_code == 200):
    print("Login Success")
    print(response.text)
else:
    print("Login failed")

