# covid-19 checkup:
from ast import Try
from covid import Covid
from extras import try_import

print('Covid-19 Status: ')
covid = Covid()
cases = covid.get_status_by_country_name(input('Enter Country name: ').lower())
# print(type(cases)) # it is a dictionary
print()
print('Numbers of cases: {}'.format(cases.get('confirmed')))
print(f'Numbers of dictionary keys is: {len(cases)}: ')
print('-' * 33)
for x in cases:  # x is key, cases[x] is value
    print(f'- {x}: {cases[x]}')

# print(f'cases = {cases}')
# print(cases.get('country')[0:2])

