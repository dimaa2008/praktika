def makar6(ch):
    kol = 0
    while ch> 0:
        ch = ch // 10
        kol = kol + 1
    print(kol)

    
ch = int(input())
makar6(ch)
