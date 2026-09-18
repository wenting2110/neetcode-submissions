# gemini
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:     
        # 按照位置由大到小（由近到遠）排序，並計算到達終點所需時間
        sorted_pairs = sorted(zip(position, speed), reverse = True)
        
        fleet = 0
        maxTime = 0     # 紀錄前一方車隊到達終點的最長時間

        for p, s in sorted_pairs:
            time = (target - p) / s
            
            # 如果這輛車到達時間大於前面的車隊時間，代表它無法追上，會自成一個新車隊
            if time > maxTime:
                fleet += 1
                maxTime = time  # 更新目前最慢（領頭）車隊的時間
        
        return fleet