> ./scripts/development_scripts/pids #clean the file pids
python3 ./app/protobufs/anime/anime.py & echo $! >> ./scripts/development_scripts/pids #write pid in pids file to kill later
python3 ./app/protobufs/book/book.py & echo $! >> ./scripts/development_scripts/pids
python3 ./app/protobufs/imdb/imdb.py & echo $! >> ./scripts/development_scripts/pids
python3 ./app/protobufs/library/library.py & echo $! >> ./scripts/development_scripts/pids
python3 ./app/protobufs/account/account.py & echo $! >> ./scripts/development_scripts/pids
python3 ./app/protobufs/signin/signin.py & echo $! >> ./scripts/development_scripts/pids
python3 ./app/protobufs/api_gateway/api_gateway.py & echo $! >> ./scripts/development_scripts/pids