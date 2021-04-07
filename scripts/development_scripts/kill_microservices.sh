while read pid; do
    echo "Killing process $pid..."
    kill -9 "$pid"
fuser -k 5000/tcp #kill processes on port 5000 (children of api_gateway)
done <./scripts/development_scripts/pids