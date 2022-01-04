import re
from typing import Coroutine 
# . period  
# ^ starting 
# $ ending 
# [] range 
k=input("enter PASS :")
patt=r'^[A-Z][0-9]{0,4}.\w|[a-z]$'
c=re.match(patt,k)
if c:
    print("match")
else:
    print("unmatch")



        