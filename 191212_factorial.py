def f(n):
    result = 0
    if n <= 1:
        return 1
    result = n * f(n - 1) # 재귀함수
    return result

print(f(4)) # 0!, 1! 은 어떻게 구하나?
