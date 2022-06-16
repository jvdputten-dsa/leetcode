def get_answer(i):
    if i % 15 == 0:
        return 'FizzBuzz'
    elif i % 5 == 0:
        return 'Buzz'
    elif i % 3 == 0:
        return 'Fizz'
    else:
        return str(i)


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [get_answer(i + 1) for i in range(n)]