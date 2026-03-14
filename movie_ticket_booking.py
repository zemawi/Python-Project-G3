def movie_ticket_booking():
    # Movie database with titles, showtimes, and prices
    movies = {
        1: {"title": "Avatar: The Way of Water", "showtimes": ["10:00 AM", "1:30 PM", "5:00 PM", "8:30 PM"], "price": 12.50},
        2: {"title": "Black Panther: Wakanda Forever", "showtimes": ["11:00 AM", "2:30 PM", "6:00 PM", "9:30 PM"], "price": 10.00},
        3: {"title": "Top Gun: Maverick", "showtimes": ["12:00 PM", "3:30 PM", "7:00 PM", "10:30 PM"], "price": 11.00},
        4: {"title": "Spider-Man: No Way Home", "showtimes": ["10:30 AM", "2:00 PM", "5:30 PM", "9:00 PM"], "price": 13.00},
        5: {"title": "The Batman", "showtimes": ["11:30 AM", "3:00 PM", "6:30 PM", "10:00 PM"], "price": 12.00}
    }
    
    bookings = []
    total_cost = 0.0
    
    print("🎬 Welcome to Movie Theater Booking System! 🎬")
    print("=" * 50)
    
    while True:
        # Display available movies
        print("\n📽️  Available Movies:")
        print("-" * 30)
        for num, movie in movies.items():
            print(f"{num}. {movie['title']} - ${movie['price']:.2f}")
            print(f"   Showtimes: {', '.join(movie['showtimes'])}")
            print()
        
        # Get movie selection
        while True:
            try:
                movie_choice = int(input("Enter the movie number (1-5): "))
                if 1 <= movie_choice <= 5:
                    break
                else:
                    print("❌ Please enter a valid movie number between 1 and 5.")
            except ValueError:
                print("❌ Please enter a valid number.")
        
        selected_movie = movies[movie_choice]
        
        # Display showtimes for selected movie
        print(f"\n🕐 Showtimes for {selected_movie['title']}:")
        for i, showtime in enumerate(selected_movie['showtimes'], 1):
            print(f"{i}. {showtime}")
        
        # Get showtime selection
        while True:
            try:
                showtime_choice = int(input("Enter showtime number: "))
                if 1 <= showtime_choice <= len(selected_movie['showtimes']):
                    break
                else:
                    print(f"❌ Please enter a number between 1 and {len(selected_movie['showtimes'])}.")
            except ValueError:
                print("❌ Please enter a valid number.")
        
        selected_showtime = selected_movie['showtimes'][showtime_choice - 1]
        
        # Get number of tickets
        while True:
            try:
                num_tickets = int(input("Enter number of tickets: "))
                if num_tickets > 0:
                    break
                else:
                    print("❌ Please enter a positive number of tickets.")
            except ValueError:
                print("❌ Please enter a valid number.")
        
        # Calculate cost
        booking_cost = selected_movie['price'] * num_tickets
        
        # Display booking details and confirm
        print(f"\n📋 Booking Details:")
        print(f"Movie: {selected_movie['title']}")
        print(f"Showtime: {selected_showtime}")
        print(f"Number of tickets: {num_tickets}")
        print(f"Price per ticket: ${selected_movie['price']:.2f}")
        print(f"Total cost: ${booking_cost:.2f}")
        
        confirm = input("\nConfirm booking? (yes/no): ").lower().strip()
        
        if confirm == 'yes':
            # Add to bookings
            booking = {
                "movie": selected_movie['title'],
                "showtime": selected_showtime,
                "tickets": num_tickets,
                "price_per_ticket": selected_movie['price'],
                "total_cost": booking_cost
            }
            bookings.append(booking)
            total_cost += booking_cost
            print("✅ Booking confirmed!")
        else:
            print("❌ Booking cancelled.")
        
        # Ask if user wants to book another movie
        another_booking = input("\nWould you like to book another movie? (yes/no): ").lower().strip()
        if another_booking != 'yes':
            break
    
    # Display final summary
    print("\n" + "=" * 50)
    print("🎬 FINAL BOOKING SUMMARY")
    print("=" * 50)
    
    if bookings:
        for i, booking in enumerate(bookings, 1):
            print(f"\n📽️  Booking {i}:")
            print(f"   Movie: {booking['movie']}")
            print(f"   Showtime: {booking['showtime']}")
            print(f"   Tickets: {booking['tickets']}")
            print(f"   Cost: ${booking['total_cost']:.2f}")
        
        print(f"\n💰 TOTAL BOOKINGS: {len(bookings)}")
        print(f"💰 TOTAL COST: ${total_cost:.2f}")
    else:
        print("No bookings were made.")
    
    print("\nThank you for using Movie Theater Booking System! 🍿")

if __name__ == "__main__":
    movie_ticket_booking()
