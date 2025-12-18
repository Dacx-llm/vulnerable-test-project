# Vulnerable Test Project 🔓

> ⚠️ **WARNING: This project contains intentional security vulnerabilities for testing purposes only!**
> 
> Do NOT deploy this to any production environment. All credentials are fake/example values.

## Purpose

This project is designed to test and validate security scanning tools:

| Tool     | What it Detects                              |
|----------|----------------------------------------------|
| Semgrep  | Static code analysis, security patterns      |
| Trivy    | Vulnerability scanner for dependencies       |
| Gitleaks | Secret/credential detection                  |
| Checkov  | Infrastructure-as-Code & config scanning     |
| Syft     | SBOM (Software Bill of Materials) generation |

## Scanning Commands

```bash
# Semgrep
semgrep scan --config auto .

# Trivy
trivy fs .

# Gitleaks
gitleaks detect --source . -v

# Checkov
checkov -d .

# Syft
syft . -o json > sbom.json
```

## Expected Findings

| Tool     | Expected Findings |
|----------|-------------------|
| Semgrep  | 30+ vulnerabilities |
| Trivy    | 50+ CVEs |
| Gitleaks | 40+ secrets |
| Checkov  | 80+ misconfigs |
| AV/EDR   | EICAR + webshell patterns |

## Disclaimer

This project is for **educational and testing purposes only**.

---

Created for AgentBox security scanning validation 🛡️
