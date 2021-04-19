cd ~
gcloud config set compute/zone europe-west4-a
gcloud services enable container.googleapis.com
curl -L https://istio.io/downloadIstio | sh -
cd istio-1.9.3/
pwd
export PATH="$PATH:/tmp/istio-1.9.3/bin"
istioctl x precheck
istioctl install
kubectl get svc -n default
kubectl get pods -n default
kubectl label namespace default istio-injection=enabled
kubectl create -n default secret tls istio-ingressgateway-certs --key ../cn-g/scripts/privkey1.pem --cert ../cn-g/scripts/fullchain1.pem
