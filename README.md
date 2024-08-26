# Personal Transaction Recorder

A simple web application to record personal transactions built with Flask, MongoDB, and deployed on Vercel.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Getting Started](#getting-started)
5. [Deployment on Vercel](#deployment-on-vercel)
6. [Usage](#usage)
7. [License](#license)

## Project Overview

This project is a web-based application that allows users to record and manage personal transactions. It includes functionalities such as adding transactions, searching for transactions by friend's name, and determining the balance owed or to be received.

## Features

- Add new transactions (debit/credit).
- Search for transactions by friend's name.
- Calculate the balance to be paid or received.
- Deployable to Vercel for easy access.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- A MongoDB account and a cluster set up (either locally or in the cloud).
- Git installed for version control.
- A Vercel account for deployment.

## Getting Started

Follow these steps to get a copy of the project up and running on your local machine for development and testing purposes.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/transaction-recorder.git
cd transaction-recorder
```

### 2. Set Up a Virtual Environment
Create a virtual environment
```bash
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
### 3. Install the Required Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables
Create a .env file in the root directory of the project to store your environment variables. This file should contain:

```bash
MONGODB_URI="your_mongodb_uri"
```
Replace your_mongodb_uri with your actual MongoDB connection string and your_flask_secret_key with a secret key for Flask.

### 5. Run the Application Locally
```bash
Copy code
flask run
```
Open your web browser and navigate to http://127.0.0.1:5000 to see the application in action.

## Deployment on Vercel
To deploy this application on Vercel, follow these steps:

## 1. Push Your Code to GitHub
Ensure your latest changes are committed and pushed to your GitHub repository:

```bash
git add .
git commit -m "Initial commit"
git push origin main
```
## 2. Connect Your GitHub Repository to Vercel
Log in to your Vercel account.
Click on New Project.
Import the repository from GitHub.
Follow the prompts to configure your project.
### 3. Configure Environment Variables on Vercel
Go to your Vercel dashboard and select your project.
Click on Settings > Environment Variables.
Add the same environment variables from your .env file:
makefile
```bash
MONGODB_URI="your_mongodb_uri"
FLASK_SECRET_KEY="your_flask_secret_key"
```
### 4. Create a vercel.json File
Add a vercel.json file to the root of your project directory to specify the build settings for Vercel:

```json
Copy code
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### 5. Deploy the Project
Click Deploy on the Vercel dashboard.
Wait for the deployment to complete. You will get a URL to access your deployed application.
### Usage
Open the deployed application in your browser.
Log in using the correct credentials.
Add, view, and manage your personal transactions.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

vbnet
Copy code

---

### Instructions to Use

1. **Copy the Above Markdown**: Copy all the text above and paste it into a new file named `README.md` in the root of your repository.
2. **Edit the Content**: Make sure to replace placeholders such as `your-username` and `your_mongodb_uri` with your actual GitHub username and MongoDB URI.
3. **Save and Commit**: Save the file, add it to your git repository, commit the changes, and push it to GitHub.

By following these instructions, anyone will be able to set up, run, and deploy their own version of your tra
