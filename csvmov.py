import csv

my_movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w", newline = "") as my_csv:
    write_mov = csv.writer(my_csv, delimiter = ",")
    for movies in my_movies:
        write_mov.writerow(movies)
