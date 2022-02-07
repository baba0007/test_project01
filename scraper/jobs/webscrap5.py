# video course = https://www.youtube.com/watch?v=XVv6mJpFOb0    
# searching for jobs as python developer :

from bs4 import BeautifulSoup
import requests
import time

print('Put some skill that you are not familiar with: ')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get('https://www.pycareer.com/jobs/in/netherlands/').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.findAll('div', class_='listing-row')

    count = 0
    for index, job in enumerate(jobs):
        published_date = job.find('p', class_='t-small').text
        if 'uur' or 'dag' in published_date:
            compagny_name = job.find('span', class_='company').text.replace(' ', '') # replace() to move empty spaces
            skills = job.find('p', class_='t-medium text-muted').text
            more_info = job.h2.a['href'] # to access job link
        
            if unfamiliar_skill not in skills:
                with open(f'{index}.txt', 'w') as f:
                    
                    f.write(f'Company Name: {compagny_name} \n')
                    f.write(f'Skills needed: {skills} \n')
                    f.write(f'More info: {more_info} \n')
                    f.write(f'Posted date: {published_date} \n')
                print(f'File saved: {index}')
        
        
                count += 1

    
    print('-'*40)
    print(f'Total Jobs {count}')
    
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
        
        
        

