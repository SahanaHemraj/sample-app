how to create a flask application 
1. Set up a virtual environment
2. Install Flask
pip install Flask

3. Create a Flask app
4. Run the Flask app
python app.py

create a docker file for this
4. Build and Run the Docker Container
4.1. Build the Docker Image
docker build -t sample-app .

4.2. Run the Docker Container
docker run -p 5000:5000 sample-app

create kubernetes deployment, HPA, service account, service and config map yamals

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