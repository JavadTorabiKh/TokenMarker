# 🚀 **ERC-20 Token Deployment & Django API Integration**

<p align="center">
  <img src="https://img.shields.io/badge/Blockchain-Ethereum-blue?style=for-the-badge&logo=ethereum" alt="Ethereum">
  <img src="https://img.shields.io/badge/Backend-Django-green?style=for-the-badge&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/Smart_Contract-Solidity-black?style=for-the-badge&logo=solidity" alt="Solidity">
</p>

## 📌 **About the Project**
This project consists of two main services:
1. **Blockchain Service**: Deploy an **ERC-20 smart contract** on the Ethereum blockchain.
2. **Django API Service**: Interact with the **deployed smart contract** through a Django-based REST API.

---

## ⚙ **Prerequisites**
Before running the project, make sure you have the following installed:

- **Python 3.8+** (for Django backend)
- **Node.js** (for interacting with the blockchain)
- **Solidity Compiler (`solc`)**
- **Web3.py** (for smart contract interaction)
- **Docker** (optional, for running services in containers)
- **Metamask** or any Ethereum-compatible wallet

---

## 🚀 **Installation and Setup**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-repo/erc20-django-api.git
cd erc20-django-api
```

### 2️⃣ Install Dependencies
- **Install Django Dependencies

```bash
cd djangoApiService
pip install -r requirements.txt
```
- **Install Blockchain Dependencies

```bash
cd blockchainService
pip install -r requirements.txt
```