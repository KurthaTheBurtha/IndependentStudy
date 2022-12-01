t = int(input())
for i in range(t):
    n = int(input())
    a = input().split()
    index = 1
    ans = "no"
    while index<len(a):
        l_arr,r_arr,s1,s2= [],[],0,0
        for i in range(n):
            if i<index:
                l_arr.append(int(a[i]))
            else:
                r_arr.append(int(a[i]))
        for i in l_arr:
            s1+=i
        for i in r_arr:
            s2+=i
        product = s1*s2
        if product%2==1:
            ans = "yes"
        index+=1
    print(ans)