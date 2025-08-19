echo "Removing previous container ..."
docker rm -f devops-project
docker build --tag devops-project .
echo "Running container ..."
docker run --name=devops-project -d --network host -p 8000:8000 devops-project