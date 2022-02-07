# video sajjad 009:
# Parsing Stackoverflow
# Showing results on the basis of paremeter
import requests
import urllib.request
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class'
response = requests.get(url)
# print(response)

# parsing:
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
answers = soup.findAll('div', {'class_', 'answer'})
# print(answers)
for answer in answers:
    votes = answer.find(
        'div', class_='js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center')
    # print(votes)
    solutions = answer.find(
        'div', class_='s-prose js-post-body')
    # print(solutions.text)

    for vote in votes:
        print('votes: ', vote)
    print('Solution :')
    for solution in solutions.text:
        print(solution, end='')
    print('-' * 40)
