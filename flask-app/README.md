git add . 
git commit -m "comment"

git push origin Day1 ---> to push the code 
git status  ---> to check status 


To run the application locally -: 
pyhton app.py 
http://localhost:5000 ---> open the app in the local 

Docker ---: 

docker build -t anilflask-app . ---> to build the image 
docker run -itd -p 5000:5000 anilflask-app ----> to run the image 

To tag image name -: 
docker tag anilflask-app litu2rout/flask-ci-test:v1
Push the image to docker hub -: 
docker push litu2rout/flask-ci-test:v1


Kubernetes -: 
======================
kubectl get pods 
kubectl apply -f pod.yaml 
kubectl port-forward pod/newpd 5000:5000 -------------> this to port forward from the local host 
