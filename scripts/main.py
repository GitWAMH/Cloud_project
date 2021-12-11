#!/usr/bin/python

import pyfiglet
import os
  
title = pyfiglet.figlet_format("Movie Recommendator")
menu_options = {
    0: 'Download Datasets (Essential)',
    1: 'Movies for adults or children',
    2: 'Best rated movies by year',
    3: 'Best runtime',
    4: 'Ratings per IMDb type',
    5: 'Best movies from a given genre',
    6: 'Best movies from a given title',
    7: 'Is it worth to watch this movie?',
    8: 'Best movies by year and region',
    9: 'Exit',
}

print(title)
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def download():
     print('Starting Download...')
     os.system('python download_datasets.py')

def adult_child(master):
     print('You selected \'Movies for adults or children\'')
     arg = input('Enter \'-a\' for adult or \'-c\' for child: ')
     num = input('Enter the number of movies you want to be shown(Optional): ')
     os.system('spark-submit --master ' + master + ' adult_child_movies.py ' + arg + ' ' + num)

def by_year(master):
     print('You selected \'Best rated movies by year\'')
     mode = input('Enter \'-m\' for MovieLens results or \'-i\' for IMDb results: ')
     year = input('Enter a year: ')
     num = input('Enter the number of movies you want to be shown(Optional): ')
     os.system('spark-submit --master ' + master + ' best_rated_movies_by_year.py ' + mode + ' ' + year + ' ' + num)

def runtime(master):
     print('You selected \'Best runtime\'')
     ratinglvl = input('Enter the rating level(Optional): ')
     minRun = input('Enter the minimum runtime(Optional): ')
     maxRun = input('Enter the maximum runtime(Optional): ')
     arg = input('Enter a command (-avg, -min, -max, -sum) (Optional): ')
     os.system('spark-submit --master ' + master + ' best_runtime.py ' + ratinglvl + ' ' + minRun + ' ' + maxRun + ' ' + arg)

def imdb_type(master):
     print('You selected \'Ratings per IMDb type\'')
     type = input('Enter the type(Enter -help or -h for help): ')
     ratinglvl = input('Enter the rating level: ')
     count = input('Enter the number of movies you want to be shown: ')
     os.system('spark-submit --master ' + master + ' getRatingsPerIMDbType.py ' + type + ' ' + ratinglvl + ' ' + count)

def by_genre(master):
     print('You selected \'Best movies from a given genre\'')
     mode = input('Enter \'-m\' for MovieLens results or \'-i\' for IMDb results: ')
     genre = input('Enter a movie genre: ')
     num = input('Enter the number of movies you want to be shown(Optional): ')
     os.system('spark-submit --master ' + master + ' movies_by_genre.py ' +  mode + ' ' + genre + ' ' + num)

def by_title(master):
     print('You selected \'Best movies from a given title\'')
     title = input('Enter a movie title: ')
     os.system('spark-submit --master ' + master + ' movies_by_title.py \'' + title + '\'')
     
def is_worth(master):
     print('You selected \'Is it worth to watch this movie?\'')
     title = input('Enter a movie title: ')
     os.system('spark-submit --master ' + master + ' worth_movie.py \'' + title + '\'')
     
def year_region(master):
     print('You selected \'Best movies by year and region\'')
     data = input('Enter a year or a language: ')
     num = input('Enter the number of movies you want to be shown(Optional): ')
     os.system('spark-submit --master ' + master + ' year_region_recommendations.py \'' + data + '\' ' + num)

if __name__=='__main__':
    masterOpt = 0
    master = ''
    while (not (masterOpt == 1 or masterOpt == 2)):
        try:
            masterOpt = int(input('Enter where do you want to run the application:\n1 -- Local\n2 -- Cluster\nOption: '))
        except:
            print('Wrong input. Please enter a number ...')
        if masterOpt == 1:
            cores = input('Enter the number of cores you want to use to run the application (\'*\' for all cores available): ')
            master = 'local[' + cores + ']'
        elif masterOpt == 2:
            cluster = input('Enter the URL of the cluster you want to use to run the application: ')
            master = cluster
        else:
            print('Invalid option. Please enter 1 for Local or 2 for Cluster')

    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 0:
        	  download()
        elif option == 1:
            adult_child(master)
        elif option == 2:
            by_year(master)
        elif option == 3:
            runtime(master)
        elif option == 4:
            imdb_type(master)
        elif option == 5:
            by_genre(master)
        elif option == 6:
            by_title(master)
        elif option == 7:
            is_worth(master)
        elif option == 8:
            year_region(master)
        elif option == 9:
            print('Thanks for using our recommender')
            exit()
        
        else:
            print('Invalid option. Please enter a number between 0 and 9.')
