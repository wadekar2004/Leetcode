class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph={}

        for(a,b),value in zip(equations,values):
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            graph[a].append((b,value))
            graph[b].append((a,1/value))
        def dfs(current,target,visited):
            if current not in graph:
                return -1.0

            if current == target:
                return 1.0
            visited.add(current)

            for nei,weight in graph[current]:
                if nei in visited:
                    continue
                result=dfs(nei,target,visited)

                if result !=-1.0:
                    return weight * result
            return -1.0
        ans=[]

        for start,end in queries:
            visited=set()
            result=dfs(start, end, visited)
            ans.append(result)
        return ans
    






            