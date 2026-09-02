class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph=[[] for _ in range(n)]



        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))
        visited=set()

        def dfs(city):
            visited.add(city)
            count=0


            for nei,dir in graph[city]:
                if nei in visited:
                    continue
                count+=dir
                count+=dfs(nei)
            return count
        return dfs(0)

