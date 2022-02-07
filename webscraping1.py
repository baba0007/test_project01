#Web scraping is the process of extracting data on the web.
# scraping has a lot of uses like SEO tracking, job tracking, news analysis, and — my favorite — sentiment analysis on social media!
#Is Web Scraping Legal?
# Talking about whether web scraping is legal or not, some websites allow web scraping and some don’t. 
# To know whether a website allows web scraping or not, you can look at the website’s “robots.txt” file. 
# You can find this file by appending “/robots.txt” to the URL that you want to scrape. For this example, 
# I am scraping Flipkart website. So, to see the “robots.txt” file, the URL is www.flipkart.com/robots.txt.

#import the library used to query a website
import urllib.request
from bs4 import BeautifulSoup #import the Beautiful soup functions to parse the data returned from the website
#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
#Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(wiki) #For python 3 use urllib.request.urlopen(wiki)
#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)
# print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.a) # Find all the links within page’s <a> tags
# find all links on this wiki page:
all_links =  soup.findAll('a')
for link in all_links:
    print(link.get('href'))

#Find the right table:
# all_tables=soup.find_all('table')
# print(all_tables)
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
# print(right_table)

#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))
#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G
print(df)