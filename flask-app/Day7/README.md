Kubelet’s Role:

Kubelet’s job is to read static pod manifest files from disk and ensure that pods (like etcd, apiserver, controller-manager, etc.) are running as defined in those manifests.

If a static pod fails, kubelet will repeatedly try to restart it, regardless of etcd’s health, because this is a local node operation.

How Kubelet Manages Master Node Components
Static Pod Creation:
Each control plane component is defined by a static pod manifest located in a specific directory (typically /etc/kubernetes/manifests). The kubelet monitors this directory and ensures every manifest corresponds to a running pod.

Health & Restart:
If any static pod (for example, kube-apiserver, kube-scheduler, etcd) managed on the master node fails or crashes, the kubelet immediately detects this failure and automatically restarts the pod to maintain the cluster’s operational integrity.

No API Server Dependency:
Since kubelet manages these static pods directly—independent of the API server—control plane services can be reliably bootstrapped or recovered, even if the API server isn’t currently available.

Role of Kubelet on the Master (Control Plane) Node
Overview
The kubelet is the primary agent that runs on every node in a Kubernetes cluster, including master (control plane) nodes. Its job is to ensure the desired state of all pods specified for its node.

Key Functions on the Master Node
Management of Control Plane Pods

On master nodes, kubelet is responsible for running and monitoring core control plane components (like the API server, controller manager, scheduler, and etcd) as pods. These components are often deployed as static pods using manifest files placed in a special directory.

Static Pod Handling

The kubelet watches for static pod manifests (YAML files) in directories like /etc/kubernetes/manifests. When such files are found, kubelet creates and keeps these pods running, even if the Kubernetes API server is not available. This mechanism is essential for cluster bootstrapping and control plane resiliency.

Health and Resource Monitoring

Kubelet collects and reports node and pod metrics, which are critical for both scheduling and monitoring the health of master node components.

Registration and Self-Management

Kubelet on the master node registers the node with the API server, ensuring the control plane recognizes it as an active part of the cluster.

Why Is Kubelet Needed on Master Nodes?
Almost all Kubernetes clusters run control plane components as pods for flexibility, management, and resilience.

These components must be managed by kubelet because kubelet is the only component that can ensure local containers are running and healthy, restart them if they fail, and handle local resources.

Without kubelet, static pods—and thus the essential Kubernetes control plane services—would not start or be managed on the master node.

Typical Scenario (kubeadm, etc.)
Component	Managed As	Managed By
API Server	Static Pod	Kubelet (on master)
Controller Manager	Static Pod	Kubelet (on master)
Scheduler	Static Pod	Kubelet (on master)
etcd	Static Pod	Kubelet (on master)
