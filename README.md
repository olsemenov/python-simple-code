# Simple python code

This repo includes python webserver and helm chart to show how k8s works

## Requirements
* Helm 3 [How install](https://helm.sh/docs/intro/install/)
* kubectl [How install](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Installation

In the repo folder run:
```bash
helm template helm_chart/ > out
```
It will create manifests from this helm chart. [To read more](https://helm.sh/docs/helm/helm_template/)
_______
You need to apply these manifests to your k8s cluster:
```bash
kubectl apply -f out
```
It will create all resources you've specified. [To read more](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply)
___
After you need to expose your application in our case to a local machine:
```bash
kubectl port-forward svc/webserver 8080:80
```
Now you can see the application at this link http://localhost:8080
## How the application works

* `http://localhost:8080` - main page with a random color and it will create the test.txt file with a color name 
* `http://localhost:8080/color/red` - you can specify another color one from the color list "red","green","blue","blue2","darkblue","pink"
* `http://localhost:8080/read_file` - to check data in the test.txt file

## Another useful command
```bash
kubectl exec -it POD_NAME bash
```
Give you access to pod. [To read more](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#exec)


## License
[MIT](https://choosealicense.com/licenses/mit/)