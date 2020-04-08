def sum(n):
    a = 0
    for i in range(1, n + 1):
        a += i
        print('a는 %s, i는 %s' %(a, i))
    return a

s=sum(5)
print(s)

s = sum(55)
print(s)
