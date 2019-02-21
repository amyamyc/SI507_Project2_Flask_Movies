import csv

movies = []
x = open("movies_clean.csv", "r")
csv_reader = csv.reader(x)

class Movie(object):
    def __init__(self, each_row): # each row is a list
        self.title = each_row[0]
        self.ratings = each_row[14]

    def __str__(self):
        return "{} | {}<br>".format(self.title, self.ratings)
# Movie(row) is an instance of class Movie
for row in csv_reader:
    movies.append(Movie(row)) #appending an instance of Movie to movie list
