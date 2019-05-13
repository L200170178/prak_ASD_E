import re
f = open('indonesia.txt')
teks = f.read()
f.close()
p = r'\s(di\w+)'
strings = re.findall(p, teks)
if strings:
    print(strings)
else:
    print('[]')



