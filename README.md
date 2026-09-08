# Noodles Store
## Description
Noodle Store is a Django-based web application built to showcase and manage a catalog of noodle products for an online food store. The application allows visitors to browse through available noodle varieties, view individual product pages with full details such as name, description, price and category, and explore items organized by category for easier navigation. On the backend, the project includes a fully functional Django admin panel that lets an administrator add new products, update existing listings, upload product images, and manage the overall catalog without touching any code. The project follows a clean structure with reusable templates and environment-based configuration, making it easy to maintain and extend with features like a shopping cart or order system in the future.
## Features
- View noodles products
- View product details
- Product names, descriptions and prices
- Product images
- Product categories
- Django admin panel for managing products
## Technologies Used
- Python
- Django
- HTML
- CSS
- SQLite
## Requirements
The required Python packages are listed in `requirements.txt`.
## Installation

1. Clone the repository

   git clone https://github.com/tayyabadev11/noodle-store.git

   cd noodle-store

2. Create and activate a virtual environment

   python -m venv venv

   venv\Scripts\activate

3. Install the required packages

   pip install -r requirements.txt

4. Create a `.env` file in the project root and add

   SECRET_KEY=your-secret-key
 
   DEBUG=True

5. Run migrations

   python manage.py makemigrations

   python manage.py migrate

6. Create a superuser (optional, for admin access)

   python manage.py createsuperuser

7. Run the development server

   python manage.py runserver

8. Open `http://127.0.0.1:8000/` in your browser

## Requirements
The required Python packages are listed in `requirements.txt`.
## Environment
Project configuration and sensitive settings are managed using environment variables.
## Author
Tayyaba