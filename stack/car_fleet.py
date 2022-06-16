class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res, n_steps = 0, 0
        cars = sorted(zip(position, speed))
        print(cars)

        while cars:
            first = cars.pop()

            if first[0] + n_steps * first[1] < target:
                n_steps = (target - first[0]) / first[1]
                res += 1

        return res