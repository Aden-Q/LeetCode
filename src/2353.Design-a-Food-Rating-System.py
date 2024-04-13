class FoodRatings:
    # a map for cuisine --> (food, rating), value as a maxHeap
    # a map between food --> cuisine, to quickly get the cuisine of a food

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_food_rating = defaultdict(list)
        for idx in range(len(foods)):
            cuisine = cuisines[idx]
            food = foods[idx]
            rating = ratings[idx]
            heapq.heappush(self.cuisine_to_food_rating[cuisine], (-rating, food))
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        heapq.heappush(self.cuisine_to_food_rating[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # lazy deletion
        rating, food = self.cuisine_to_food_rating[cuisine][0]
        while -rating != self.food_to_rating[food]:
            heapq.heappop(self.cuisine_to_food_rating[cuisine])
            rating, food = self.cuisine_to_food_rating[cuisine][0]
        
        return food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)