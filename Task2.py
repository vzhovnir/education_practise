#!/usr/bin/env python3
for x in range(1,100):

    s=''
    if x % 3==0:
        s+="Fizz"
    elif x % 5==0:
        s+="Buzz"
    elif s=='':
        s=x
    print(s,end=' ') 