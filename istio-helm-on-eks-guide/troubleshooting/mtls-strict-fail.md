# mTLS STRICT failure

Check:

- both client and server workloads have sidecars;
- PeerAuthentication scope;
- DestinationRule TLS mode;
- whether external clients are trying plain HTTP;
- whether PERMISSIVE mode is needed during migration.
