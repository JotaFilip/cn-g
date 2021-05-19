
printf "Populating Databases\n"
printf "\t Populating Books . . . "
# { python3 "app/databases/data/GoodReads/PopulateBooks.py" } &> /dev/null
printf "done\n"

printf "\t Populating Animes . . . "
# { python3 "app/databases/data/MyAnimeList/PopulateAnimes.py" } &> /dev/null
printf "done\n"

printf "\t Populating Movies . . . "
# { python3 "app/databases/data/IMDB/PopulateMovies.py"
#   python3 "app/databases/data/IMDB/PopulateMovies2.py" } &> /dev/null
printf "done\n"