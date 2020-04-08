def f(x):
    qu = []
    st = []
    for char in x:
        if char.isalpha():
            qu.append(char)
            st.append(char)
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

if __name__ == "__main__":
    while True:
        print("검사하려는 회문을 입력하세요.", "종료하려면 x를 입력하세요.")
        inp = input()
        if inp == 'x':
            break
        result = f(inp)
        print(result)
