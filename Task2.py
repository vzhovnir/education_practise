#!/usr/bin/env python3
for x in range(1,100):
    s=''
    if x % 3==0:
        s+="Fizz"
    if x % 5==0:
        s+="Buzz"
    if not s:
        s = str(x)
    print(s, end=' ')
print("")