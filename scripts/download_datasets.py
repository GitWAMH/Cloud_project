import requests
import gzip

URLs_IMDb = ["https://datasets.imdbws.com/name.basics.tsv.gz",
            "https://datasets.imdbws.com/title.akas.tsv.gz",
            "https://datasets.imdbws.com/title.basics.tsv.gz",
            "https://datasets.imdbws.com/title.crew.tsv.gz",
            "https://datasets.imdbws.com/title.episode.tsv.gz"
            "https://datasets.imdbws.com/title.principals.tsv.gz",
            "https://datasets.imdbws.com/title.ratings.tsv.gz"]

URLs_Movie_Lense = {}

x = 1
for URL in URLs_IMDb:
    print("Download " + str(x) + " from " + URL)
    r = requests.get(URL, allow_redirects=True)
    print("---" + str(r.status_code) + "---")
    open(str(x) + '.tsv.gz', 'wb').write(r.content)
    print("--Start unzip--")
    try:
        with gzip.open('file.txt.gz', 'rb') as f:
            file_content = f.read()
            print(file_content)
    except:
        print("Something went wrong")
    print("--End unzip--")
    x = x + 1

