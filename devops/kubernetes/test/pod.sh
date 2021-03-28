kubectl run $1 --image=$2 --namespace=$3 --restart=Never --dry-run=true -o yaml
