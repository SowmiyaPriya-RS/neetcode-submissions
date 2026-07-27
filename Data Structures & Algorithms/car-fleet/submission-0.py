class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleet = 1
        prev_time = (target-cars[0][0])/cars[0][1]

        for i in range(1, len(cars)):
            curr = cars[i]
            curr_time = (target-curr[0])/curr[1]
            if(curr_time > prev_time):
                fleet += 1
                prev_time = curr_time
        return fleet

        