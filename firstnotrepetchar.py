from collections import *
#method1
s = "qwewwwwwweeerrreedgggheetdfdfl"

d = Counter(s)

print("d:",d)

for k,v in d.items():
    if(v == 1):
        print("first non repeting character is :",k)
        break
#method2
d1 = {}
count = 0
for i in s:
    if(d1.get(i) == None ):
        count = 1
        d1[i] = count
    else:
        count = count+1
        d1[i] = count

print("d1:",d1)

for k,v in d1.items():
    if(v == 1):
        print("first non repeting character is :",k)
        break
