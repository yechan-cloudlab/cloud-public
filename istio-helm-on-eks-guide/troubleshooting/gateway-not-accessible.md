# Gateway not accessible

Check:

- ingress gateway Service type;
- LoadBalancer external address;
- security groups and NACLs on EKS;
- Gateway selector labels;
- VirtualService gateway reference;
- DNS record points to the correct load balancer.
