# README

docker build -t dpinedaj/enc-fastapi:1.0.0 .
docker push dpinedaj/enc-fastapi:1.0.0

kubectl apply -f k8s/api/api.yaml

kubectl port-forward enc-api-69b7bc9847-vt9pv 8080:8080