# Sample prompts

These prompts are designed for a test realm named `demo`.

## 1. Dry-run bulk user creation

```text
Create 50 marketing team users in the demo realm.
Use usernames marketing001 to marketing050.
Use emails marketing001@example.com to marketing050@example.com.
Set temporary password Temp123!ChangeMe.
Require password update on first login.
Run dry-run first.
```

## 2. Execute after review

```text
The dry-run result looks correct.
Create the marketing001 to marketing050 users in the demo realm.
Use dryRun false.
```

## 3. Assign role

```text
Assign grafana-reader role to marketing001 through marketing050 in the demo realm.
Run dry-run first.
```

## 4. Validate

```text
Validate that marketing001 through marketing050 exist in the demo realm.
```

## 5. Rollback

```text
Disable marketing001 through marketing050 in the demo realm.
Run dry-run first.
```

## 6. Safety question

```text
Before running this against production, list the risks and the controls I need to add.
```
