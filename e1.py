import glob

myfiles = glob.glob('files/*.txt')

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())


# glob functions allow me to read content of multiple files, function of a file path, very useful going forward