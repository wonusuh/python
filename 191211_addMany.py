def addMany(* args): # 모든 변수를 입력받음.
    result = 0
    for i in args:
        result += i
    return result

print(addMany(1, 2, 3))
print(addMany(4, 5, 6, 7, 8, 9, 10))
