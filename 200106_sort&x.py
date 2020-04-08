def f():
    while True:
        a = input()
        if a == 'x':
            break
        n = len(newList)
        if n <= 0:
            newList.append(a)
        for i in range(n):
            if int(newList[i]) > int(a):
                newList.insert(i, a)
                break
            if i == n - 1:
                newList.append(a)
    return newList

newList = []

if __name__ == '__main__':
    result = f()
    print(result)
