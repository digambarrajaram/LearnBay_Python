class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __gt__(self, other):  # Greater than >
        if isinstance(other, Movie):
            return self.rating > other.rating
        return NotImplemented

    def __mul__(self, factor):  # Multiply rating by a number
        if isinstance(factor, (int, float)):
            boosted_rating = self.rating * factor
            if boosted_rating > 10:
                boosted_rating = 10.0  # Cap at 10
            return Movie(self.name, boosted_rating)
        return NotImplemented

    def __str__(self):
        return f"Movie: {self.name}, Rating: {self.rating}"


movie1 = Movie("Inception", 8.5)
movie2 = Movie("Interstellar", 9.0)

print(movie1 > movie2)       # False

boosted = movie1 * 2
print(boosted)               # Movie: Inception, Rating: 10.0 (max 10)
