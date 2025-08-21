docker rm -f app
docker build --tag app --target app .
docker run --name=app -d --network host app
