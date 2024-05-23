from typing import List

v = []
vis = []
par = []
tmp = []


def dfs(node: int, p: int = -1) -> int:
    vis[node] = 1
    par[node] = p
    tmp.append(node)
    for i in v[node]:
        if vis[i] == 0:
            z = dfs(i, node)
            if z != -1:
                return z
        elif vis[i] == 1:
            sum = i
            while node != i:
                sum += node
                node = par[node]
                if node == i:
                    return sum
            return -1
    return -1


def largestSumCycle(N: int, Edge: List[int]) -> int:
    ans = -1
    global v, vis, par, tmp
    vis = [0] * N
    v = [[] for _ in range(N)]
    par = [-1] * N
    for i in range(N):
        if Edge[i] != -1:
            v[i].append(Edge[i])

    for i in range(N):
        if not vis[i]:
            ans = max(ans, dfs(i))
            for j in tmp:
                vis[j] = 2
            tmp.clear()

    return ans


# Driver code
if __name__ == '__main__':
    N = 4
    Edge = [1, 2, 0, -1]
    # Function Call
    ans = largestSumCycle(N, Edge)
    print(ans)