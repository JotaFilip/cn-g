
printf "Building Dockers"

printf "\t Building Account ... "
# sudo docker build . -f app/protobufs/account/Dockerfile -t account
printf "done\n"

printf "\t Building Anime ... "
# sudo docker build . -f app/protobufs/anime/Dockerfile -t anime
printf "done\n"

printf "\t Building Book ... "
sudo docker build . -f app/protobufs/book/Dockerfile -t book
printf "done\n"

printf "\t Building IMDB ... "
# sudo docker build . -f app/protobufs/imdb/Dockerfile -t imdb
printf "done\n"

printf "\t Building Library ... "
sudo docker build . -f app/protobufs/library/Dockerfile -t library
printf "done\n"

printf "\t Building SignIn ... "
# sudo docker build . -f app/protobufs/signin/Dockerfile -t signin
printf "done\n"