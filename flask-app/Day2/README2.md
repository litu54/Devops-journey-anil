📘 Kubernetes ReplicaSet (RS) – DevOps Notes
✅ Purpose:
A ReplicaSet ensures that a specified number of identical Pods are running at all times.

🔧 Key Components of ReplicaSet YAML:
yaml
Copy
Edit
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-rs
  labels:
    app: example       # optional - labels for the RS itself

spec:
  replicas: 3
  selector:
    matchLabels:
      app: web         # RS manages only Pods with this label
  template:
    metadata:
      labels:
        app: web       # must match selector above
    spec:
      containers:
      - name: nginx
        image: nginx:1.23.4
        ports:
        - containerPort: 80
🧠 How It Works:
replicas: → how many Pods RS should ensure are running.

selector.matchLabels: → tells RS which Pods to monitor.

template: → defines what the Pods will look like (labels, container image, etc.).

template.metadata.labels: must match selector.matchLabels exactly.

If a Pod crashes or is deleted → RS recreates it automatically.

⚠️ Important Rules:
Rule	Explanation
template: is mandatory	Without it, RS doesn’t know what Pods to create.
selector.matchLabels must match template.metadata.labels	Otherwise, RS won’t manage any Pods.
You can have extra labels in the Pod	As long as required labels in matchLabels are present.
Labels in metadata: (RS itself) are not used for matching	They're only for tagging the RS object itself.

🔁 Real-Time Use:
We rarely use ReplicaSet directly in production.

Instead, we use Deployment, which internally creates and manages ReplicaSets.

Still, understanding RS is crucial to master how Deployment works under the hood.

✅ Useful Commands:
bash
Copy
Edit
# Create RS from YAML
kubectl apply -f rs.yaml

# Get ReplicaSets
kubectl get rs

# Describe RS (troubleshoot label mismatch)
kubectl describe rs <rs-name>

# Get Pods managed by a specific RS (by label)
kubectl get pods -l app=web

# Delete RS and its Pods
kubectl delete -f rs.yaml
🧪 Test Scenarios:
Correct label match → Pods created

Wrong matchLabels → 0 Pods created

Manually deleted a Pod → RS recreates it

Extra labels in Pods → Still matches if required labels are present

💡 Interview Tip:
“ReplicaSet maintains the desired state by comparing its matchLabels with existing Pods. If Pods matching those labels are fewer than desired, RS uses the template to create more. This is the core mechanism used under the hood by Deployments.”

