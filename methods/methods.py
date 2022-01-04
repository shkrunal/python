a=open('file.txt','r')
b=a.readlines()
for i in b:
    print(i)
    for j in i:
        print(j)
        