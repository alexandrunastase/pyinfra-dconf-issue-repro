To reproduce the issue run :

```
make up
```

Expected result: dconf write command is executed
Actual result: dconf write command is not executed

Possible causes:
- quote escaping
