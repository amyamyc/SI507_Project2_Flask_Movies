#### SI 507 Python Programming Project 1 Assignment
This is a README.md for file SI507_project_2.py. This is a homework assignment for SI 507/ Professor Jackie Cohen at the University of Michigan.

##### What are the files included?
The files included are movies_clean.csv, movie_tools.py, SI507_project2.py and requirements.txt.

The movies_clean.csv file is a spreadsheet contains information about movies. Each row in this spreadsheet represents information about a single movie. The SI507_project2.py is where we use a flask framework to present data onto your web browser. The movie_tools.py essentially supports reading and isolating information in the movies_clean.csv file. 

##### How do you run this project?
Download project2 into your local computer.
Ensure you have the dependencies based off the requirements.txt file.
In terminal, locate your project2 file and use command prompts to arrive in the project2 directory.
Type into terminal "python SI507_project2.py runserver". This will prompt a local server URL that you can paste into your web browser.

##### What is the final result?
The final result will depend on the URL that you input into your web browser.
If your url ends with a "/". you will see the sentence "3145 movies recorded".
If your url ends with "/movies/ratings", you will see 5 movie titles and their IMDB rating right next to it. Each time you refresh the page, you will see a different set of 5 movie titles with the IMDB ratings. The browser shows this information because the code written in SI507_project2.py and movies_tools.py is extracting information from the movies_clean.csv file to be shown on on a web browser.
