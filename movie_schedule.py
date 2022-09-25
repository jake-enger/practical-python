current_movies = {'The Grinch':'11:00am',
                'Rudolph':'1:00pm',
                'Frosty the Snowman':'3:00pm',
                'Christmas Vacation':'5:00pm'}

print("We're currently showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)
if showtime == None:
    print("We're sorry, but the movie you wish to see is unavailable")
else:
    print(movie, "is playing at:", showtime)