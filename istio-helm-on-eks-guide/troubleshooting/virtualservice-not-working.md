# VirtualService not working

Check:

- `hosts` value;
- `gateways` reference;
- namespace of Gateway and VirtualService;
- route destination host;
- DestinationRule subset names;
- whether another VirtualService is conflicting with the same host.
