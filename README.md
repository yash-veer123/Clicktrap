<p align="center">
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python">
  <img src="https://img.shields.io/badge/kali%20linux-181717?style=for-the-badge&logo=kali-linux&logoColor=white" alt="Kali Linux">
  <img src="https://img.shields.io/badge/cybersecurity-magenta?style=for-the-badge&logo=generic" alt="Cybersecurity">
  <img src="https://img.shields.io/badge/Version-1.0_Stable-purple?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Author-Dev--Jangid-blue?style=for-the-badge" alt="Author">
</p>

<h1 align="center">🎯 CLICKTRAP 🎯</h1>

<p align="center">
  <b>The Elite Automated UI Redressing & Clickjacking Scanner for Modern Security Research.</b>
</p>

---

## 📜 OVERVIEW

**CLICKTRAP** is a high-performance reconnaissance and vulnerability assessment tool engineered specifically to hunt down Clickjacking vulnerabilities at scale. By analyzing critical HTTP response headers (`X-Frame-Options` and `Content-Security-Policy`), ClickTrap instantly identifies unprotected endpoints and automatically generates visual Proof of Concept (PoC) exploits.

---

## ⚡ KEY FEATURES

* 🔍 **Smart Header Analysis:** Precision checking for missing or weak `X-Frame-Options` and CSP `frame-ancestors` headers.
* 🛠️ **Instant PoC Generation:** Automatically writes operational, ready-to-test HTML exploit files (`clickjacking_poc.html`) for vulnerable targets.
* 🌀 **Mass Pipeline Automation:** Seamless integration with sub-domain discovery pipelines (like Subfinder and Httpx output lists).
* 📟 **Clean UI Terminal:** Clear, color-coded diagnostic feedback highlighting secure vs. vulnerable assets instantly.

---

## 📦 WORKFLOW ENGINE



1. **Scan:** The core Python engine analyzes the target web headers.
2. **Detect:** Flags missing defensive headers in real-time.
3. **Exploit:** Drops an interactive visual layering exploit template aligned perfectly for target validation.

---

## 🛠️ INSTALLATION

Clone the repository and set up the dependencies inside your Kali Linux terminal:

```bash
git clone [https://github.com/devjangid/ClickTrap.git](https://github.com/devjangid/ClickTrap.git)
cd ClickTrap
pip3 install -r requirements.txt
