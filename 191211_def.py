def f(x):
    l = len(x)
    i = s.find(x) # 내장함수 find()
    if i == -1:
        print("ㅋㅋㅋ")
    print("%s는 %s번째 입니다." %(s[i:i + l], l))

s = "python is the best choice"
f("python") # 왜 오류가 나는가?
f("is")
f("the")
f("best")
f("choice") # 왜 오류가 나는가?
f("django") # 왜 오류가 나는가?
