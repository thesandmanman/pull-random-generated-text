import requests
import bs4

# pull randomly generated text from "https://www.lipsum.com/feed/html" using requests.get
data = requests.get('https://www.lipsum.com/feed/html').text

# set the parser
soup = bs4.BeautifulSoup(data, 'lxml')

''' soup.find is used instead of find_all because text is
    placed in the first div which has class boxed and .find
    method will only get the first div'''

div = soup.find('div', class_='boxed')

p = div.find_all('p')

# print the paragraphs
for i in p:
    print(i.text)
