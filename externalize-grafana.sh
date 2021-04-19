#grafana should be configure first using the marketplace, this script is just used to be able to access it externally, output will be grafana's address

kubectl patch svc "prometheus-1-grafana" --namespace "default" -p '{"spec": {"type": "LoadBalancer"}}'

SERVICE_IP=$(kubectl get svc prometheus-1-grafana --namespace default --output jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo "http://${SERVICE_IP}/"
