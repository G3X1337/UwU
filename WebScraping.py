def oi():
	print("*******************************************************")
	print("Infection Security")
	print("Hacking, Securing and Developing")
	print("Coded by Al GQ Infection")
	print("Web Scraping Search Engine")
	print("*******************************************************")
oi()
from googlesearch import search
query = str(input("Keyword: "))
for URL in search(query=query):
  print(URL)