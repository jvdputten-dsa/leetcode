class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item not in ['+', '*', '-', '/']:
                stack.append(item)

            else:
                v = stack.pop()
                v2 = stack.pop()

                if item == '/':
                    v = int(float(v2) / float(v))
                else:
                    v = eval(v2 + item + v)
                stack.append(str(v))

        return stack[0]