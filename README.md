# EAR Checker

🔍 A Python tool to detect EAR (External After Redirect / Authentication Bypass via Direct Access) vulnerabilities based on misconfigured redirection with content.

---
## ❓ What is an EAR Vulnerability?

**Execution After Redirect (EAR)** is an attack in which an attacker intentionally ignores redirection responses (such as HTTP 30X) and directly retrieves sensitive content that was intended only for authenticated users.

A successful EAR exploit can lead to unauthorized data exposure — and in some cases, complete compromise of the application.

---

## 🚀 Features

- Detects EAR via misused HTTP redirection (301, 302, 303, 307, 308)
- Prints Burp Suite `Match and Replace` rules for quick exploitation (if it's vulnerable)
- Shows HTTP version dynamically (1.0, 1.1, 2)
- Colorful ASCII banner 😎
- Fully CLI-friendly
---
## POC
- There are 2 directories available in the website:
	- /login
	- /admin
- When access to /admin it redirects to /login because we don't have any valid credentials.
![2025-04-05](https://github.com/J4ckie0x17/EAR_checker/blob/c50f2803a8ef8c523ce83cabd7a8b745440f93d2/poc/EAR_POC.mp4)


---

## 📦 Requirements
```bash
pip3 install -r requirements.txt
```

## ⚙️ Usage
```python
python3 EAR_checker.py -u http://TARGET_IP -d /admin
```
```python
python3 EAR_checker.py -u http://10.129.28.59 -d /admin
```

## 💡 Tip for Burp Suite:

If it appears vulnerable, the tool generates what to put in the BurpSuite in Match and Replace

Use the generated `Match` and `Replace` output in:

`Proxy → Options → Match and Replace`

Example rule:

|Match|Replace|
|---|---|
|`HTTP/1.1 30X FOUND`|`HTTP/1.1 200 FOUND`|
