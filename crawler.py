import requests,sys
from bs4 import BeautifulSoup

def crawler(link):
    
    
    url=link
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    sttr=soup.get_text()
    return sttr
    



if __name__ == "__main__":
    crawler()