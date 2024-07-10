class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for ele in logs:
            if ".." in ele:
                if stack:
                    stack.pop()
            elif "." in ele:
                continue
            else:
                stack.append(ele)
        return len(stack)
