🔑 Kubernetes TLS & Certificates – CKA Quick Cheatsheet
📍 Key Cert Locations (default kubeadm setup)
Cluster CA: /etc/kubernetes/pki/ca.crt

API Server cert & key:

/etc/kubernetes/pki/apiserver.crt

/etc/kubernetes/pki/apiserver.key

API Server client certs:

To kubelet → /etc/kubernetes/pki/apiserver-kubelet-client.crt

Key → /etc/kubernetes/pki/apiserver-kubelet-client.key

Scheduler kubeconfig: /etc/kubernetes/scheduler.conf

Controller Manager kubeconfig: /etc/kubernetes/controller-manager.conf

Kubelet kubeconfig: /var/lib/kubelet/config.yaml → usually references /etc/kubernetes/kubelet.conf

Admin kubeconfig: /etc/kubernetes/admin.conf

📍 How Trust Works
API Server (Server) presents its cert (apiserver.crt) signed by cluster CA.

Clients (Scheduler, Controller, Kubelet, kubectl) present their own client certs (stored in respective *.conf files).

Mutual TLS (mTLS) → both sides verify using same CA (ca.crt).

📍 Inspecting Certs
bash
Copy
Edit
# Check subject, expiry, SANs
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout

# Verify a cert against CA
openssl verify -CAfile /etc/kubernetes/pki/ca.crt /etc/kubernetes/pki/apiserver.crt
📍 Checking Current Certs Expiry
bash
Copy
Edit
kubeadm certs check-expiration
📍 Renew Certificates
bash
Copy
Edit
# Renew all
sudo kubeadm certs renew all

# Then restart static pod manifests
sudo systemctl restart kubelet
📍 Debugging Tips
If control plane pod (apiserver, scheduler, controller) fails: check /etc/kubernetes/manifests/*.yaml for wrong cert paths.

If kubectl fails with x509 error → check ~/.kube/config or /etc/kubernetes/admin.conf.

If kubelet not joining → bootstrap token expired OR kubelet.conf outdated. Fix with:

bash
Copy
Edit
kubeadm token create --print-join-command


🔑 Kubernetes TLS Map (Simplified)
Who (Client)	Talks to (Server)	Client Cert (file)	Server Cert (file)	Trusted by (CA)
kubectl (admin)	API Server	/etc/kubernetes/admin.conf (uses admin.crt/key)	/etc/kubernetes/pki/apiserver.crt	/etc/kubernetes/pki/ca.crt
Scheduler	API Server	/etc/kubernetes/scheduler.conf	/etc/kubernetes/pki/apiserver.crt	/etc/kubernetes/pki/ca.crt
Controller Manager	API Server	/etc/kubernetes/controller-manager.conf	/etc/kubernetes/pki/apiserver.crt	/etc/kubernetes/pki/ca.crt
Kubelet	API Server	/etc/kubernetes/kubelet.conf	/etc/kubernetes/pki/apiserver.crt	/etc/kubernetes/pki/ca.crt
API Server (client)	Kubelet (server)	/etc/kubernetes/pki/apiserver-kubelet-client.crt	/var/lib/kubelet/pki/kubelet.crt	/etc/kubernetes/pki/ca.crt

🌍 Logic samajh lo:
Har component (kubectl, scheduler, controller, kubelet) → API server ke client hote hain.

API server apna cert dikhata hai (apiserver.crt) jo cluster CA se signed hota hai.

Client apna cert (conf files me defined) bhejta hai.

Dono ek hi CA (ca.crt) pe trust karte hain → isiliye connection secure ho jata hai.

👉 Exam me agar certs ka question aaya to bas table yaad karo:

client config → /etc/kubernetes/*.conf

server certs → /etc/kubernetes/pki/

trust → /etc/kubernetes/pki/ca.crt

Bataun kya mai ek diagram bana kar flow dikhau (client → server → CA) jisse aur crystal clear ho jaye?









Ask ChatGPT
