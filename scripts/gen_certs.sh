#!/bin/bash

# Generate CA key and self-signed cert
#openssl req -x509 -nodes -newkey rsa:4096 -keyout ca.key -out ca.pem -subj /O=me

# Generate a private key and certificate signing request for the client and server
openssl req -nodes -newkey rsa:4096 -keyout account.key -out account.csr -subj /CN=account
openssl req -nodes -newkey rsa:4096 -keyout anime.key -out anime.csr -subj /CN=anime
openssl req -nodes -newkey rsa:4096 -keyout api_gateway.key -out api_gateway.csr -subj "/C=PT/ST=Aveiro/L=Anadia/O=Leitao, Inc./OU=IT/CN=api-gateway"
openssl req -nodes -newkey rsa:4096 -keyout book.key -out book.csr -subj /CN=book
openssl req -nodes -newkey rsa:4096 -keyout imdb.key -out imdb.csr -subj /CN=imdb
openssl req -nodes -newkey rsa:4096 -keyout library.key -out library.csr -subj /CN=library
openssl req -nodes -newkey rsa:4096 -keyout signin.key -out signin.csr -subj /CN=signin

#openssl req -nodes -newkey rsa:4096 -keyout account.key -out account.csr -subj /CN=localhost
#openssl req -nodes -newkey rsa:4096 -keyout anime.key -out anime.csr -subj /CN=localhost
#openssl req -nodes -newkey rsa:4096 -keyout api_gateway.key -out api_gateway.csr -subj "/C=PT/ST=Aveiro/L=Anadia/O=Leitao, Inc./OU=IT/CN=localhost"
#openssl req -nodes -newkey rsa:4096 -keyout book.key -out book.csr -subj /CN=localhost
#openssl req -nodes -newkey rsa:4096 -keyout imdb.key -out imdb.csr -subj /CN=localhost
#openssl req -nodes -newkey rsa:4096 -keyout library.key -out library.csr -subj /CN=localhost
#openssl req -nodes -newkey rsa:4096 -keyout signin.key -out signin.csr -subj /CN=localhost

# Sign the client and server certs with the CA cert
openssl x509 -req -in account.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out account.pem
openssl x509 -req -in anime.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out anime.pem
openssl x509 -req -in api_gateway.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out api_gateway.pem
openssl x509 -req -in book.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out book.pem
openssl x509 -req -in imdb.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out imdb.pem
openssl x509 -req -in library.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out library.pem
openssl x509 -req -in signin.csr -CA ca.pem -CAkey ca.key -set_serial 1 -out signin.pem

mv account.* ../app/protobufs/account
mv anime.* ../app/protobufs/anime
mv api_gateway.* ../app/protobufs/api_gateway
mv book.* ../app/protobufs/book
mv imdb.* ../app/protobufs/imdb
mv library.* ../app/protobufs/library
mv signin.* ../app/protobufs/signin
cp ca.pem ../app/protobufs/account
cp ca.pem ../app/protobufs/anime
cp ca.pem ../app/protobufs/api_gateway
cp ca.pem ../app/protobufs/book
cp ca.pem ../app/protobufs/imdb
cp ca.pem ../app/protobufs/library
cp ca.pem ../app/protobufs/signin