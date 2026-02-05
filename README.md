🏗️ **Infrastructure:** This application is deployed on an [FDIC-Style Azure DevSecOps Platform](https://github.com/rjabeen04/fdic-style-azure-devsecops) using Terraform and AKS.

# 🎶 Musical Volunteer App

A simple web application that connects volunteer musicians with elder care homes for live performances. Built using Flask and Docker, this app allows musicians to sign up and institutions to view available volunteers.

---

## 📋 Features

- 🎸 **Volunteer Sign-Up Form**: Musicians can enter their name, instrument, and availability.
- 👥 **View Volunteers**: See a list of all volunteers who have signed up.
- 🐳 **Dockerized App**: Easy to build and deploy using Docker and Docker Compose.
- 💾 **Redis Integration**: Stores volunteer data temporarily using Redis.
- 🌐 **Runs Locally**: Fully self-contained; no need for external databases.

---

## 🛠️ Tech Stack

| Tool            | Purpose                              |
|----------------|--------------------------------------|
| **Python & Flask** | Backend and routing logic            |
| **HTML & Jinja2** | Templating engine for the front end  |
| **Redis** | Temporary in-memory storage          |
| **Docker** | Containerization                      |
| **Docker Compose** | Multi-container orchestration        |
| **Git & GitHub** | Version control and source hosting   |

---

## 🚢 Deployment & DevSecOps
While this app can run locally, it is designed as a production-ready workload for a highly regulated Azure environment.
- **Platform:** Hosted on Azure Kubernetes Service (AKS).
- **Security:** Secrets managed via Azure Key Vault with RBAC.
- **Ingress:** Secured via Azure Application Gateway with Web Application Firewall (WAF).
- **CI/CD:** Fully automated via GitHub Actions with IaC security scanning.

---

## 🚀 Getting Started

### 1. Clone this Repository
```bash
git clone [https://github.com/rjabeen04/musical-volunteer.git](https://github.com/rjabeen04/musical-volunteer.git)
cd musical-volunteer
