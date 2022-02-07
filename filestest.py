with open('homsi.txt', 'r') as f:
    # print(f.read())
    print('Is this file readable ?:', f.readable())
    print('Is this file writable ?:', f.writable())
    # print(f.write('Alexander-Hacker\nMustapha-Networker\nBaba-Electricien'))
    print()
    print('Content of this files is: ')
    # print(f.readlines())
    print()
    for lines in f.readlines():
        print(lines)
f.close()
