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
print(f("토마토"))
