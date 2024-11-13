# Eliteross

## Description

This API is designed for managing personal training services. It allows detailed client records, assigning mesocycles based on their goals, and storing information about exercises, repetitions, frequency, stretching exercises, calories, and macronutrients. It also allows storing images to evaluate progress, calculating progress, and sending reports.

## Project Status

This project is currently under development. Some features may not be complete or may change.

## Features

- Detailed client records.
- Assigning mesocycles based on client goals.
- Managing exercises, repetitions, frequency, and stretching exercises.
- Storing calories and macronutrients.
- Storing images to evaluate progress.
- Calculating progress.
- Tracking historical data for skinfolds and circumferences to apply different formulas for measuring BMI, body fat, etc.
- Sending reports.

## Prerequisites

List of software and tools you need to have installed to run the project.

- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [django-filter](https://django-filter.readthedocs.io/en/stable/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [Pillow](https://pypi.org/project/Pillow/)

## Installation

Steps to set up the local development environment.

1. Clone the repository:
    ```sh
    git clone https://github.com/dominguesleo/eliteross_api.git
    cd eliteross_api
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

