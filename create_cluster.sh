gcloud services enable cloudapis.googleapis.com  container.googleapis.com containerregistry.googleapis.com
gcloud container clusters create cluster-recommendations  --zone=europe-west4-a --cluster-version=latest --num-nodes=3 --machine-type=n1-standard-4  --enable-autoscaling --min-nodes=1 --max-nodes=5   --enable-autorepair   --scopes=service-control,service-management,compute-rw,storage-ro,cloud-platform,logging-write,monitoring-write
gcloud container clusters get-credentials cluster-recommendations --zone europe-west1-b
kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)
cd cn-g
#kubectl create secret tls recommendations  --cert scripts/fullchain1.pem --key scripts/privkey1.pem --dry-run=client
kubectl create secret tls recommendations  --cert scripts/fullchain1.pem --key scripts/privkey1.pem
