import random
s='abcdefghijklmnopqrtuvwxyzABCDEFIJKLMNOPQRSTUVWXYZ0123456789!+=-~±<>@#$%^&*(){}][:,;|/'
long=8
pwd="".join(random.sample(s,long))
print(pwd)


