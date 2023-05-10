def r(num):
    if len(str(num))%2==0:
        d=len(str(num))//2
        e=1
        num=str(num)
        for y in range(d):
            if num[y]!=num[d*2-1-y]:
                e=0
        if e==1:
            print("Симметричное")
        else:
            print("Не Симметричное")
    else:
        print("Не Симметричное")


r(int(input()))            
