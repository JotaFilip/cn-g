
printf "Running Dockers\n"

printf "\t Building Account ... "
# sudo docker run -p 127.0.0.1:50055:50055/tcp account &
printf "done\n"

printf "\t Building Anime ... "
# sudo docker run -p 127.0.0.1:50053:50053/tcp anime &
printf "done\n"

printf "\t Building Book ... "
sudo docker run -p 127.0.0.1:50051:50051/tcp book &
printf "done\n"

printf "\t Building IMDB ... "
# sudo docker run -p 127.0.0.1:50052:50052/tcp imdb &
printf "done\n"

printf "\t Building Library ... "
sudo docker run -p 127.0.0.1:50050:50050/tcp library &
printf "done\n"

printf "\t Building SignIn ... "
# sudo docker run -p 127.0.0.1:50054:50054/tcp signin &
printf "done\n"