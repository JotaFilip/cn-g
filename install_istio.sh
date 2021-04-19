cd ~
gcloud config set compute/zone europe-west4-a
gcloud services enable container.googleapis.com
curl -L https://istio.io/downloadIstio | sh -
cd istio-1.9.3/
pwd
export PATH="$PATH:/tmp/istio-1.9.3/bin"
istioctl x precheck
istioctl install
kubectl get svc -n istio-system
kubectl get pods -n istio-system
kubectl label namespace default istio-injection=enabled