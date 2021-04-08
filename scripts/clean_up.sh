
# stop all
docker stop $(docker ps -a -q)
# remove all
docker rm $(docker ps -a -q)

# remove protos
rm ./app/protobufs/*/*pb2*