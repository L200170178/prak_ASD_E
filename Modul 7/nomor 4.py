import re

f = open('KEI.htm', 'r', encoding='latin1')

teks = f.read()
f.close()


cari = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>\n<td>([0-9.]+)</td>', teks)

listbaru = []

for i in cari:
    a = (i[0],float(i[4]))
    listbaru.append(a)

print(listbaru)
    


