# 🐳 Microservices with Flask, Docker, Kubernetes, and AWS Load Balancer

This project demonstrates how to deploy a simple microservices architecture using:

- 🐍 Flask Web Apps (Two separate apps)
- 🐳 Docker for containerization
- ☸️ Kubernetes for orchestration
- 🌐 Ingress Controller for traffic routing
- ⚙️ AWS Load Balancer for external access

---

## 📦 Apps Description

### App 1: `/available-products`
A Flask app that returns a list of available products with prices.

### App 2: `/sold-out-products`
A Flask app that returns a list of sold-out products.

---

## 🔧 Setup Overview

### 1. Dockerize the Flask Apps
Each app has its own `Dockerfile` and is built separately.

### 2. Push Images to Docker Hub
> 🚨 I learned that **locally built Docker images can't be used by Kubernetes directly** unless pushed to a public or accessible container registry (like Docker Hub).
> That's why I tagged the images and pushed them using:

```bash
docker tag app1-available-products mkhattab77/app1-available-products
docker push mkhattab77/app1-available-products
