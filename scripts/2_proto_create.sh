printf  "Creating Protobufs ."
rm ./app/protobufs/*/*pb2*
### GERAR FICHEIROS PARA BOOK
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/book/ --grpc_python_out=./app/protobufs/book/ ./app/protobufs/book.proto --experimental_allow_proto3_optional
ln ./app/protobufs/book/*pb2* ./app/protobufs/library/ &> /dev/null
printf " ."

### GERAR FICHEIROS PARA ANIME
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/anime/ --grpc_python_out=./app/protobufs/anime/ ./app/protobufs/anime.proto --experimental_allow_proto3_optional
ln ./app/protobufs/anime/*pb2* ./app/protobufs/library/ &> /dev/null
printf " ."

### GERAR FICHEIROS PARA IMDB
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/imdb/ --grpc_python_out=./app/protobufs/imdb/ ./app/protobufs/imdb.proto --experimental_allow_proto3_optional
ln ./app/protobufs/imdb/*pb2* ./app/protobufs/library/ &> /dev/null
printf " ."

### GERAR FICHEIROS PARA LIBRARY
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/library/ --grpc_python_out=./app/protobufs/library/ ./app/protobufs/library.proto --experimental_allow_proto3_optional
ln ./app/protobufs/library/*pb2* ./app/protobufs/api_gateway/ &> /dev/null
printf " ."

### GERAR FICHEIROS PARA ACCOUNT
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/account/ --grpc_python_out=./app/protobufs/account/ ./app/protobufs/account.proto --experimental_allow_proto3_optional
ln ./app/protobufs/account/*pb2* ./app/protobufs/signin/ &> /dev/null
ln ./app/protobufs/account/*pb2* ./app/protobufs/library/ &> /dev/null
printf " ."

### GERAR FICHEIROS PARA UTILS
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/utils --grpc_python_out=./app/protobufs/utils/ ./app/protobufs/utils.proto --experimental_allow_proto3_optional
ln ./app/protobufs/utils/*pb2* ./app/protobufs/library/ &> /dev/null
ln ./app/protobufs/utils/*pb2* ./app/protobufs/account/ &> /dev/null
ln ./app/protobufs/utils/*pb2* ./app/protobufs/signin/ &> /dev/null
ln ./app/protobufs/utils/*pb2* ./app/protobufs/book/ &> /dev/null
ln ./app/protobufs/utils/*pb2* ./app/protobufs/anime/ &> /dev/null
ln ./app/protobufs/utils/*pb2* ./app/protobufs/imdb/ &> /dev/null
printf " ."

### GERAR FICHEIROS PARA SIGNIN
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/signin/ --grpc_python_out=./app/protobufs/signin/ ./app/protobufs/signin.proto --experimental_allow_proto3_optional
ln ./app/protobufs/signin/*pb2* ./app/protobufs/api_gateway/ &> /dev/null
printf " done\n" 
