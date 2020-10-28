from bs4 import BeautifulSoup 
import requests 
def news():
  URL = "https://www.vogue.in/fashion"
  r = requests.get(URL) 
  soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
  table = soup.findAll('div',{'class':'Row-sc-8fdd29-1 AqRAd'})
  quotes=[]
  for row in table: 
      quote = {}
      if(row.a is not None):  
        quote['url'] = row.a['href'] 
        quote['text']=row.a.text
      if(row.img is not None):
        quote['img'] = row.img['src']
      if quote: 
        quotes.append(quote)
        
  quotes=quotes[1:-3]

  return quotes