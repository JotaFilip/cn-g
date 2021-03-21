 
printf "Building Dockers\n" 
 
printf "\t Building Account ... " 
{ 
sudo docker build . -f app/protobufs/account/Dockerfile -t account 
} &> /dev/null 
printf "done\n" 
 
printf "\t Building Anime ... " 
{ 
sudo docker build . -f app/protobufs/anime/Dockerfile -t anime 
} &> /dev/null 
printf "done\n" 
 
printf "\t Building Book ... " 
{ 
sudo docker build . -f app/protobufs/book/Dockerfile -t book 
} &> /dev/null 
printf "done\n" 
 
printf "\t Building IMDB ... " 
{ 
sudo docker build . -f app/protobufs/imdb/Dockerfile -t imdb 
} &> /dev/null 
printf "done\n" 
 
printf "\t Building Library ... " 
# { 
# sudo docker build . -f app/protobufs/library/Dockerfile -t library
# } &> /dev/null 
printf "done\n" 
 
printf "\t Building SignIn ... " 
# {
# sudo docker build . -f app/protobufs/signin/Dockerfile -t signin 
# } &> /dev/null 
printf "done\n" 