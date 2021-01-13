with open('numere.txt','r') as f:
    a=f.readline()
    b=int(a)+3
    c=int(a)+int(b)-2
    s=int(a)+int(b)+int(a)
with open('bradut.txt','w') as f:
    f.write(str(s))