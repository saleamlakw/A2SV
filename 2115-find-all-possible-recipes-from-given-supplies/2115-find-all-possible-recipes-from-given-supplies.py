class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies=set(supplies)
        supplies2=set(recipes)
        # print(supplies,supplies2)
        graph=defaultdict(list)
        indegree=defaultdict(int)
        for i in range(len(recipes)):
            ch=True
            for ele in ingredients[i]:
                ch = ch and (ele in supplies or ele in supplies2)
                # print(ch)
            if ch:
               for ele in ingredients[i]:
                    if ele in recipes:
                        graph[ele].append(recipes[i])
                        indegree[recipes[i]]+=1
        # print(graph)
        # print(indegree)
        def topological_sort():
            
            result=[]

            queue=deque()
            for node in recipes:
                if indegree[node]==0:
                    queue.append(node)
            
            while queue:
                node=queue.popleft()
                result.append(node)

                for nb in graph[node]:
                    indegree[nb]-=1

                    if indegree[nb]==0:
                        queue.append(nb)
            # if len(result)!=n:
            #     return []
            return result
        return topological_sort()
