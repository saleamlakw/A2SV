class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        recipesSet = set(recipes)
        suppliesSet = set(supplies)

        graph = defaultdict(list)
        indegree = defaultdict(int)

       
        allRecipes = []
        for idx in range(len(recipes)):
            checker = True
            res = []
            for ingredient in ingredients[idx]:
                checker = checker and (ingredient in suppliesSet or ingredient in recipesSet)
                if not checker:
                    break 

            
            if checker:
                allRecipes.append(recipes[idx])
                for ingredient in ingredients[idx]:
                    if ingredient in recipesSet:
                        graph[ingredient].append(recipes[idx])
                        indegree[recipes[idx]] += 1
                
        
        queue = deque()
        for ingredient in allRecipes:
            if indegree[ingredient] == 0:
                queue.append(ingredient)
        
        ans = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                ans.append(node)

                for nb in graph[node]:
                    indegree[nb] -= 1

                    if indegree[nb] == 0:
                        queue.append(nb)
        return ans

            


        