
printf "Running Dockers\n"

printf "\t Running Account ... "
sudo docker run -p 127.0.0.1:50055:50055/tcp account &
printf "done\n"

printf "\t Running Anime ... "
sudo docker run -p 127.0.0.1:50053:50053/tcp anime &
printf "done\n"

printf "\t Running Book ... "
sudo docker run -p 127.0.0.1:50051:50051/tcp book &
printf "done\n"

printf "\t Running IMDB ... "
sudo docker run -p 127.0.0.1:50052:50052/tcp imdb &
printf "done\n"

printf "\t Running Library ... "
sudo docker run -p 127.0.0.1:50050:50050/tcp library &
printf "done\n"

printf "\t Running SignIn ... "
sudo docker run -p 127.0.0.1:50054:50054/tcp signin &
printf "done\n"