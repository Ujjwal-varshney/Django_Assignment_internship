# Django User Authentication Application

## Overview
This Django project implements user authentication using either an email or username along with a password. It features login, signup, password reset, password change, dashboard, and profile pages. Access to certain pages is restricted based on the user's authentication status.

## Features
- User login via email or username and password.
- Pages for login, signup, password reset, password change, dashboard, and profile.
- Restricted access to specific pages depending on whether the user is authenticated.

## Requirements
- Python 3.x
- Django 3.x or newer

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-repo/django-auth-app.git
    cd django-auth-app
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the database migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

6. **Start the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and navigate to `http://127.0.0.1:8000`.

## Pages and Features

### 1. Login Page
- **Fields**: Username/Email, Password
- **Links/Buttons**: Sign Up, Forgot Password

### 2. Sign Up Page
- **Fields**: Username, Email, Password, Confirm Password
- **Links/Buttons**: Back to Login

### 3. Forgot Password Page
- **Fields**: Email
- **Button**: Send reset instructions
- **Functionality**: Sends an email with a password reset link

### 4. Change Password Page
- **Access**: Requires authentication
- **Fields**: Old Password, New Password, Confirm Password
- **Links/Buttons**: Back to Dashboard

### 5. Dashboard
- **Access**: Only for authenticated users
- **Content**: Greeting message ("Hi, username!"), links to Profile and Change Password pages, Logout option

### 6. Profile Page
- **Content**: Displays Username, Email, Date Joined, Last Updated
- **Links/Buttons**: Back to Dashboard, Logout

## Project Structure

django-auth-app/
├── manage.py
├── myapp/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── change_password.html
│ │ ├── dashboard.html
│ │ ├── forgot_password.html
│ │ ├── login.html
│ │ ├── profile.html
│ │ ├── signup.html
│ ├── urls.py
│ ├── views.py
├── db.sqlite3
├── requirements.txt
└── README.md