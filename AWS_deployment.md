# AWS Deployment Guide for Music Recommendation System 🎵

This guide will help you deploy the Music Recommendation System on an AWS EC2 instance using Docker.

---

## Prerequisites

- AWS Account
- EC2 instance (Ubuntu)
- Docker and Git installed on EC2
- Open ports 22 (SSH), 80 (HTTP), and 8501 (Streamlit) in your security group
- Your project repository: [https://github.com/Gaurvi11/Music-recommendation-system](https://github.com/Gaurvi11/Music-recommendation-system)

---

## Step-by-Step Deployment

### 1. Launch an EC2 Instance

- Go to [AWS EC2 Console](https://console.aws.amazon.com/ec2/)
- Choose:
  - **Ubuntu Server 20.04 LTS**
  - **t2.micro** (Free Tier eligible)
  - Configure Security Group:
    - Allow SSH (port 22)
    - Allow HTTP (port 80)
    - Allow Custom TCP (port 8501) — for Streamlit app

Download the `.pem` key file to access your instance.

---

### 2. Connect to EC2 via SSH

Open terminal in your local system and run:

```bash
ssh -i "your-key.pem" ubuntu@your-ec2-public-ip

