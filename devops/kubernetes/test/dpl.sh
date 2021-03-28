kubectl create deployment $1 --image=$2 --namespace=$3 --dry-run=true -o yaml 
