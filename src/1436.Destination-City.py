class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # find the city with 0 out degree
        d = {}

        for path in paths:
            city_from, city_to = path
            if city_from not in d:
                d[city_from] = 0
            if city_to not in d:
                d[city_to] = 0
            d[city_from] += 1
        
        for key in d:
            if d[key] == 0:
                return key
