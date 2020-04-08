n = [5, 3, 1, 2, 4]

def getMin(lst):
    min = lst[0]
    for i in lst[1:]:
        if min > i:
            min = 1
    return min
print(getMin(n))

# n번 반복
for i in range(5):
    # print(i)
    print(getMin(n))

# 리스트에서 요소 삭제
el = ['a', 'b', 'c']
del el[1] # 'b'를 삭제
print(el)
