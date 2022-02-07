# indirect execution
import modul3
modul3.f2()
modul3.calc(2, 3)
name = 'Amina'
modul3.name  # nothin will be returned coz we use if __name__ == '__main__':

print('-' * 10)
# from mathmodule import *
from mathmodule import get_fake_eno, get_fake_city

print(get_fake_eno())
print(get_fake_city())
