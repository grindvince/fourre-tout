def finobachi(n):
    fibo = [0,1]
    for i in range(n):
        if i > 1:
            fibo.append(fibo[i-2] + fibo[i-1])
        print (fibo[i])

finobachi(50)