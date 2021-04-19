cd ~
ZONE=europe-west4-a
PROJECT=$(gcloud config get-value project)
CLUSTER=gke-load-test
TARGET="https://recommendations.sytes.net"
SCOPE="https://www.googleapis.com/auth/cloud-platform"

gcloud config set compute/zone ${ZONE}
gcloud config set project ${PROJECT}

git clone https://github.com/GoogleCloudPlatform/distributed-load-testing-using-kubernetes
cd distributed-load-testing-using-kubernetes

gcloud container clusters create $CLUSTER --zone $ZONE --scopes $SCOPE --enable-autoscaling --min-nodes "3" --max-nodes "10" --scopes=logging-write,storage-ro --addons HorizontalPodAutoscaling,HttpLoadBalancing
gcloud container clusters get-credentials $CLUSTER --zone $ZONE --project $PROJECT

gcloud builds submit --tag gcr.io/$PROJECT/locust-tasks:latest docker-image
gcloud container images list | grep locust-tasks

sed -i -e "s/\[TARGET_HOST\]/$TARGET/g" kubernetes-config/locust-master-controller.yaml
sed -i -e "s/\[TARGET_HOST\]/$TARGET/g" kubernetes-config/locust-worker-controller.yaml
sed -i -e "s/\[PROJECT_ID\]/$PROJECT/g" kubernetes-config/locust-master-controller.yaml
sed -i -e "s/\[PROJECT_ID\]/$PROJECT/g" kubernetes-config/locust-worker-controller.yaml

kubectl apply -f kubernetes-config/locust-master-controller.yaml
kubectl apply -f kubernetes-config/locust-master-service.yaml
kubectl apply -f kubernetes-config/locust-worker-controller.yaml

