# 이진 검색 알고리즘
# 중간값을 찾아서 같으면 위치에 삽입
# 다르면 작거나 큰쪽에 다시(재귀) 이분탐색을 진행
def input2List():
    newList = []
    while True:
        a = input()
        idx = 0
        if a == 'x':
            break
        start = 0
        end = len(newList) - 1
        while int(start) <= int(end):
            mid = (start + end) // 2
            if int(a) == int(newList[mid]):
                idx = mid
                break
            elif int(a) > int(newList[mid]):
                start = mid + 1
                if int(start) >= int(end):
                    idx = mid + 1
            else:
                end = mid - 1
                if int(start) >= int(end):
                    idx = mid
        newList.insert(idx, a)
    return newList

if __name__ == '__main__':
    result = input2List()
    print(result)
