from bs4 import BeautifulSoup
import requests


url = requests.get('https://www.xataka.com/tag/python')

soup = BeautifulSoup(url.content, 'html.parser')
entries = soup.find_all('div',class_='abstract-content')
#print(entries)
#print(entries)

for entry in entries:
  title = entry.find("a").text
  summary = entry.find("p").text
  print(f"** {title} ** \n\n  {summary}\n\n")