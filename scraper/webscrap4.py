#link for the video course : https://www.youtube.com/watch?v=XVv6mJpFOb0
from bs4 import BeautifulSoup

with open('test3.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    # courses_html_tags = soup.findAll('h5')
    # print(courses_html_tags)
    
    # for course in courses_html_tags:
        # print(course.text)
        
    course_cards =  soup.findAll('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] # i need only price without text that is why split()[-1]
        # print(course_name)
        # print(course_price)
        print(f'Course name {course_name} costs {course_price}.')

        