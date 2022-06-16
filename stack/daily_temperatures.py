class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [temperatures[0]]
        result = []

        for temp in temperatures[1:]:

            if stack and temp <= stack[-1]:
                stack.append(temp)

            else:
                while stack and temp > stack[-1]:
                    result.append(len(stack))
                    stack.pop()
                stack.append(temp)

        return result