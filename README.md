Sample project for istio demo

Frontend talks to backend. There are two versions of backend v1 and v2

***Build Frontend docker***

docker build -t springland/istio-demo-frontend -f ./FrontendDockerfile .

docker push springland/istio-demo-frontend

***Build Backend docker***

docker build -t springland/istio-demo-backend -f BackendDockerfile .
docker push springland/istio-demo-backend




kubectl get events --sort-by=.metadata.creationTimestamp

create name space
kubectl create ns istio-demo 

kubectl label namespace istio-demo istio-injection=enabled
kubectl label namespace istio-demo istio-injection-

kubectl label namespace istio-demo istio-injection=disabled


**change to istio-demo**
kubectl config set-context --current --namespace=istio-demo

kubectl run busyboxplus --image=radial/busyboxplus:curl -i --tty

deploy

kubectl apply -f deployment.yaml

minikube service list -n istio-demo

export INGRESS_HOST=$(minikube ip)

 export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')

export GATEWAY_URL="http://$INGRESS_HOST:$INGRESS_PORT"


export BACKEND_V1_POD=$(kubectl get pod -l app=istio-demo-backend,version=v1 -o jsonpath='{.items[0].metadata.name}')
istioctl x describe pod $BACKEND_V1_POD

export BACKEND_V2_POD=$(kubectl get pod -l app=istio-demo-backend,version=v2 -o jsonpath='{.items[0].metadata.name}')
istioctl x describe pod $BACKEND_V2_POD