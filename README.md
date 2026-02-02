# 🔍 Data Footprint Mapper

**Privacy-first personal data exposure scanner** — Discover where your digital footprint exists without storing any of your data.

![Tech Stack](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=flat&logo=typescript&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)

## 🎯 Problem Statement

Most people have no idea where their personal data exists online. Existing tools are either:
- Paid and expensive
- Western-centric (ignore Indian platforms)
- Fear-mongering (selling VPNs/services)
- Require account creation

**This tool is different:** Free, India-focused, privacy-first, and transparent.

---

## ✨ Features

### Core Functionality
- 🔎 **Smart Email/Username Scanning** — Pattern-based OSINT detection
- 🇮🇳 **India-Specific Platforms** — Flipkart, Swiggy, Paytm, Naukri, and 50+ services
- 📊 **Risk Scoring** — Explainable algorithm (not black-box AI)
- 🛡️ **Privacy-First** — Zero data storage, all processing in real-time
- 📋 **Actionable Cleanup Plan** — Prioritized steps with time estimates

### Technical Highlights
- ⚡ **High Performance** — Async FastAPI backend
- 🎨 **Modern UI** — React + TypeScript + Tailwind CSS
- 🔒 **DPDP Compliant** — Follows India's Digital Personal Data Protection Act 2023
- 🚀 **Production Ready** — Rate limiting, error handling, CORS configured

---

## 🏗️ Tech Stack

### Backend
- **FastAPI** — Modern async Python web framework
- **PostgreSQL** (Supabase) — Platform pattern storage
- **Redis** (Upstash) — Rate limiting & caching
- **Pydantic** — Data validation

### Frontend
- **React 18** — Component-based UI
- **TypeScript** — Type-safe development
- **Vite** — Lightning-fast build tool
- **TailwindCSS** — Utility-first styling
- **Axios** — HTTP client

### Infrastructure
- **Render** — Backend hosting (free tier)
- **Vercel** — Frontend hosting (free tier)
- **GitHub** — Version control

---

## 🚀 Local Setup

### Prerequisites
- Python 3.9+
- Node.js 18+
- Git

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env with your credentials

# Run server
uvicorn app.main:app --reload
Backend runs on: http://localhost:8000

Frontend Setup
bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Run dev server
npm run dev
Frontend runs on: http://localhost:5173

🗂️ Project Structure
text
data-footprint-mapper/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes & models
│   │   ├── core/         # Config & security
│   │   ├── services/     # Business logic (OSINT engine)
│   │   └── main.py       # FastAPI app
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── hooks/        # Custom hooks
│   │   ├── types/        # TypeScript interfaces
│   │   ├── lib/          # API client
│   │   └── App.tsx
│   ├── package.json
│   └── .env.example
│
└── README.md
🔒 Privacy & Compliance
What We DON'T Do
❌ Store user inputs (emails/usernames)

❌ Log scan requests

❌ Track users with cookies/analytics

❌ Sell or share any data

❌ Require account creation

What We DO
✅ Process scans in real-time (ephemeral)

✅ Rate limit by IP (prevent abuse)

✅ Use open-source breach databases

✅ Provide transparent risk explanations

DPDP Act 2023 Compliant: No personal data collection = No consent needed.

📊 Platform Coverage
Categories (11 total)
Social Media (5 platforms)

E-Commerce India (5 platforms)

Food Delivery (5 platforms)

Job Portals India (5 platforms)

Fintech & Payments (5 platforms)

Education (5 platforms)

Streaming (5 platforms)

Travel & Booking (6 platforms)

Communication (5 platforms)

Gaming (5 platforms)

Professional Networks (5 platforms)

Total: 50+ platforms detected

🛣️ Roadmap
 HIBP (Have I Been Pwned) integration for breach detection

 Export results as PDF

 Dark mode

 Multi-email comparison

 Browser extension

 API for developers

🤝 Contributing
Contributions welcome! Please read CONTRIBUTING.md first.

📄 License
MIT License - See LICENSE for details.

👤 Author
Your Name
🔗 LinkedIn | Portfolio | GitHub

🙏 Acknowledgments
Have I Been Pwned for breach data

FastAPI for excellent documentation

Supabase & Upstash for free tiers

Built with privacy in mind 🔒