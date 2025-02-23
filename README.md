# create a flask application 
## Set up a virtual environment
1. Install Flask
```sh
pip install Flask
```

# Create a Flask app
## Run the Flask app
```sh
python app.py
```

# create a docker file
## Build the Docker Image
```sh
docker build -t sample-app .
```

## Run the Docker Container
```sh
docker run -p 5000:5000 sample-app
```

# create kubernetes deployment, HPA, service account, service and config map yamals

```sh
brew install minikube
minikube start
minikube image load sample-app

kubectl apply -f Deploy/sample-app-config.yaml
kubectl apply -f Deploy/sample-app-deployment.yaml
kubectl apply -f Deploy/sample-app-hpa.yaml
kubectl apply -f Deploy/sample-app-service-account.yaml
kubectl apply -f Deploy/sample-app-service.yaml


kubectl get deployments
kubectl get namespaces
kubectl get pods -n default
kubectl -n default exec -it sample-app-deployment-669bd8cc6d-62dk2 -- /bin/sh
kubectl logs sample-app-deployment-669bd8cc6d-62dk2 -n default
```