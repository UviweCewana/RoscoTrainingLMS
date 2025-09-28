# 📚 Learner Portfolio Data Pipeline

**End-to-end MVP** for automated learner portfolio generation. Built with FastAPI, Postgres, React, Google Drive API, and AWS (EC2 + RDS). 

✨ **Core features**
- Auto-create learner folders on LMS events (via webhooks)
- Store assignments, quizzes, and certificates in cloud storage
- Compile portfolio → digital flipbook + downloadable PDF
- Admin dashboard to manage integrations & monitor learners

---

## 🏗️ Architecture
![Architecture Diagram](samples/architecture.png)

---

## 🚀 Run locally

### Prerequisites
- Docker + Docker Compose
- Node.js 18+ (if running frontend outside Docker)

### Quickstart
```bash
git clone https://github.com/UviweCewana/RoscoTrainingLMS
cd rosco-training-lms
cp .env.example .env

docker-compose up --build
