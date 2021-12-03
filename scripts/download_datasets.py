#!/usr/bin/python
import os
import requests
import datetime
from zipfile import ZipFile
import gzip
import shutil

from requests.api import delete


URLs_IMDb = ["https://datasets.imdbws.com/name.basics.tsv.gz",
             "https://datasets.imdbws.com/title.akas.tsv.gz",
             "https://datasets.imdbws.com/title.basics.tsv.gz",
             "https://datasets.imdbws.com/title.crew.tsv.gz",
             "https://datasets.imdbws.com/title.episode.tsv.gz"
             "https://datasets.imdbws.com/title.principals.tsv.gz",
             "https://datasets.imdbws.com/title.ratings.tsv.gz"]
NAMEs_IMDb = ["name.basics", "title.akas", "title.basics", "title.crew", "title.episode", "title.principals", "title.ratings"]
TYP_ARCHIVE_IMDb = ".tsv.gz"
TYPE_DATA_IMDb = ".tsv"

URLs_GROUP_LENS = []
NAMEs_ROUP_LENS = []
TYP_ARCHIVE_ROUP_LENS = ""
TYPE_DATA_ROUP_LENS = ""

URLs_Movie_Lense = {}

#Downloading the IMDb-Datasets
x = 1
for URL in URLs_IMDb:
    start = datetime.datetime.now()
    print("Download " + str(x) + " from " + URL + " @" + str(start))
    r = requests.get(URL, allow_redirects=True)
    print("---" + "Status-Code: " + str(r.status_code) + "---")
    if r.status_code == 200:
        open(NAMEs_IMDb[x - 1] + TYP_ARCHIVE_IMDb, 'wb').write(r.content)
        print("--- Start unzip ---")    
        try:
            delete_flag = False
            try: os.remove(NAMEs_IMDb[x - 1] + TYPE_DATA_IMDb)
            except: delete_flag = False 
            finally: delete_flag = True
            if delete_flag:
                with gzip.open(NAMEs_IMDb[x - 1] + TYP_ARCHIVE_IMDb, 'rb') as f_in:
                    with open("data.tsv", 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.rename("data.tsv", NAMEs_IMDb[x] + TYPE_DATA_IMDb)
                #Checking if the size is bigger then 0
                if os.stat(NAMEs_IMDb[x] + TYPE_DATA_IMDb).st_size > 0: print("--> Succesfull download + unzip")  
                else: print("Check data: The size is 0")
        except: print("Something went wrong")
        finally: os.remove(NAMEs_IMDb[x - 1] + TYP_ARCHIVE_IMDb)     
        print("--- End unzip ---")
        print("--- Download-Time: " + str(round((datetime.datetime.now() - start).total_seconds()/60), 2) + "min ---")
    else: print("Download failed")
    x = x + 1 #Increment for the next dataset

#https://docs.python.org/3/library/zipfile.html
#https://appdividend.com/2020/01/31/python-unzip-how-to-extract-single-or-multiple-files/ 
#https://docs.python.org/3/library/gzip.html 
#https://www.codegrepper.com/code-examples/python/how+to+extract+gz+file+python 