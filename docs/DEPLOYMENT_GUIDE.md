# Smart Resume Analyzer | Cloud Deployment Guide

This guide provides step-by-step instructions to deploy the **Smart Resume Analyzer** to cloud hosting platforms for free.

---

## Option 1: Deploy on Render (Recommended & 100% Free)

Render provides free hosting for Python web applications with automatic deploys directly from GitHub.

### Step 1: Sign Up / Log In
1. Visit **[render.com](https://render.com/)** and log in with your GitHub account (`subbaraju-cmd`).

### Step 2: Create a New Web Service
1. On the Render Dashboard, click the **New +** button and select **Web Service**.
2. Select **Build and deploy from a Git repository**.
3. Choose your repository: **`subbaraju-cmd/Smart-Resume-Analyzer`**.

### Step 3: Configure Settings
Fill in the configuration fields:
- **Name:** `smart-resume-analyzer` (or your preferred name)
- **Region:** Any region closest to you (e.g., Singapore or Oregon)
- **Branch:** `main`
- **Root Directory:** *(leave blank)*
- **Runtime:** **Python 3**
- **Build Command:**
  ```bash
  pip install -r requirements.txt
  ```
- **Start Command:**
  ```bash
  gunicorn app:app
  ```
- **Instance Type:** **Free**

### Step 4: Click Deploy
1. Click **Create Web Service**.
2. Render will automatically pull the repository, install dependencies from `requirements.txt`, and start the app with Gunicorn.
3. Once the build completes, your live deployment link will be displayed at the top:
   `https://smart-resume-analyzer-xxxx.onrender.com`

---

## Option 2: Deploy on Railway

1. Visit **[railway.app](https://railway.app/)** and connect with GitHub.
2. Click **New Project** $\rightarrow$ **Deploy from GitHub repo**.
3. Select `subbaraju-cmd/Smart-Resume-Analyzer`.
4. Railway automatically reads `Procfile` (`web: gunicorn app:app`) and deploys.
5. In project settings, click **Generate Domain** to get your public live URL.

---

## Local Development Link
While developing locally, the application runs at:
- **`http://127.0.0.1:5000`**
