# cook your dish here
import math
t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    ans = "no"
    for i in range(16):
        if (a^i)+(b^i)==c^i:
            ans="yes"
    print(ans)