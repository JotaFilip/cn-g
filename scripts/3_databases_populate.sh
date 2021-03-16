printf "Populating Books . . . "
# { python3 "app/databases/data/GoodReads/PopulateBooks.py" } &> /dev/null
printf "done\n"

printf "Populate Animes . . . "
# { python3 "app/databases/data/MyAnimeList/PopulateAnimes.py" } &> /dev/null
printf "done\n"

printf "Populate Movies . . . "
# { python3 "app/databases/data/IMDB/PopulateMovies.py"
#   python3 "app/databases/data/IMDB/PopulateMovies2.py" } &> /dev/null
printf "done\n"