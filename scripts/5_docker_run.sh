
printf "Running Dockers\n"

sudo docker network create micro_services

printf "\t Running Account . . . "
sudo docker run -p 127.0.0.1:50055:50055/tcp account --network="micro_services" --name "account" &
printf "done\n"

printf "\t Running Anime . . . "
sudo docker run -p 127.0.0.1:50053:50053/tcp anime --network="micro_services" --name "anime" &
printf "done\n"

printf "\t Running Book . . . "
sudo docker run -p 127.0.0.1:50051:50051/tcp book --network="micro_services" --name "book" &
printf "done\n"

printf "\t Running IMDB . . . "
sudo docker run -p 127.0.0.1:50052:50052/tcp imdb --network="micro_services" --name "imdb" &
printf "done\n"

printf "\t Running Library . . . "
sudo docker run -p 127.0.0.1:50050:50050/tcp library --network="micro_services" --name "library" & # -e ANIME_HOST=anime -e BOOKS_HOST=book -e IMDBS_HOST=imdb -e ACCOUNTS_HOST=account &
printf "done\n"

printf "\t Running SignIn . . . "
sudo docker run -p 127.0.0.1:50054:50054/tcp signin --network="micro_services" --name "signin" & # -e ACCOUNTS_HOST=account &
printf "done\n"

printf "\t Running API Gateway . . . "
sudo docker run -p 127.0.0.1:5000:5000/tcp api_gateway --network="micro_services" --name "api_gateway" & # -e SIGNIN_HOST=signin -e LIBRARY_HOST=library &
printf "done\n"