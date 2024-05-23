import shutil

def copy_file(filename_from, filename_to):
    shutil.copyfile(filename_from, filename_to)


with open('ИмяФайла', 'w') as f1:
    f1.write("Hello =)")

with open('Copy ИмяФайла', 'w'):
    pass

filename_from = 'ИмяФайла'
filename_to = 'Copy ИмяФайла'
copy_file(filename_from, filename_to)