# Keycloak Permissions

Use a dedicated Keycloak client and service account.

## Recommended review items

- Can the service account create users only in the intended realm?
- Can it assign only expected realm roles?
- Does it avoid broad realm-admin style permissions where possible?
- Is production realm access blocked by configuration?
- Is the client secret stored outside Git?

## Practical advice

Start with a test realm. Grant only the permissions required for this sample:

- create users
- query users
- view realm roles
- assign approved realm roles
- disable or delete generated test users only after approval

Actual Keycloak role names and permission models vary by version and realm design. Validate with your own test realm before adapting this sample.
