import random
a='1234567890'
b='asdfghjklqwertyuiopzxcvbnm'
c='!@#$%^&*'
length=2

x=random.sample(a,length)
y=random.sample(b,length)
z=random.sample(c,length)
all=x+y+z
random.shuffle(all)
print(all)