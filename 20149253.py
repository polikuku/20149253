N, M, V = map(int,input().split())
lists = [[] for i in range(N+1)]

check = [False for j in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    lists[a].append(b)
    lists[b].append(a)

for i in lists:
    i.sort()

#dfs
def dfs(V):
    check[V] = True
    string = str(V)+" "
    for e in lists[V]:
        if check[e] == False:
            string += dfs(e)
    return string

#bfs
def bfs(V):
    num_list = []
    check[V] = True
    string = str(V)+" "
    num_list.append(V)
    while len(num_list):
        v = num_list[0]
        del num_list[0]

        for e in lists[v]:
            if check[e] == False:
                check[e] = True
                string = string + str(e) + " "
                num_list.append(e)
    return string

print(dfs(V))
check = [False for j in range(N+1)]
print(bfs(V))
