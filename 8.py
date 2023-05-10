def d(num):
    s=0
    for p in range(1,num+1):
        if num%p==0:
            s=s+1
    if s==2:
        print("true")
    else:
        print("false")


d(int(input()))
