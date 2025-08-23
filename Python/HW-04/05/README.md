# Assignment 9: Login System
### Difficulty: Advanced

Create a simple login system that:

- Has **predefined valid usernames and passwords**
- Uses appropriate conditional logic for validation
- Provides **different messages** for different failure types

---

## Requirements
- Use the **`and`** operator for credential validation
- Use the **`or`** operator to allow **multiple valid credential pairs**
- Practice **complex conditional logic**
- **Prompts** should be exactly:
  - `Username: `
  - `Password: `
- **Messages** (use this exact wording for consistency with tests you may add later):
  - On success: `Login successful!`
  - On wrong password (known username): `Incorrect password.`
  - On unknown username: `Username not found.`

> **Note:** Treat input as **case-sensitive** (i.e., `"Admin"` ≠ `"admin"`).

---

## Valid Credentials (example set)
- `admin / password123`  
- `user / mypass`  
- `guest / welcome`
---

## Example Runs

### Example 1 — Success on first try
```
Username: admin
Password: password123
Login successful!
```

### Example 2 — Wrong password, then success on second attempt
```
Username: admin
Password: wrong
```


---

## Hints
- Validate success with a single compound condition using `and` for a pair and `or` between pairs.
- Keep messages **exactly** as shown above to make automated testing straightforward.
