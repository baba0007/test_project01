import platform
uname = platform.uname()
print(f'System name :{uname.system}')
print(f'Node name :{uname.node}')
print(f'Release :{uname.release}')
print(f'Version :{uname.version}')
print(f'Machine name :{uname.machine}')
print(f'Processor :{uname.processor}')