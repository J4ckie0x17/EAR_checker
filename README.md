# EAR Checker

🔍 A Python tool to detect EAR (External After Redirect / Authentication Bypass via Direct Access) vulnerabilities based on misconfigured redirection with content.

---

## 🚀 Features

- Detects EAR via misused HTTP redirection (301, 302, 303, 307, 308)
- Prints Burp Suite `Match and Replace` rules for quick testing
- Shows HTTP version dynamically (1.0, 1.1, 2)
- Colorful ASCII banner 😎
- Fully CLI-friendly

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


## 🧠 What is EAR?

EAR (External Attack Surface or Access Restriction bypass) is a vulnerability where redirection logic (like 302 Found) leaks sensitive content inside the response body, instead of enforcing access control correctly.

## 💡 Tip for Burp Suite:

Use the generated `Match` and `Replace` output in:


`Proxy → Options → Match and Replace`

Example rule:

|Match|Replace|
|---|---|
|`HTTP/1.1 302 FOUND`|`HTTP/1.1 200 FOUND`|
