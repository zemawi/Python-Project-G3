movies = [
    {"id": 1, "title": "Avengers: Endgame", "showtime": "3:00 PM", "price": 10},
    {"id": 2, "title": "The Dark Knight", "showtime": "5:30 PM", "price": 12},
    {"id": 3, "title": "Inception", "showtime": "7:00 PM", "price": 11},
    {"id": 4, "title": "Interstellar", "showtime": "8:30 PM", "price": 13},
    {"id": 5, "title": "John Wick", "showtime": "9:45 PM", "price": 10},
    {"id": 6, "title": "Spider-Man: No Way Home", "showtime": "6:15 PM", "price": 12}
]


def movie_booking():
    for movie in movies:
        print(movie["id"], "Title:", movie["title"], "Showtime:", movie["showtime"], "Price:", movie["price"])
    movie_id = int(input("Choose the movie using id of the movies: "))
    no_tickets = int(input("How many tickets do you want? : "))
    return movie_id, no_tickets



def calc_payment(movie_id, no_tickets):
    for book in movies:
        if(movie_id == book["id"]):
            price = book["price"] * no_tickets
            print(f"Movie: {book['title']}")
            print(f"Showtime: {book['showtime']}")
            print(f"Number of tickets: {no_tickets}")
            print(f"Total amount: ${price}")

            another_book = (input("Do you want to book another movie(yes/no): ")).lower()
            if another_book in ['yes', 'y']:
                new_movie_id, new_no_tickets = movie_booking()
                calc_payment(new_movie_id, new_no_tickets)
                return
            elif another_book in ['no', 'n']:
                print("Your book is confirmed.\n")
                print("Thank you for your booking.")
                return
            else:
                print("Please enter yes or no.")
                
        
    print("Movie id not found please enter again: ")
    new_movie_id, new_no_tickets = movie_booking()
    calc_payment(new_movie_id, new_no_tickets)
        

print("Welcome To Movie Booking System!")
movie_id, no_tickets = movie_booking()
calc_payment(movie_id, no_tickets)
