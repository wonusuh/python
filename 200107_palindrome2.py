def f(x):
    qu = []
    st = []
    for char in x:
        print(qu, st)
        if char.isalpha():
            qu.append(char)
            st.append(char)
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True
print(f('찰진 의사의 진찰'))
