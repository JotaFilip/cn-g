# ./scripts/1_proto_dependencies.sh 
./scripts/2_proto_create.sh 
#./scripts/3_databases_populate.sh
cd app/protobufs
sudo docker-compose up --build

#./scripts/4_docker_build.sh
#./scripts/5_docker_run.sh
#./scripts/6_test.sh