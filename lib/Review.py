class Review:
    all_reviews=[]
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating
    
    def customer(self):
        return self.customer
    def restaurant(self):
        return self.restaurant
    def all(self):
        return Review.all_reviews
    
    
        
        # Example usage:
# customer1 = "Joyce"
# restaurant1 = "art cafe"
# rating1 = 4

# review1 = Review(customer1, restaurant1, rating1)

# print(review1.customer)  
# print(review1.restaurant)  
# print(review1.rating)  

