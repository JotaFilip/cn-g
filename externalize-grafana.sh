kubectl patch svc "prometheus-1-grafana" --namespace "default" -p '{"spec": {"type": "LoadBalancer"}}'

SERVICE_IP=$(kubectl get svc prometheus-1-grafana --namespace default --output jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo "http://${SERVICE_IP}/"