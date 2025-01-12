import requests

# response = requests.get("https://api.github.com/events")

# print(response)
# print(response.status_code)

# if response.status_code == 200:
#     print("Success")
#     # content_type = response.headers['Content-Type']
#     # print(content_type)
#     # print(response.text)

#     if 'application/json' in response.headers['Content-Type']:
#         data = response.json()
#         print(data)
# else:
#     print("Error while fetching the page")

# print(response.headers) 

# url = "https://example.com"

# params = {'q' : 'python', 'category' : 'books'}
# response = requests.get(url, params=params)

# if response.status_code == 200:
#     print(response.url)
#     print(response.text)
# else:
#     print("Error while fetching the page")
 

url = "https://httpbin.org/get"

user_name = "user"
password = "pass"

response = requests.get(url, auth=(user_name, password))

if response.status_code == 200:
    print("Authentication Success")
    print(response.text)
else:
    print("Error while fetching the page")\
    
