# Security policy

This repository is a sample project for a blog series.

## Supported use

Use this project for local learning, development realm testing, and readonly Keycloak inspection experiments.

## Not supported

Do not use this sample as-is for production Keycloak administration.

Before production use, add:

- strong authentication around the MCP server
- network isolation
- centralized audit logging
- secret manager integration
- explicit approval workflow for any state-changing operation
- security review from the owner of the Keycloak environment

## Reporting issues

If you find a security issue in this sample, open a GitHub issue without including real secrets, tokens, or production realm data.
