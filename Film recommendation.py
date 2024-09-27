import random


class Film:
    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

    def display_all(self):
        return f"Name: {self.name}\nGenre: {self.genre}\nRating: {self.rating}"


class Recommendation:
    def __init__(self):
        self.movies = []

    def add_movie(self, film):
        self.movies.append(film)

        print("Movie added")

    def recommend(self, preferred_genre):
        fitered_movie = [film for film in self.movies if preferred_genre == film.genre]

        if not fitered_movie:
            print("Not found movies for this genre")
            return

        recommended_film = random.choice(fitered_movie)
        return recommended_film.display_all()


recommendation = Recommendation()

while True:
    print("1. Add movie")
    print("2. Recommend movie")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter film name: ")
        genre = input("Enter film genre: ")
        rating = float(input("Enter film rating: "))

        film = Film(name, genre, rating)
        recommendation.add_movie(film)

    elif choice == '2':
        chosen_genre = input('enter the genre: ').lower()

        result = recommendation.recommend(chosen_genre)
        if result:
            print(result)

    else:
        print("INvalid choice")
