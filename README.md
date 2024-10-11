# Airline Management System Dashboard

## Overview

The **Airline Management System Dashboard** is a web application built with Django as the backend and HTML with Bootstrap CSS for the frontend. This system provides a comprehensive platform for managing various aspects of an airline, including flights, planes, passengers, pilots, crew members, and airports.

## Features

- **User Authentication**: Secure login for users to manage airline data.
- **Flight Management**: Create, update, and delete flight information.
- **Plane Management**: Maintain records of planes and their specifications.
- **Passenger Management**: Manage passenger details and bookings.
- **Pilot and Crew Management**: Keep track of pilots and crew members associated with flights.
- **Airport Management**: Manage information about airports served by the airline.

## Technologies Used

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, Bootstrap CSS
- **Database**: MySQL
- **Version Control**: Git

## Installation

To set up the Airline Management System on your local machine, follow these steps:

### Prerequisites

- Python 3.x installed on your machine
- Django installed (use `pip install django`)
- MySQL database server installed and running

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gonz-tyler/airline-management-system.git
   cd airline-management-system
   ```
2. **Create a virtual environment (optional but recommended)**:

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
3. **Install dependencies**:

```bash
pip install -r requirements.txt
```
4. **Set up the MySQL database**:

- Create a new MySQL database for the project.
- Update the DATABASES setting in settings.py with your MySQL database credentials.
- Run migrations:
    ```bash
    python manage.py migrate
    ```
5. **Create a superuser (optional)**:
    ```bash
    python manage.py createsuperuser
    ```
6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```
7. **Access the dashboard**:
   - Open your web browser and navigate to http://127.0.0.1:8000/.

##Usage
- Log in with your credentials (or create a superuser if you haven't).
- Navigate through the dashboard to manage flights, planes, passengers, pilots, crew members, and airports.
## Contributing
Contributions are welcome!
## License
This project is licensed under the MIT License - see the LICENSE file for details.

##Acknowledgements
 - [Django Documentation](https://docs.djangoproject.com/).
 - [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/))
 - [MySQL Documentation](https://dev.mysql.com/doc/)

