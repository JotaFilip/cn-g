
# stop all
docker stop $(docker ps -a -q)
# remove all
docker rm $(docker ps -a -q)
# prune
docker image prune -a

# remove protos
rm ./app/protobufs/*/*pb2*