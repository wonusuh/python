def f(dic, start):
	path = [] # 방문한 곳을 기록
	qu = [start] # 큐에 시작점을 줄세움
	while qu: # qu 가 빌 때 까지 탐색을 계속
		vertex = qu.pop(0) # 큐의 맨 앞의 원소를 방문할 꼭짓점으로 설정
		if vertex not in path: # 꼭짓점이 방문된 적이 없다면 방문 기록에 추가
			path.append(vertex)
			for node in dic[vertex]: # 꼭짓점에 연결된 노드들 중 
				if node not in path: # 방문 안 된 곳 만을
					qu.append(node) # 큐에 줄세움
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
