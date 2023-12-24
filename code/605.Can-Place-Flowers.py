class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while n > 0 and i < len(flowerbed):
            if flowerbed[i] == 0:
                # left side check
                if (i - 1 >= 0 and flowerbed[i-1] == 0) or i == 0:
                    # right side check
                    if (i + 1 < len(flowerbed) and flowerbed[i+1] == 0) or  i + 1 == len(flowerbed):
                        n -= 1
                        i += 2
                        continue
            
            i += 1

        if n == 0:
            return True
        
        return False