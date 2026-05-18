# Single-Cluster HA Architecture

```mermaid
flowchart LR
  U["User"] --> LB["Ingress / Load Balancer"]
  LB --> K1["Keycloak Pod A"]
  LB --> K2["Keycloak Pod B"]
  K1 <-->|"cache / cluster traffic"| K2
  K1 --> DB["RDS Multi-AZ"]
  K2 --> DB

  subgraph AZ1["Availability Zone A"]
    K1
  end

  subgraph AZ2["Availability Zone B"]
    K2
  end
```

## Reading the diagram

- The application tier is duplicated with at least 2 Pods.
- Pods should not be concentrated on one node or one AZ.
- The database tier also needs HA; otherwise the login path still has a single point of failure.
- This is a single-cluster HA sample, not a multi-cluster or multi-region architecture.
