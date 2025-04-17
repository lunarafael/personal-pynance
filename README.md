# Personal-Pynance - Personal Finance Management System

**Pynance** is a personal finance management system built with Django (backend), PostgreSQL (database), and consumed via a REST API. The purpose of this project is to provide a simple and efficient way for users to track their personal finances, with categories for expenses, transactions, and reports. This project was developed as a part of a personal learning journey to understand Django and RESTful APIs better.

## Technologies Used

- **Backend**: Django, Django Rest Framework (DRF).
- **Database**: PostgreSQL.
- **Authentication**: JWT (JSON Web Tokens).
- **Docker**: Docker and Docker Compose to manage the environment.
- **Testing**: Pytest for unit and integration tests.

## Project Structure

The project is organized as follows:

```
    personal-pynance/ 
    └───backend 
        ├───finance           # Main app (transactions, categories, etc.) 
        │   ├───migrations    # Django migrations for the finance app 
        │   └───tests         # Tests for the finance app
        ├───pynance           # Main Django configurations 
        └───users             # User management app (authentication, registration, etc.) 
            ├───migrations    # Django migrations for the users app 
            └───tests         # Tests for the users app
```
The `backend` folder contains the Django project, with separate folders for the main application (`pynance`), the finance app (`finance`), and the user management app (`users`). Each app has its own migrations and tests directories. The root directory contains the `docker-compose.yml` and `Dockerfile` files, which are used to manage the Docker images and containers for the project.

## Running the Project with Docker Compose

This project uses Docker Compose to manage the containers. Below are the instructions to run the project.

### Prerequisites

- Git installed on your machine.
- Docker and Docker Compose installed on your machine.
- Internet connection to pull the Docker images.

### Running the Application

1. Clone the repository:

   ```bash
   git clone https://github.com/lunarafael/personal-pynance.git
   cd personal-pynance
   ```
   Or download the ZIP file and extract it. Make sure to navigate to the `personal-pynance` directory after cloning or extracting.

2. Build and start the containers:

    ```bash
    docker-compose up --build
    ```

This command will build the images and start the containers for the backend, the database (PostgreSQL), and other required services.

3. The application will be available at:
   - Backend (API): http://localhost:8000/api/
   - Admin: http://localhost:8000/admin/

4. To stop the application, use:

    ```bash
    docker-compose down
    ```

## Running Tests

You can run the tests using Docker to access the container and execute the commands inside the configured environment.

### Running Tests with Pytest

1. Access the backend container:

    ```bash
    docker-compose exec backend bash
    ```

2. Navigate to the backend folder:

    ```bash
    cd backend
    ```

3. Run the tests with Pytest:

    ```bash
    pytest -o log_cli=true --log-level=INFO
    ```

    This command runs the tests and shows the logs in the terminal, making it easier to follow the test execution process.

4. For more details on the tests, you can check the test files in `backend/finance/tests/` or `backend/users/tests/`.

## Environment Variables

Make sure to set the necessary environment variables for your development or production setup.

Create a `.env` file in the root of the project so that `docker-compose` can easily load these variables. This improves security and makes configuration management simpler.

The main variables are:

- `DB_NAME`: The name of the PostgreSQL database
- `DB_USER`: The database user
- `DB_PASSWORD`: The database user's password
- `DJANGO_SETTINGS_MODULE`: Should remain set to `pynance.settings`

Example `.env` file:

```env
DB_NAME=pynance_db
DB_USER=pynance_user
DB_PASSWORD=supersecurepassword
DJANGO_SETTINGS_MODULE=pynance.settings
```