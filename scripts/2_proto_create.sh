
printf  "Creating Protobufs ."

### GERAR FICHEIROS PARA BOOK
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/book/ --grpc_python_out=./app/protobufs/book/ ./app/protobufs/book.proto
printf " ."

### GERAR FICHEIROS PARA ANIME
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/anime/ --grpc_python_out=./app/protobufs/anime/ ./app/protobufs/anime.proto
printf " ."

### GERAR FICHEIROS PARA IMDB
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/imdb/ --grpc_python_out=./app/protobufs/imdb/ ./app/protobufs/imdb.proto
printf " ."

### GERAR FICHEIROS PARA LIBRARY
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/library/ --grpc_python_out=./app/protobufs/library/ ./app/protobufs/library.proto --experimental_allow_proto3_optional
printf " ."

### GERAR FICHEIROS PARA ACCOUNT
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/account/ --grpc_python_out=./app/protobufs/account/ ./app/protobufs/account.proto
printf " ."

### GERAR FICHEIROS PARA SIGNIN
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/signin/ --grpc_python_out=./app/protobufs/signin/ ./app/protobufs/signin.proto
printf " done\n"