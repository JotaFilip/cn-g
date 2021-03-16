### GERAR FICHEIROS PARA BOOK
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/book/ --grpc_python_out=./app/protobufs/book/ ./app/protobufs/book.proto

### GERAR FICHEIROS PARA ANIME
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/anime/ --grpc_python_out=./app/protobufs/anime/ ./app/protobufs/anime.proto

### GERAR FICHEIROS PARA IMDB
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/imdb/ --grpc_python_out=./app/protobufs/imdb/ ./app/protobufs/imdb.proto

### GERAR FICHEIROS PARA LIBRARY
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/library/ --grpc_python_out=./app/protobufs/library/ ./app/protobufs/library.proto

### GERAR FICHEIROS PARA ACCOUNT
python3 -m grpc_tools.protoc -I ./app/protobufs --python_out=./app/protobufs/account/ --grpc_python_out=./app/protobufs/account/ ./app/protobufs/account.proto