from flask import Flask
from movies_tools import *
import csv
import random

app = Flask(__name__)


@app.route('/') # this is a list of Movie instances
def number_movies(): # Route function names can be anything unique
    number = str(len(movies)-1)
    return '<h1>{} movies recorded </h1>'.format(number)


@app.route('/movies/ratings')
def five_ratings():
    random.shuffle(movies)
    movie_inst = movies[1:6]
    titles_ratings = ""
    for movie in movie_inst:
        titles_ratings += str(movie) # without the string method, we are put together a empty string and class instance
    return titles_ratings


if __name__ == '__main__':
    app.run()
