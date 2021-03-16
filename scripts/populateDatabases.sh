echo "Populate Books"
python "cn-g/app/databases/data/GoodReads/PopulateBooks.py"

echo "Populate Animes"
python "cn-g/app/databases/data/MyAnimeList/PopulateAnimes.py"

echo "Populate Movies"
python "cn-g/app/databases/data/IMDB/PopulateMovies.py"
python "cn-g/app/databases/data/IMDB/PopulateMovies2.py"