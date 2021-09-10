def fibonacci(numerp):
    a = 0
    b = 1
    print(a)
    for x in range(numerp):
        c = b+a
        a = b
        b = c
        
        print(a) 



fibonacci(5)