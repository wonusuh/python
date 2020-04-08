a = '찰진 의사의 진찰'
qu = []
st = []
isPld = True
for char in a:
    print(qu, st)
    if char.isalpha():
        qu.append(char)
        st.append(char)
while qu:
    if qu.pop(0) != st.pop():
        isPld = False
        break
print(isPld)
