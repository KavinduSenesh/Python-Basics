import requests
from bs4 import BeautifulSoup

# html_doc = """<html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie&quot; class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie&quot; class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie&quot; class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.title)
# print(soup.p)
# print(soup.a)

# p_tag = soup.find('p')
# print(p_tag)
# p_tags = soup.find_all('p')
# print(p_tags)

url  = "http://example.com"

response = requests.get(url)

if response.status_code == 200:
    print("Success")
    soup = BeautifulSoup(response.text, 'html.parser')
    h1_tag = soup.find('h1')	
    if h1_tag:
        print(h1_tag.text)
else:
    print("Error while fetching the page")