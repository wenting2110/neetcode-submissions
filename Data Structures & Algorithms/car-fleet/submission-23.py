# gemini
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed), reverse = True)
        
        fleet = 0
        maxTime = 0

        for p, s in sorted_pairs:
            time = (target - p) / s
            if time > maxTime:
                fleet += 1
                maxTime = time
        
        return fleet