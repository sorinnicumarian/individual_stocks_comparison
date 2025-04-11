
# Installation Instructions

This document provides the step-by-step guide to install and set up the **Individual Stocks Comparison** project on your local environment.

## Prerequisites

Before setting up the project, ensure that you have the following installed:

- **Python 3.x** (if you're using Python)
- **Node.js** and **npm** (if you're using Node.js)
- **Google Cloud SDK** (for setting up OAuth credentials)

## Step 1: Clone the Repository

First, clone the repository to your machine:

```bash
git clone https://github.com/yourusername/individual_stocks_comparison.git
cd individual_stocks_comparison
```

## Step 2: Set Up Your Environment

### 2.1. Install Dependencies

For **Python**:
- Install required Python dependencies:
  ```bash
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

For **Node.js**:
- Install required Node.js dependencies:
  ```bash
  npm install
  ```

### 2.2. Create `.env` file

Create a `.env` file in the root directory of your project to store environment variables. This file will be **ignored by Git** so it remains private.

#### Example `.env` file:

```bash
# Google Spreadsheet ID
SPREADSHEET_ID=17WqfEsuEs7ky-TyVRty8LNWdy8FihkKZF2OUYxuxgvg (obvious fake id used only as example; take it from your own google sheet URL)

# API Keys (for third-party services like Finnhub or others)
FINNHUB_API_KEY=your-api-key
```

### 2.3. Create OAuth `secret.json`

In order to access Google APIs (like Google Sheets), you need to create a **OAuth 2.0 client ID** and **secret**.

#### Steps to create `google_client_secret.json` (OAuth 2.0 credentials):

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. **Create a new project** or use an existing one.
3. In the left-hand menu, navigate to **API & Services > Credentials**.
4. Click **Create Credentials** and select **OAuth client ID**.
5. Set up the consent screen (you can leave most fields blank, just add your email and project name).
6. Choose **Web Application** as the application type.
7. Under **Authorized redirect URIs**, don't add anything if you develop online or add `http://localhost:8000` if you develop locally.
8. Click **Create**, and you will be provided with your **Client ID** and **Client Secret**.
9. Download the **JSON file** and save it as `google_client_secret.json` in your project directory.

### 2.4. Add `google_client_secret.json` and `.env` to `.gitignore`

To prevent your sensitive data from being committed to GitHub, add `google_client_secret.json` and `.env` to your `.gitignore` file.

```bash
# .gitignore
google_client_secret.json
.env
```

## Step 3: Develop Locally

### 3.1. Run Python Application

If you're using Python, you can run the application using the following command:

```bash
python src/main.py
```

Ensure your `.env` file and `google_client_secret.json` are correctly set up before running the application.

---

## Step 3: Develop in the Cloud (Optional Alternative)

If you'd like to develop in **GitHub Codespaces**, follow these steps to set up your development environment in the cloud.

### 1. Open the Repository in GitHub Codespaces

1. Go to the GitHub repository for the **Individual Stocks Comparison** project.
2. Click the green **Code** button located at the top-right of the repository page.
3. Select **Open with Codespaces** and then click **New codespace**. GitHub will create a new codespace environment for you to develop in.

### 2. Set Up the Development Environment

Once your codespace is ready, follow these steps:

1. **Install Python Extension**: 
   - GitHub Codespaces will automatically detect that you're working with Python. However, if the Python extension isn't already installed, you can install it manually by:
     - Clicking on the **Extensions** icon in the left sidebar.
     - Searching for **Python** and clicking **Install**.

2. **Install Dependencies**:
   - Open the terminal in Codespaces (from the bottom panel or `Ctrl + `).
   - Install the dependencies as you would in a local environment by running:
     ```bash
     pip install -r requirements.txt
     npm install
     ```

3. **Set Up `.env` file**:
   - Create a `.env` file in the root directory of your project, as explained in **Step 2: Set Up Your Environment**. Make sure to include the required environment variables.

4. **Run the Application**:
   - You can run the application in the same way as you would locally:
     ```bash
     python src/main.py
     ```
