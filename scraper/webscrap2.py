from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

myurl = 'https://www.newegg.com/p/pl?d=graphics+card'
#opening connection, grabbing the page:
uclient = uReq(myurl)
page_html = uclient.read()
uclient.close()

#parsing the html coz it is a big jumble of text that is why we call soup function:
# html parsing:
page_soup = soup(page_html, 'html.parser')
print(page_soup.h1) # grab header tag
print(page_soup.p) # grab p tag
print(page_soup.body.span)
#grab each product:
containers = page_soup.findAll('div', {'class': 'item-container'})
print('Numbers of Graphics cards are: ', len(containers))
# print(containers[0])
container = containers[0]
# print(container.a)
# print(container.div)
# print(container.div.div.a.img)
# print(container.div.div.a.img['title'])
print('-'*40)
count = 0
filename = 'products.csv'
f = open(filename, 'w')
headers = 'brand, product_name, shipping\n'
f.write(headers)

for container in containers:
    brand = container.div.div.a.img['title']
    title_container = container.findAll('a', {'class': 'item-title'})
    product_name = title_container[0].text
    shipping_container = container.findAll('li', {'class': 'price-ship'})
    shipping = shipping_container[0].text.strip()
    print('Brand: ', brand)
    print('Product_name: ', product_name)
    print('Shipping: ', shipping)
    f.write(brand + ',' +  product_name.replace(',', '|') + ', ' + shipping + '\n')
    count += 1
    print('-'*40)
f.close()

print(f'Number of Graphic cards is: {count}')


