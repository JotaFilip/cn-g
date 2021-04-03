
printf  "Creating Protobufs ."
rm ./app/protobufs/*/*pb2* &> /dev/null
rm ./app/protobufs/api_gateway/models.py &> /dev/null

### GERAR FICHEIROS PARA BOOK
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/book/ --grpc_python_out=./app/protobufs/book/ ./app/protobufs/book.proto
ln ./app/protobufs/book/*pb2* ./app/protobufs/library/
printf " ."

### GERAR FICHEIROS PARA ANIME
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/anime/ --grpc_python_out=./app/protobufs/anime/ ./app/protobufs/anime.proto
ln ./app/protobufs/anime/*pb2* ./app/protobufs/library/
printf " ."

### GERAR FICHEIROS PARA IMDB
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/imdb/ --grpc_python_out=./app/protobufs/imdb/ ./app/protobufs/imdb.proto
ln ./app/protobufs/imdb/*pb2* ./app/protobufs/library/
printf " ."

### GERAR FICHEIROS PARA LIBRARY
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/library/ --grpc_python_out=./app/protobufs/library/ ./app/protobufs/library.proto --experimental_allow_proto3_optional
ln ./app/protobufs/library/*pb2* ./app/protobufs/api_gateway/
printf " ."

### GERAR FICHEIROS PARA ACCOUNT
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/account/ --grpc_python_out=./app/protobufs/account/ ./app/protobufs/account.proto
ln ./app/protobufs/account/*pb2* ./app/protobufs/signin/
printf " ."

### GERAR FICHEIROS PARA UTILS
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/utils --grpc_python_out=./app/protobufs/utils/ ./app/protobufs/utils.proto
ln ./app/protobufs/utils/*pb2* ./app/protobufs/library/
ln ./app/protobufs/utils/*pb2* ./app/protobufs/account/
ln ./app/protobufs/utils/*pb2* ./app/protobufs/signin/
printf " ."

### GERAR FICHEIROS PARA SIGNIN
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/signin/ --grpc_python_out=./app/protobufs/signin/ ./app/protobufs/signin.proto
ln ./app/protobufs/signin/*pb2* ./app/protobufs/api_gateway/
ln app/protobufs/signin/models.py app/protobufs/api_gateway/models.py
printf " done\n" 
