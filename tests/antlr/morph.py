from sys import argv

content = ""
with open(argv[1]) as rfile:
    a:str = rfile.read(1)
    while a:
        if a=='<':
            a = rfile.read(1)
            while a and a!='>':
                content += a.upper()
                a = rfile.read(1)
        else:
            content += a
        a = rfile.read(1)

print(content)