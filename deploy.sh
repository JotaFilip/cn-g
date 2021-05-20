export PROJECT_ID=$(gcloud info --format='value(config.project)')
cd cn-g/
./scripts/1_proto_dependencies.sh
./scripts/2_proto_create.sh
cd app/
cd protobufs/
cd account/
docker build -t gcr.io/${PROJECT_ID}/account .
cd ..
cd spark_connector/
docker build -t gcr.io/${PROJECT_ID}/spark-connector .
cd ..
cd api_gateway/
docker build -t gcr.io/${PROJECT_ID}/api-gateway .
cd ../book/
docker build -t gcr.io/${PROJECT_ID}/book .
cd ../anime/
docker build -t gcr.io/${PROJECT_ID}/anime .
cd ../imdb/
docker build -t gcr.io/${PROJECT_ID}/imdb .
cd ../library/
docker build -t gcr.io/${PROJECT_ID}/library .
docker images
gcloud services enable containerregistry.googleapis.com
gcloud auth configure-docker
docker push gcr.io/${PROJECT_ID}/imdb
docker push gcr.io/${PROJECT_ID}/library
docker push gcr.io/${PROJECT_ID}/anime
docker push gcr.io/${PROJECT_ID}/book
docker push gcr.io/${PROJECT_ID}/account
docker push gcr.io/${PROJECT_ID}/spark-connector
docker push gcr.io/${PROJECT_ID}/api-gateway
docker images
gcloud container images list
kubectl get nodes
gcloud container clusters get-credentials cluster-recommendations --zone europe-west4-a
cd ../../..
kubectl apply -f deployment.yaml 
