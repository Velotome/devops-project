echo "Removing previous container ..."
docker rm -f devops-project
docker build --tag app .
echo "Running container ..."
docker run --name=app -d --network host app
