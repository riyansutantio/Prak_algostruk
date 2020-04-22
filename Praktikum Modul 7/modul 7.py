import re

f = open('Indonesia.txt','r',encoding='latin1')
teks = f.read()
f.close()
#1
string1 = re.findall(r'(Me\w+)',teks)
string2 = re.findall(r'(\w+me\w+)\s',teks)
string3 = re.findall(r'(\w+me)\s',teks)
print(string1)
print(string2)
print(string3)

#2
string4 = re.findall(r'(Di\w+)\s(\w+)',teks)
print(string4)

#3
string5 = re.findall(r'(Di\s\w+)',teks)
print(string5)

#4
c = open('KEI.html','r',encoding='latin1')
file = c.read()
string6 = re.findall(r'title="([\w+]+)">',file)
string7 = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
x = []
for y in strings:
    x.append((y[0], float(y[1])))

print(x)
