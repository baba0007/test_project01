from bs4 import BeautifulSoup


with open('test1.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
for article in soup.findAll('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()

