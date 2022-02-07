from speedtest import Speedtest

st = Speedtest()

option = int(input('''Enter You choise:

1) Download Speed
2) Upload Speed
3) Ping

Your choise:  '''))

if option == 1:
    print(f'Download Speed is: {st.download()}')
elif option == 2:
    print(f'Upload Speed is: {st.upload()}')
elif option == 3:
    servernames = []
    st.get_servers(servernames)
    print(st.results.ping)
else:
    print('Please enter the correct choise !')
