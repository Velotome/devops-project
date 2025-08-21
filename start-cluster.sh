kind create cluster --config kube/kind-config.yaml

if [ -z "$(docker images -q app 2> /dev/null)" ]; then
    echo "image app not found, building it..."
    docker build --tag app --target app .
fi

kind load docker-image app
kubectl apply -f kube/devops-project-namespace.yml
kubectl apply -f kube/pod-app.yml
