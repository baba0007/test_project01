from bs4 import BeautifulSoup
import requests

'''
# google example:
result = requests.get('https://google.com')
print(result.status_code) # if we get 200 ==> site is accessed
# print(result.headers)
# for x in result.headers.items():
    # print(type(x))
src = result.content # will return page source code
# print(src)
soup = BeautifulSoup(src, 'lxml')
# print(soup.prettify)
links = soup.find_all('a')
# print(links)
for link in links:
    if 'Maps' in link.text:
        print(link)
        print(link.attrs['href'])
'''

#--------------------------------------------

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

# with open('test2.html', 'w') as f: #to create the test2.html from html_doc
    # f.write(html_doc)

with open('test2.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
# print(soup.prettify)
# to print the name of the tag:
# print(soup.b.name)
# to exctract all the link:
'''
urls = []
for link in soup.findAll('a'):
    urls.append(link.attrs['href'])
print(urls)
'''
#-----------------------------------------
'''
#print all the bold tag:
all_bold_tag = soup.findAll('b')
# print(all_bold_tag) #will return a list
for bold_tag in all_bold_tag:
    print(bold_tag)

print('-'*40)
'''
#-----------------------------------------
#to print all p tag:
'''
 for p_tag in soup.findAll('p'):
    print(p_tag)
'''
#---------------------------
'''
tag = all_bold_tag[2]
print(type(tag))
print('id =', tag['id'])
'''
#-------------------------------------
'''
# to print all id tag:
for id in all_bold_tag[2:]:
    print(id)
'''
#----------------------------------
# to see all attribute in a index of a list:
'''
tag = soup.findAll('b')[3]
print(tag)
print(tag.attrs)
print(tag.attrs.keys())
print(tag.attrs.values())
print(tag.attrs.items())
print('-'*40)
#change the vlaue of the first key of dictionary:
tag['another-attribute'] = 2
print(tag.attrs)
#Remove attributes and id:
del tag['id']
print(tag)
del tag['another-attribute']
print(tag)
'''
#------------------------------------
# Navigablestring:
tag = soup.findAll('b')[3]
print(tag)
print(tag.string)
#change the content of the string with another:
tag.string.replace_with('This is another string.')
print(tag)
print(tag.string)







