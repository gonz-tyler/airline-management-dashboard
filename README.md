# ✈️ Airline Management System Dashboard

A comprehensive web platform for managing airline operations, built with Django and Bootstrap.

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

---
## Overview

The **Airline Management System Dashboard** is a web application built with Django on the backend and HTML with Bootstrap CSS for the frontend. This system provides a complete platform for managing various aspects of an airline, including flights, planes, passengers, pilots, crew members, and airports.

---
## 📸 Screenshot

> A live screenshot of the main dashboard interface.
> **(TODO: Replace this link with a real screenshot of your app!)**


`https://i.imgur.com/your-screenshot-url.png`

---
## ✨ Features

- **User Authentication**: Secure login for administrators to manage airline data.
- **Flight Management**: Create, read, update, and delete flight information.
- **Plane Management**: Maintain records of the aircraft fleet and their specifications.
- **Passenger Management**: Manage passenger details and their flight bookings.
- **Pilot and Crew Management**: Keep track of pilots and crew members assigned to flights.
- **Airport Management**: Manage information about airports served by the airline.

---
## 🛠️ Technologies Used

-   **Backend**: Django (Python web framework)
-   **Frontend**: HTML, Bootstrap CSS
-   **Database**: MySQL
-   **Version Control**: Git

---
## 🚀 Getting Started

To set up the Airline Management System on your local machine, follow these steps.

### Prerequisites

-   Python 3.x installed on your machine.
-   Django installed (`pip install django`).
-   MySQL database server installed and running.

### Installation Steps

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/gonz-tyler/airline-management-system.git](https://github.com/gonz-tyler/airline-management-system.git)
    cd airline-management-system
    ```

2.  **Create and activate a virtual environment** (optional but highly recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the MySQL database**:
    -   Create a new MySQL database for the project.
    -   Create a `.env` file in the project root with your MySQL credentials:
        ```env
        DB_NAME=<your_database_name>
        DB_USER=<your_database_username>
        DB_PASSWORD=<your_database_password>
        DB_HOST=localhost
        DB_PORT=3306
        ```
    -   Run database migrations to create the tables:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

5.  **Create a superuser** to access the admin dashboard:
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7.  **Access the dashboard**:
    -   Open your web browser and navigate to `http://127.0.0.1:8000/`.

---
## Usage

-   Log in with the superuser credentials you created.
-   Navigate through the dashboard to manage flights, planes, passengers, pilots, crew members, and airports.

---
## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

---
## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---
## Acknowledgements

-   [Django Documentation](https://docs.djangoproject.com/)
-   [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
-   [MySQL Documentation](https://dev.mysql.com/doc/)
