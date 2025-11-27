# Restaurant Management System

A complete Restaurant Management System with Django backend and HTML/JS frontend.

## Features

- **Authentication**: Custom User model with Admin/Staff roles.
- **Menu Management**: Categories and Items.
- **Order Management**: Tables, Orders, Order Items.
- **Inventory Management**: Stock tracking and low-stock alerts.
- **Inventory Deduction**: Automatic deduction when orders are placed.
- **API**: Full REST API with documentation.

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (Package Manager)

## Setup Instructions

### Backend Setup

1.  **Navigate to the project folder:**
    Make sure you are inside the `restaurant_management_system` directory.

    ```bash
    cd restaurant_management_system
    ```

2.  **Create a virtual environment:**

    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**

    - **Windows (PowerShell):**
      ```powershell
      .venv\Scripts\activate
      ```
    - **macOS/Linux:**
      ```bash
      source .venv/bin/activate
      ```

4.  **Install dependencies:**

    ```bash
    uv pip install -r requirements.txt
    ```

5.  **Apply Database Migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create an Admin User (Optional):**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the Application:**

    ```bash
    python manage.py runserver
    ```

    The server will start at `http://127.0.0.1:8000/`.

8.  **Access the Application:**
    Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    You will be redirected to the Login page. If you don't have an account, click "Sign Up" to create one.

## API Documentation

The API endpoints are available at `http://127.0.0.1:8000/api/`:

- **Auth**: `/api/auth/`
- **Menu**: `/api/menu/`
- **Orders**: `/api/orders/`
- **Inventory**: `/api/inventory/`
