def is_exe(filename):
    try:
        with open(filename, 'rb') as file:
            signature = file.read(2)
            return int(signature == b'MZ')
    except:
        return 'Файл не был найден'


filename = 'Setup.exe'
print(is_exe(filename))