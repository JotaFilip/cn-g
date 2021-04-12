cn-g/scripts/1_proto_dependencies.sh
cn-g/scripts/2_proto_create.sh
cd cn-g/
cd app/
cd protobufs/
cd account/
docker build -t gcr.io/${PROJECT_ID}/account:v2 .
cd ..
cd signin/
docker build -t gcr.io/${PROJECT_ID}/signin:v2 .
cd ..
cd api_gateway/
docker build -t gcr.io/${PROJECT_ID}/api_gateway:v2 .
cd ../book/
docker build -t gcr.io/${PROJECT_ID}/book:v2 .
cd ../anime/
docker build -t gcr.io/${PROJECT_ID}/anime:v2 .
cd ../imdb/
docker build -t gcr.io/${PROJECT_ID}/imdb:v2 .
cd ../library/
docker build -t gcr.io/${PROJECT_ID}/library:v2 .
docker images
gcloud services enable containerregistry.googleapis.com
gcloud auth configure-docker
docker push gcr.io/${PROJECT_ID}/imdb:v2
docker push gcr.io/${PROJECT_ID}/library:v2
docker push gcr.io/${PROJECT_ID}/anime:v2
docker push gcr.io/${PROJECT_ID}/book:v2
docker push gcr.io/${PROJECT_ID}/account:v2
docker push gcr.io/${PROJECT_ID}/signin:v2
docker push gcr.io/${PROJECT_ID}/api_gateway:v2
docker images
gcloud container images list
kubectl get nodes
gcloud container clusters get-credentials cluster-recommendations --zone europe-west4-a
cd ../../..
kubectl apply -f deployment.yaml 
