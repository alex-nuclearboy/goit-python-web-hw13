# Contact Management API

This repository hosts an enhanced version of a previous Contact Management project, which can be accessed [here](https://github.com/alex-nuclearboy/goit-python-web-hw12). This prior version includes a REST API for managing contact information, built using FastAPI and SQLAlchemy, leveraging PostgreSQL as the backend database. It supports basic CRUD operations for managing contacts along with additional features such as contact search by various attributes and retrieval of contacts with upcoming birthdays.

## Key Features

### Original Features:
- **Create new contacts:** Add new entries to the database.
- **Retrieve all contacts:** Fetch all contacts with pagination support.
- **Retrieve a single contact by ID:** Access details of a specific contact.
- **Update existing contacts:** Modify details of existing contacts.
- **Delete contacts:** Remove contact entries from the database.
- **Search for contacts:** Search for contacts by name, email, or phone number.
- **List upcoming birthdays:** Display contacts whose birthdays occur within the next week.
- **User Authentication:** Allows new users to register and authenticate returning users using secure hashing and JWT tokens.
- **Authorization:** Secures API endpoints with JWT-based authorization, ensuring that only authorized users can access specific actions.
### Extended Features:
- **Email Verification:** Implements a mechanism to verify the email addresses of registered users.
- **Rate Limiting:** Restricts the number of requests to contact routes to prevent abuse, specifically limiting the rate of contact creation.
- **CORS Support:** Enables Cross-Origin Resource Sharing (CORS) for the REST API.
- **User Avatar Update:** Integrates with the Cloudinary service to allow users to update their avatar images.

## Technologies Used
- **FastAPI:** For creating the REST API.
- **SQLAlchemy:** As the ORM for database interactions.
- **PostgreSQL:** As the backend database.
- **Pydantic:** For data validation.
- **Alembic:** For database migrations.
- **Docker:** Used to containerize the application and PostgreSQL database.
- **Poetry:** For managing Python package dependencies and virtual environments.
- **Cloudinary:** For managing user avatars.

## Installation and Usage

### Prerequisites

- **Docker and Docker Compose:** Ensure you have Docker and Docker Compose installed on your system to handle the application and database containers.
- **Python:** Ensure Python 3.10 or higher is installed on your system.
- **Poetry:** This project uses Poetry for dependency management.

### Setting Up the Project

- **Clone the Repository:**
```bash
git clone https://github.com/alex-nuclearboy/goit-python-web-hw13.git
```

- **Navigate to the Project Directory:**
```bash
cd goit-python-web-hw13/first_task
```

- **Environment Setup**

Create a `.env` file with the following content and substitute your values:

```plaintext
# Database PostgreSQL
POSTGRES_DB=rest_app
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

SQLALCHEMY_DATABASE_URL=postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

# JWT authentication
SECRET_KEY=
ALGORITHM=HS256

# Email service
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_PORT=
MAIL_SERVER=

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379

# Cloud Storage
CLOUDINARY_NAME=
CLOUDINARY_API_KEY=
CLOUDINARY_API_SECRET=
```

- **Activate the Poetry Environment and Install Dependencies:**
```bash
poetry shell
poetry install --no-root
```

- **Start the PostgreSQL Server:**
```bash
docker compose up -d
```

- **Run Alembic Migrations**
```bash
alembic upgrade head
```

### Starting

- **Running the FastAPI application** using Uvicorn:
```bash
uvicorn main:app --host localhost --port 8000 --reload
```

Access the API at [http://localhost:8000](http://localhost:8000) and the Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs) for testing API endpoints.

### Stopping the Application and Exiting

When you are finished using the application, follow these steps to properly shut down the server and exit the development environment:

- **Stop the Application:**

To stop the FastAPI application, press `CTRL+C` in the terminal window where the server is running. This will terminate the server process.

- **Shut Down the PostgreSQL Server:**

```bash
docker compose down
```

This command stops the running containers and removes the containers created by docker compose up, along with their networks. It’s a clean way to ensure that no unnecessary Docker processes remain running.

To stop the container but not remove it, use:
```bash
docker compose stop
```

- **Exit the Poetry Environment**
```bash
exit
```

This command will deactivate the virtual environment and return you to your system's default environment.
