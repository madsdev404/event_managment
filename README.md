# Event Management System

## Assignment - 02

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-5.x-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Description

This is a comprehensive Event Management System built with Django, designed to streamline the process of organizing and managing various events. It provides functionalities for managing event categories, events themselves, and participants, along with a dashboard for quick insights.

## Features

- **Category Management**: Create, view, update, and delete event categories.
- **Event Management**: Create, view, update, and delete events with details like name, description, date, time, location, and category.
- **Participant Management**: Register, view, update, and delete participants, linking them to events.
- **Search and Filtering**: Easily search for events by name or location, and filter by category or date range.
- **Dashboard**: An administrative dashboard providing key statistics such as total participants, total events, upcoming events, past events, and today's events.
- **User-friendly Interface**: Built with Tailwind CSS for a modern and responsive design.

## Technologies Used

- **Backend**: Python 3.x, Django 5.x
- **Database**: PostgreSQL (via `psycopg2-binary`)
- **Styling**: Tailwind CSS, PostCSS
- **Other Python Libraries**: `Pillow` (for image handling), `Faker` (for data population), `python-decouple` (for environment variables), `django-debug-toolbar` (for development).

## Installation

Follow these steps to set up the project locally:

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/madsdev404/event_managment
    cd event_management
    ```

2.  **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:

    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

4.  **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up environment variables**:
    Create a `.env` file in the `event_management` directory (same level as `manage.py`) and add your database configuration and other sensitive settings. Example:

    ```
    SECRET_KEY=your_secret_key_here
    DEBUG=True
    DATABASE_URL=postgres://user:password@host:port/dbname
    ```

    _Note: For production, ensure `DEBUG` is `False` and `SECRET_KEY` is a strong, unique value._

6.  **Run database migrations**:

    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser (for admin access)**:

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin user.

8.  **Collect static files**:

    ```bash
    python manage.py collectstatic
    ```

9.  **Run the development server**:
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.

## Usage

After running the server, navigate to `http://127.0.0.1:8000/` in your web browser.

- **Admin Panel**: Access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials you created.
- **Dashboard**: View the event dashboard for statistics.
- **Manage Categories, Events, and Participants**: Use the provided interfaces to perform CRUD operations.
- **Search and Filter**: Utilize the search bar and filter options on the event listing page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
