gcloud beta container clusters update cluster-recommendations --update-addons=Istio=ENABLED --istio-config=auth=MTLS_PERMISSIVE --zone=europe-west4-a
kubectl label namespace default istio-injection=enabled





git clone --recursive https://github.com/GoogleCloudPlatform/click-to-deploy.git
kubectl --insecure-skip-tls-verify apply -f "https://raw.githubusercontent.com/GoogleCloudPlatform/marketplace-k8s-app-tools/master/crd/app-crd.yaml"
cd click-to-deploy/k8s/prometheus

export APP_INSTANCE_NAME=prometheus-1
export NAMESPACE=default

TAG=2.11
export IMAGE_PROMETHEUS="marketplace.gcr.io/google/prometheus:${TAG}"
export IMAGE_ALERTMANAGER="marketplace.gcr.io/google/prometheus/alertmanager:${TAG}"
export IMAGE_KUBE_STATE_METRICS="marketplace.gcr.io/google/prometheus/kubestatemetrics:${TAG}"
export IMAGE_NODE_EXPORTER="marketplace.gcr.io/google/prometheus/nodeexporter:${TAG}"
export IMAGE_GRAFANA="marketplace.gcr.io/google/prometheus/grafana:${TAG}"
export IMAGE_PROMETHEUS_INIT="marketplace.gcr.io/google/prometheus/debian9:${TAG}"

for i in "IMAGE_PROMETHEUS" \
         "IMAGE_ALERTMANAGER" \
         "IMAGE_KUBE_STATE_METRICS" \
         "IMAGE_NODE_EXPORTER" \
         "IMAGE_GRAFANA" \
         "IMAGE_PROMETHEUS_INIT"; do
  repo=$(echo ${!i} | cut -d: -f1);
  digest=$(docker pull ${!i} | sed -n -e 's/Digest: //p');
  export $i="$repo@$digest";
  env | grep $i;
done

# Install pwgen and base64
sudo apt-get install -y pwgen

# Set the Grafana password
export GRAFANA_GENERATED_PASSWORD= "$(echo "12345" | base64)"

export PROMETHEUS_REPLICAS=2
export STORAGE_CLASS="standard"

kubectl --insecure-skip-tls-verify create namespace "$NAMESPACE"
kubectl --insecure-skip-tls-verify create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user $(gcloud config get-value account)

export PROMETHEUS_SERVICE_ACCOUNT="${APP_INSTANCE_NAME}-prometheus"
export KUBE_STATE_METRICS_SERVICE_ACCOUNT="${APP_INSTANCE_NAME}-kube-state-metrics"
export ALERTMANAGER_SERVICE_ACCOUNT="${APP_INSTANCE_NAME}-alertmanager"
export GRAFANA_SERVICE_ACCOUNT="${APP_INSTANCE_NAME}-grafana"
export NODE_EXPORTER_SERVICE_ACCOUNT="${APP_INSTANCE_NAME}-node-exporter"

cat resources/service-accounts.yaml | envsubst '$NAMESPACE $PROMETHEUS_SERVICE_ACCOUNT $KUBE_STATE_METRICS_SERVICE_ACCOUNT $ALERTMANAGER_SERVICE_ACCOUNT $GRAFANA_SERVICE_ACCOUNT $NODE_EXPORTER_SERVICE_ACCOUNT' > "${APP_INSTANCE_NAME}_sa_manifest.yaml"

kubectl --insecure-skip-tls-verify apply -f "${APP_INSTANCE_NAME}_sa_manifest.yaml" --namespace "${NAMESPACE}"
awk 'FNR==1 {print "---"}{print}' manifest/* | envsubst '$APP_INSTANCE_NAME $NAMESPACE $STORAGE_CLASS $IMAGE_PROMETHEUS $IMAGE_ALERTMANAGER $IMAGE_KUBE_STATE_METRICS $IMAGE_NODE_EXPORTER $IMAGE_GRAFANA $IMAGE_PROMETHEUS_INIT $NAMESPACE $GRAFANA_GENERATED_PASSWORD $PROMETHEUS_REPLICAS $PROMETHEUS_REPLICAS $PROMETHEUS_SERVICE_ACCOUNT $KUBE_STATE_METRICS_SERVICE_ACCOUNT $ALERTMANAGER_SERVICE_ACCOUNT $GRAFANA_SERVICE_ACCOUNT $NODE_EXPORTER_SERVICE_ACCOUNT' > "${APP_INSTANCE_NAME}_manifest.yaml"
kubectl --insecure-skip-tls-verify apply -f "${APP_INSTANCE_NAME}_manifest.yaml" --namespace "${NAMESPACE}"
echo "https://console.cloud.google.com/kubernetes/application/${ZONE}/${CLUSTER}/${NAMESPACE}/${APP_INSTANCE_NAME}"

kubectl --insecure-skip-tls-verify patch svc "$APP_INSTANCE_NAME-grafana" --namespace "$NAMESPACE" -p '{"spec": {"type": "LoadBalancer"}}' #IP externo
SERVICE_IP=$(kubectl --insecure-skip-tls-verify get svc $APP_INSTANCE_NAME-grafana --namespace $NAMESPACE --output jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo "http://${SERVICE_IP}/"

#kubectl --insecure-skip-tls-verify port-forward --namespace ${NAMESPACE} ${APP_INSTANCE_NAME}-grafana-0 3000 #IP local

#-------CHECK CREDENTIALS-------
GRAFANA_USERNAME="$(kubectl --insecure-skip-tls-verify get secret $APP_INSTANCE_NAME-grafana --namespace $NAMESPACE --output=jsonpath='{.data.admin-user}' | base64 --decode)"
GRAFANA_PASSWORD="$(kubectl --insecure-skip-tls-verify get secret $APP_INSTANCE_NAME-grafana --namespace $NAMESPACE --output=jsonpath='{.data.admin-password}' | base64 --decode)"

echo "Grafana credentials:"
echo "- user: ${GRAFANA_USERNAME}"
echo "- pass: ${GRAFANA_PASSWORD}"
