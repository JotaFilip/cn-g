
printf  "Creating Protobufs ."

### GERAR FICHEIROS PARA BOOK
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/book/ --grpc_python_out=./app/protobufs/book/ ./app/protobufs/book.proto
cp ./app/protobufs/book/*pb2* ./app/protobufs/library/
printf " ."

### GERAR FICHEIROS PARA ANIME
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/anime/ --grpc_python_out=./app/protobufs/anime/ ./app/protobufs/anime.proto
cp ./app/protobufs/anime/*pb2* ./app/protobufs/library/
printf " ."

### GERAR FICHEIROS PARA IMDB
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/imdb/ --grpc_python_out=./app/protobufs/imdb/ ./app/protobufs/imdb.proto
cp ./app/protobufs/imdb/*pb2* ./app/protobufs/library/
printf " ."

### GERAR FICHEIROS PARA LIBRARY
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/library/ --grpc_python_out=./app/protobufs/library/ ./app/protobufs/library.proto --experimental_allow_proto3_optional
cp ./app/protobufs/library/*pb2* ./app/protobufs/api_gateway/
printf " ."

### GERAR FICHEIROS PARA ACCOUNT
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/account/ --grpc_python_out=./app/protobufs/account/ ./app/protobufs/account.proto
cp ./app/protobufs/account/*pb2* ./app/protobufs/signin/
printf " ."

### GERAR FICHEIROS PARA UTILS
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/utils --grpc_python_out=./app/protobufs/utils/ ./app/protobufs/utils.proto
cp ./app/protobufs/utils/*pb2* ./app/protobufs/library/
cp ./app/protobufs/utils/*pb2* ./app/protobufs/account/
cp ./app/protobufs/utils/*pb2* ./app/protobufs/signin/
printf " ."

### GERAR FICHEIROS PARA SIGNIN
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/signin/ --grpc_python_out=./app/protobufs/signin/ ./app/protobufs/signin.proto
cp ./app/protobufs/signin/*pb2* ./app/protobufs/api_gateway/
printf " done\n"