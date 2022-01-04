import random
a=['stone','papper','sizzer']
t=int(input("enter tournament lenth:"))
i=1
count=0
c=0
while i<=t:
    k=input("enter value:")
    com=random.choice(a)
    print("com value:",com)
    if k==com:
        print("match drew")
    elif (k=='stone' and com=='sizzer') or (k=='sizzer' and com=='papper') or (k=='papper' and com=='stone'):
        c=c+1
        print("k is:",c)
    else:
        count=count+1
        print("com is:",count)
    i=i+1
if c<=count:
    print("com is winner")
elif c==count:
    k=input("enter value:")
    com=random.choice(a)
    print("com value:",com)
    if (k=='stone' and com=='sizzer') or (k=='sizzer' and com=='papper') or (k=='papper' and com=='stone'):
        print("k is:")
    else:
        print("com is:")
else:
    print("k is winner")
