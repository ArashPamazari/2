fibo = []
n = 1
fibo.append(n)
n1= 1
fibo.append(n1)
tedad = int(input('tedad ra vared konid: '))

for i in range(2,tedad):
    seri = fibo[i-1] + fibo[i-2]

    fibo.append(seri)

print(fibo)    
