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
- Install Django Dependencies

```bash
cd djangoApiService
pip install -r requirements.txt
```
- Install Blockchain Dependencies

```bash
cd blockchainService
pip install -r requirements.txt
```


### 3️⃣ Set Up Environment Variables
- Create a .env file inside the django-api/ directory and add the following:

```env
SECRET_KEY=your_secret_key
WEB3_PROVIDER_URL=https://your-ethereum-node-url
CONTRACT_ADDRESS=your_contract_address
PRIVATE_KEY=your_wallet_private_key
```

---


## 🚀 Running the Project
### ▶ Start the Django API Server

```bash
cd django-api
python manage.py runserver
```

### ▶ Deploy the ERC-20 Smart Contract

```bash
cd blockchain
node deploy.js
```

After execution, the deployed contract address will be displayed. Make sure to update your .env file with the deployed contract address.

---


## 🔗 API Endpoints

| Method | Endpoint           | Description                          |
|--------|--------------------|--------------------------------------|
| `POST` | `/deploy/`         | Deploy an ERC-20 contract           |
| `GET`  | `/balance/<address>/` | Get token balance for a given address |
| `POST` | `/transfer/`       | Transfer tokens to another address  |


To test the API, you can use Postman or curl:

```bash
curl -X GET http://127.0.0.1:8000/balance/0xYourWalletAddress/
```

---

## 📜 Project Structure

```bash
erc20-django-api/
│── django-api/        # Django-based API logic
│── blockchain/        # Solidity and JavaScript scripts for deploying the smart contract
│── README.md          # Project documentation
│── docker-compose.yml # Docker setup for running services
```

---

## 📜 Project Structure

```bah
erc20-django-api/
│── django-api/        # Django-based API logic
│── blockchain/        # Solidity and JavaScript scripts for deploying the smart contract
│── README.md          # Project documentation
│── docker-compose.yml # Docker setup for running services
```
--- 

## 🤝 Contributing
Contributions are welcome! To contribute:

1. Fork the repository 🍴
2. Create a new branch (git checkout -b feature-xyz)
3. Commit your changes (git commit -m "Add new feature")
4. Submit a Pull Request ✅

--- 

## 📌 License
This project is licensed under the MIT License. See the LICENSE file for details.

🚀 Ready to deploy on Ethereum! Happy coding! 🎯🔥

```yaml
---

### ✨ Features of this `README.md`:
✔ **Professional structure** with clear sections  
✔ **Prerequisites, installation, and API documentation**  
✔ **Formatted tables for API endpoints**  
✔ **Contribution and licensing details**  

💡 **Let me know if you need any modifications or improvements!** 🚀
```