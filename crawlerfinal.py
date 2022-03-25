
import requests
from bs4 import BeautifulSoup

import sys
import requests
from bs4 import BeautifulSoup
try:
  from googlesearch import search
except ImportError:
  print("No module named 'google' found")





def main(query):
	try:
		from googlesearch import search
	except ImportError:
		print("No module named 'google' found")

	# to search

	# query = sys.argv[1]
	out={}
	for j in search(query,tld='co.in', num=1, stop=10, pause=2):
		r = requests.get(j)
		soup = BeautifulSoup(r.content, 'html.parser')
		sttr=soup.get_text()
		sttr=sttr.replace('\n', ' ')
  		sttr.replace('@', ' ')
  		sttr.replace('#', ' ')
  		sttr.replace('%', ' ')
  		sttr.replace('&', ' ')
  		sttr.replace('^', ' ')
  		sttr.replace('*', ' ')
  		sttr.replace('1', ' ')
  		sttr.replace('2', ' ')
  		print(sttr.replace('9', ' '))
		out[j]= sttr
		#print(j)
	return out	

if __name__ == "__main__":
    main()



