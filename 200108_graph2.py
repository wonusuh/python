def f(dic, start):
    path = {} # []?
    qu = [start] # qu.append(start)
    done = set()
    while qu:
        qu_i = qu.pop(0) # ABF
        x = qu_i[-1] # F
        done.add(x)
        for i in dic[x]:
            if i not in done:
                qu.append(qu_i + i)
                if i not in path:
                    path[i] = len(qu_i)
                elif path[i] > len(qu_i):
                    path[i] = len(qu_i)
                else:
                    pass
    return path

if __name__ == '__main__':
    soc = {
        'A':set(['B', 'C', 'E']),
        'B':set(['A', 'C', 'F']),
        'C':set(['A', 'B', 'D', 'F']),
        'D':set(['C', 'E']),
        'E':set(['A', 'D', 'F']),
        'F':set(['B', 'C', 'E', 'G']),
        'G':set(['F']),
        'H':set(['I']),
        'I':set(['H']),
    }
    print(f(soc, 'A'))
