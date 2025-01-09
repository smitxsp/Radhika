Contact Us with Django

This repository contains a Django-based web application that allows users to submit their contact information and inquiries through a "Contact Us" form. The application demonstrates key Django features such as forms, models, and database integration, providing a solid foundation for a real-world contact management system.

Features

Contact Form: Users can submit their name, email, subject, and message.

Database Storage: Submitted data is saved in the database for future reference.

Admin Panel: Manage and view submitted inquiries via the Django Admin interface.

Validation: Form validation ensures all required fields are completed before submission.

User-friendly Interface: A responsive and clean design for the form.

Installation

Follow the steps below to set up the project on your local machine:

Clone the Repository:

Installation

Follow the steps below to set up the project on your local machine:

Clone the Repository:

git clone https://github.com/your-username/contact_us_with_Django.git
cd contact_us_with_Django

Create a Virtual Environment:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install Dependencies:

pip install -r requirements.txt

Set Up the Database:

python manage.py makemigrations
python manage.py migrate

Run the Development Server:

python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/.

Project Structure

contact_us_with_Django/
├── contact_app/       # Django app handling the contact form
│   ├── migrations/    # Database migrations
│   ├── templates/     # HTML templates
│   ├── views.py       # View logic for the contact form
│   ├── models.py      # Database models
│   ├── forms.py       # Django forms
│   └── urls.py        # App-specific routes
├── contact_us_with_Django/  # Project settings
├── db.sqlite3         # Default SQLite database
├── manage.py          # Django project management script
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

Usage

Navigate to the homepage where the "Contact Us" form is displayed.

Fill out the form with the required information (name, email, subject, message) and submit it.

Administrators can view submitted forms via the Django Admin panel.

Technologies Used

Backend: Django (Python)

Frontend: HTML, CSS (Bootstrap for styling)

Database: SQLite (default, can be replaced with other databases)

Contribution

Contributions are welcome! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

