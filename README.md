# 🔍 Data Footprint Mapper

**Privacy-first personal data exposure scanner**\
Discover where your digital footprint exists online --- without storing
any of your personal data.

------------------------------------------------------------------------

## 📌 Overview

Data Footprint Mapper helps individuals understand where their email IDs
and usernames are registered across the internet, especially on Indian
platforms. It performs privacy-safe OSINT-based scanning and provides
clear risk analysis and cleanup guidance.

This project is designed for students, professionals, and
privacy-conscious users.

------------------------------------------------------------------------

## 🛠️ Tech Stack

### Backend

-   FastAPI
-   PostgreSQL (Supabase)
-   Redis (Upstash)
-   Pydantic
-   Uvicorn

### Frontend

-   React 18
-   TypeScript
-   Vite
-   TailwindCSS
-   Axios

### Infrastructure

-   Render
-   Vercel
-   GitHub

------------------------------------------------------------------------

## 🎯 Problem Statement

Most users do not know:

-   Where their data is stored
-   Which platforms are risky
-   How to clean old accounts
-   If their credentials are exposed

Existing tools are: - Paid - Western-focused - Invasive - Fear-based

Data Footprint Mapper solves this with a transparent, free, and
India-focused solution.

------------------------------------------------------------------------

## ✨ Features

### Core Features

-   Email & Username Scan
-   India-Focused Platform Detection
-   Risk Score Generation
-   Account Cleanup Guide
-   No Data Storage

### Technical Features

-   Asynchronous Processing
-   Rate Limiting
-   Input Validation
-   Secure API Design
-   Error Handling

------------------------------------------------------------------------

## 🚀 Getting Started

### Prerequisites

-   Python 3.9+
-   Node.js 18+
-   Git

------------------------------------------------------------------------

## ⚙️ Backend Setup

``` bash
cd backend

python -m venv venv

# Activate

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env

uvicorn app.main:app --reload
```

Server runs on:

http://localhost:8000

------------------------------------------------------------------------

## 🎨 Frontend Setup

``` bash
cd frontend

npm install

cp .env.example .env

npm run dev
```

Frontend runs on:

http://localhost:5173

------------------------------------------------------------------------

## 🗂️ Project Structure

    data-footprint-mapper/
    ├── backend/
    │   ├── app/
    │   │   ├── api/
    │   │   ├── core/
    │   │   ├── services/
    │   │   └── main.py
    │   ├── requirements.txt
    │   └── .env.example
    │
    ├── frontend/
    │   ├── src/
    │   │   ├── components/
    │   │   ├── hooks/
    │   │   ├── types/
    │   │   └── App.tsx
    │   ├── package.json
    │   └── .env.example
    │
    └── README.md

------------------------------------------------------------------------

## 🔒 Privacy Policy

### We Never

-   Store personal data
-   Save logs
-   Track users
-   Use cookies
-   Sell information

### We Always

-   Process data in real-time
-   Delete inputs immediately
-   Encrypt communications
-   Maintain transparency

Fully compliant with India's DPDP Act (2023).

------------------------------------------------------------------------

## 📊 Platform Coverage

Supports 50+ platforms including:

-   Social Media
-   E-Commerce
-   Fintech
-   Education
-   Streaming
-   Travel
-   Gaming
-   Jobs
-   Professional Networks

------------------------------------------------------------------------

## 🛣️ Roadmap

-   HIBP Integration
-   PDF Reports
-   Dark Mode
-   Browser Extension
-   Public API
-   Mobile App

------------------------------------------------------------------------

## 🤝 Contributing

1.  Fork the repo
2.  Create a branch
3.  Commit changes
4.  Open a Pull Request

All contributions are welcome.

------------------------------------------------------------------------

## 🧪 Testing

-   Unit Tests (PyTest)
-   API Tests (Postman)
-   Frontend Tests (Jest)

------------------------------------------------------------------------

## 📄 License

MIT License

------------------------------------------------------------------------

## 👤 Author

Siri V Hegde\
GitHub: https://github.com/Siri-026

------------------------------------------------------------------------

## 🙏 Acknowledgments

-   Have I Been Pwned
-   FastAPI Docs
-   Supabase
-   Upstash

------------------------------------------------------------------------

### 🔐 Built With Privacy First Approach
