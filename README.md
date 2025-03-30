# Bookstore

This is Django-based web app. The application uses PostgreSQL as its database, and it’s built to be fully customizable with a modular structure, including components for goods management, user authentication, orders, and more.
This project allows users to browse books, add them to a cart, place orders, and manage their profiles. 

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.8+
- Django 4.2.7+
- PostgreSQL
- `pip` (for installing dependencies)

## Setup Instructions

### 1. Clone this Repository

### 2. Set Up the Virtual Environment

Create and activate a virtual environment to manage dependencies.

python -m venv .venv
source .venv/bin/activate  # On Mac/Linux
.venv\Scripts\activate     # On Windows

### 3. Install Dependencies

Install the required packages using pip:
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables

Create a .env file in the root of the project and configure the following "env.example" file


### 5. Apply Migrations

Run the following command to apply migrations to the PostgreSQL database:
```bash
python manage.py migrate
```
### 6. Run the Development Server

Start the development server:
```bash
python manage.py runserver
```
You should now be able to access the application at http://127.0.0.1:8000/.

## Technologies Used

- Django
- PostgreSQL
- Python-dotenv
- Django Debug Toolbar
- Django Channels
- Pillow
- Bootstrap
- Ajax
- jQuery

## Interface
1.Catalog\
<img width="600" alt="Screenshot 2025-03-30 at 22 01 31" src="https://github.com/user-attachments/assets/6066cb6f-8c1a-47a4-88ad-c9b82105f151" />\
2. Product Item\
<img width="600" alt="Screenshot 2025-03-30 at 22 02 09" src="https://github.com/user-attachments/assets/b85b824c-a278-4966-a3a6-4603ce9d3e43" />\
3.Shopping Cart\
<img width="600" alt="Screenshot 2025-03-30 at 22 02 30" src="https://github.com/user-attachments/assets/7c8d0512-ed4e-4b77-8623-d828328089c8" />\
4.Order creation\
<img width="600" alt="Screenshot 2025-03-30 at 22 04 25" src="https://github.com/user-attachments/assets/59079fa9-7e63-48b5-8980-17777a4c434a" />\
5.Profile Page\
<img width="600" alt="Screenshot 2025-03-30 at 22 05 05" src="https://github.com/user-attachments/assets/62abd868-85b9-4f44-9855-56e9f434fd0d" />
