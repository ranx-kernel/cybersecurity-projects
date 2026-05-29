# Advanced Secure Coding Review & Vulnerability Assessment Platform

## Overview
This project demonstrates an advanced secure coding review and vulnerability assessment process using Python, Flask, Bandit, Streamlit, and OWASP security principles. A vulnerable Flask application was intentionally developed with multiple security flaws and later remediated using secure coding practices.

The project includes:
- Vulnerable Flask Web Application
- Static Security Analysis
- OWASP Top 10 Vulnerability Mapping
- Advanced Security Dashboard
- Secure Remediation Techniques
- Security Visualization and Analytics

---

# Features

- Vulnerable Flask Web Application
- Static Security Analysis using Bandit
- OWASP Top 10 Vulnerability Detection
- Advanced Security Dashboard
- Vulnerability Severity Analytics
- Secure Remediation Workflow
- Security Visualization using Streamlit & Plotly

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Flask | Web Application Framework |
| Bandit | Static Security Analysis |
| Streamlit | Dashboard Development |
| Plotly | Data Visualization |
| SQLite | Database |
| VS Code | Development Environment |

---

# Project Structure

```bash
advanced-secure-coding-review/
│
├── vulnerable_app/
│   ├── app.py
│   └── login.py
│
├── fixed_app/
│   ├── secure_app.py
│   └── secure_login.py
│
├── dashboard/
│   └── dashboard.py
│
├── screenshots/
│   ├── dashboard.png
│   ├── bandit_scan.png
│   ├── vulnerable_code.png
│   ├── secure_code.png
│   ├── flask_app.png
│   └── folder_structure.png
│
├── report/
│   └── Secure_Coding_Review_Report.docx
│
└── README.md
```

---

# Vulnerable Flask Application

The Flask application was intentionally developed with multiple vulnerabilities for secure coding review and cybersecurity analysis purposes.

## Vulnerabilities Included

| Vulnerability | Severity | OWASP Category |
|---|---|---|
| SQL Injection | Medium | A03 Injection |
| Command Injection | High | A03 Injection |
| Hardcoded Secret | Low | A07 Authentication Failures |
| Flask Debug Mode Exposure | High | A05 Security Misconfiguration |

---

# Flask Application Preview

![Flask Application](Screenshot%202026-05-29%141802.png)

---

# Static Security Analysis

Static code analysis was performed using Bandit.

## Bandit Scan Command

```bash
python -m bandit -r .
```

## Vulnerabilities Detected

- SQL Injection
- Command Injection
- Hardcoded Secret
- Flask Debug Mode Exposure

---

# Bandit Scan Result

![Bandit Scan](Screenshot%202026-05-29%143934.png)

---

# Vulnerable Code Example

## SQL Injection Vulnerability

```python
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
```

## Command Injection Vulnerability

```python
os.system(cmd)
```
# Vulnerable Code Screenshot

![Vulnerable Code](Screenshot%202026-05-29%144055.png)


---

# Advanced Security Dashboard

An advanced interactive dashboard was developed using Streamlit and Plotly to visualize vulnerabilities, severity distribution, OWASP mappings, and application risk score.

## Dashboard Features

- KPI Metrics
- Severity Distribution Charts
- OWASP Category Analytics
- Vulnerability Table
- Risk Score Visualization
- Timeline Analysis

---

# Dashboard Preview

![Dashboard](Screenshot%202026-05-29%143508.png)
![Dashboard](Screenshot%202026-05-29%143529.png)
![Dashboard](Screenshot%202026-05-29%143554.png)


---

# Secure Remediation

A secure version of the Flask application was developed by implementing secure coding best practices.

## Security Improvements

| Vulnerability | Remediation |
|---|---|
| SQL Injection | Parameterized Queries |
| Command Injection | Removed os.system() |
| Hardcoded Secret | Improved Secret Management |
| Debug Mode Exposure | Disabled Flask Debug Mode |
| Plaintext Passwords | SHA-256 Password Hashing |

---

# Secure Code Example

## Parameterized Query

```python
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))
```

## Password Hashing

```python
password = hashlib.sha256(
    request.form['password'].encode()
).hexdigest()
```

---

# Secure Code Screenshot

![Secure Code](Screenshot%202026-05-29%144042.png)

---

# Dashboard Analytics

The dashboard visualizes:
- Vulnerability Severity Distribution
- OWASP Category Mapping
- Risk Score
- Vulnerability Counts
- Security Trends

---

# Security Best Practices Implemented

- Input Validation
- Parameterized SQL Queries
- Password Hashing
- Secure Configuration
- Removal of Dangerous System Commands
- Principle of Least Privilege
- Secure Coding Practices

---

# Results

The project successfully demonstrated:
- Detection of multiple application vulnerabilities
- Static code analysis workflow
- OWASP Top 10 vulnerability mapping
- Security remediation techniques
- Advanced security visualization
- Application Security (AppSec) concepts

---

# Conclusion

This project demonstrates practical secure coding review and vulnerability assessment techniques aligned with modern Application Security (AppSec) and DevSecOps workflows. Multiple vulnerabilities were identified, analyzed, visualized, and remediated using secure coding principles and security best practices.

---

# Future Enhancements

- Real-time Vulnerability Scanning
- CVSS Scoring Integration
- AI-Based Remediation Suggestions
- CI/CD Security Pipeline Integration
- Threat Intelligence Integration
- Automated PDF Report Generation

---

# Author

Rania

---

# License

This project is developed for educational and cybersecurity learning purposes.
