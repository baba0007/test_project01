import psutil
batt = psutil.sensors_battery()
perc = str(batt.percent)
if int(perc) >= 100:
    print(f'Battery percent is FullCharged {perc}% :)')
else:
    print('Battery percent is draining :(')



