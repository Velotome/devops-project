echo "Removing previous container ..."
docker rm -f devops-project
docker build --tag devops-project .
echo "Running container ..."
docker run --name=devops-project -d --network host devops-project