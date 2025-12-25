# Complaint Management System

## Overview

The Complaint Management System is a web application built using Flask. It allows users to register, log in, and submit complaints. Admin users can review and manage complaints, providing a streamlined process for complaint resolution.

## Features

- **User Authentication**: Register, log in, and log out functionality.
- **Complaint Submission**: Users can create and view their complaints.
- **Admin Panel**: Admins can review, approve, or reject complaints.
- **Role-Based Access Control**: Different functionalities for users and admins.
- **Responsive Design**: User-friendly interface with responsive design.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML, CSS, Bootstrap
- **Authentication**: Flask-Login
- **ORM**: SQLAlchemy

## Installation

1. Clone the repository:

   ```bash
   git clone complaint_management_system_flask.git
   cd complaint_management_system_flask
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. Run the application:

   ```bash
   flask run
   ```

6. Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

```
complaint_management_system_flask/
├── app/
│   ├── __init__.py
│   ├── decorators.py
│   ├── extenshions.py
│   ├── forms.py
│   ├── models.py
│   └── routes/
│       ├── admin.py
│       ├── auth.py
│       └── complaints.py
├── templates/
│   ├── all_complaints.html
│   ├── base.html
│   ├── create.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   └── review_complaint.html
├── config.py
├── requirements.txt
└── README.md
```

## License

This project is licensed under the MIT License.
