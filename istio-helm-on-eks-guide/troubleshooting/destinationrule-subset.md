# DestinationRule subset issue

Check:

- subset label keys match pod labels;
- subset label values match pod labels;
- deployments actually have different versions;
- VirtualService references the correct subset name;
- workload endpoints are ready.
