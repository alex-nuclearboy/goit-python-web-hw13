# REST API and Django Projects

This repository hosts two distinct projects: a Contact Management API built with FastAPI and a Quotes Web Application built with Django. Both projects demonstrate advanced features of their respective frameworks, including user authentication, CRUD operations, and database management.

### Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/alex-nuclearboy/goit-python-web-hw13.git
```

## Table of Contents
1. [Contact Management API](#contact-management-api)
   - [Key Features](#contact-management-api-key-features)
   - [Technologies Used](#contact-management-api-technologies-used)
   - [Installation and Usage](#contact-management-api-installation-and-usage)
   - [Stopping the Application and Exiting](#stopping-the-contact-management-api-and-exiting)
2. [Quotes Web Application](#quotes-web-application)
   - [Key Features](#quotes-web-application-key-features)
   - [Technologies Used](#quotes-web-application-technologies-used)
   - [Installation and Usage](#quotes-web-application-installation-and-usage)
   - [How to Use the "Quotes" Website](#how-to-use-the-quotes-website)
   - [Stopping the Server and Exiting](#stopping-the-server-and-exiting)


## Contact Management API

This section of the repository enhances a previous Contact Management project, accessible [here](https://github.com/alex-nuclearboy/goit-python-web-hw12). This prior version includes a REST API for managing contact information, built using FastAPI and SQLAlchemy, leveraging PostgreSQL as the backend database. It supports basic CRUD operations for managing contacts along with additional features such as contact search by various attributes and retrieval of contacts with upcoming birthdays.

### Contact Management API Key Features

#### Original Features:
- **Create new contacts:** Add new entries to the database.
- **Retrieve all contacts:** Fetch all contacts with pagination support.
- **Retrieve a single contact by ID:** Access details of a specific contact.
- **Update existing contacts:** Modify details of existing contacts.
- **Delete contacts:** Remove contact entries from the database.
- **Search for contacts:** Search for contacts by name, email, or phone number.
- **List upcoming birthdays:** Display contacts whose birthdays occur within the next week.
- **User Authentication:** Allows new users to register and authenticate returning users using secure hashing and JWT tokens.
- **Authorization:** Secures API endpoints with JWT-based authorization, ensuring that only authorized users can access specific actions.

#### New in this extension:
- **Email Verification:** Implements a mechanism to verify the email addresses of registered users.
- **Rate Limiting:** Restricts the number of requests to contact routes to prevent abuse, specifically limiting the rate of contact creation.
- **CORS Support:** Enables Cross-Origin Resource Sharing (CORS) for the REST API.
- **User Avatar Update:** Integrates with the Cloudinary service to allow users to update their avatar images.

### Contact Management API Technologies Used
- **FastAPI:** For creating the REST API.
- **SQLAlchemy:** As the ORM for database interactions.
- **PostgreSQL:** As the backend database.
- **Pydantic:** For data validation.
- **Alembic:** For database migrations.
- **Docker:** Used to containerize the application and PostgreSQL database.
- **Poetry:** For managing Python package dependencies and virtual environments.
- **Cloudinary:** For managing user avatars.

### Contact Management API Installation and Usage

#### Prerequisites

- **Docker and Docker Compose:** Ensure you have Docker and Docker Compose installed on your system to handle the application and database containers.
- **Python:** Ensure Python 3.10 or higher is installed on your system.
- **Poetry:** This project uses Poetry for dependency management.

#### Setting Up the Project

- **Navigate to the Project Directory:**
```bash
cd goit-python-web-hw13/first_task
```

- **To set up the environment** use the following commands depending on your operating system:
    - Unix/Linux/macOS:
    ```bash
    cp .env.example .env
    ```
    - Windows:
    ```powershell
    copy .env.example .env
    ```

Edit the `.env` file with your settings.

- **Activate the Poetry Environment and Install Dependencies:**
```bash
poetry shell
poetry install --no-root
```

- **Start the PostgreSQL Server** using Docker Compose:
```bash
docker compose up -d
```

- **Run Alembic Migrations**
```bash
alembic upgrade head
```

#### Starting

- **Launch the FastAPI application** using Uvicorn:
```bash
uvicorn main:app --host localhost --port 8000 --reload
```

Access the API at [http://localhost:8000](http://localhost:8000) and the Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs) for testing API endpoints.

### Stopping the Contact Management API and Exiting

When you are finished using the application, follow these steps to properly shut down the server and exit the development environment:

#### Stop the Application:

To stop the FastAPI application, press `CTRL+C` in the terminal window where the server is running. This will terminate the server process.

#### Shut Down the PostgreSQL Server:

If you've started the PostgreSQL server using Docker Compose and wish to stop it, you can use the following command:

- **To stop and remove containers, networks, and volumes:**
```bash
docker compose down
```

- **To stop the server without removing resources:**
```bash
docker compose stop
```

#### Exit the Poetry Environment
```bash
exit
```

This command will deactivate the virtual environment and return you to your system's default environment.

<a href="#rest-api-and-django-projects" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; display: inline-block; border-radius: 8px; text-decoration: none;">Back to Top</a>

## Quotes Web Application

This section of the repository features an enhanced version of a "Quotes" Website Project, accessible [here](https://github.com/alex-nuclearboy/goit-python-web-hw10). 
This Python-based Django project is a dynamic website dedicated to the exploration and sharing of famous quotations. The site serves as an educational platform to demonstrate practical applications of Django, highlighting advanced features like user authentication, database migrations, and environment variable management. The project aims to provide a practical demonstration of advanced Django features, database handling, and personalized user management.

### Quotes Web Application Key Features

#### Original Features:
- **Viewing Content:** Visitors can view all uploaded quotes and read detailed biographies of authors without logging in.
- **User Authentication:** Supports user registration and login, enabling personalized experiences on the site.
- **User Profile Management:** Users can set and update their profile pictures (avatars), personalizing their interaction with the site.
- **Author and Quote Management:** Registered users have the privilege to add, edit and delete authors, tags, and quotes. This makes the site interactive and continuously evolving.
- **Tagging System:** Registered users can create tags for quotes, facilitating efficient categorization and retrieval, and enhancing the browsing experience.
- **Data Migration:** Demonstrates robust data migration from Atlas MongoDB to PostgreSQL, showcasing the handling of data across different database systems.
- **Search Functionality:** Features a tag-based search that allows visitors to find all quotes associated with a selected tag.
- **Top Ten Tags:** Displays the ten most popular tags dynamically, highlighting the most talked-about topics.
- **Pagination:** Implements pagination to manage the display of quotes effiQuotes Web Applicationciently, equipped with `next` and `previous` navigation buttons for ease of access.
#### New in this extension:
- **Password Reset:** Provides a secure mechanism for users to reset their passwords via email.
- **Environment Variables:** Uses environment variables for managing sensitive information like database credentials, email server settings, and secret keys.

### Quotes Web Application Technologies Used

- **Django:** Used for the backend framework, facilitating rapid development and clean, pragmatic design.
- **PostgreSQL:** Acts as the primary relational database management system for robust data handling.
- **Poetry:** Manages dependencies and packages, ensuring a consistent and reproducible virtual development environment.
- **Docker Compose:** Simplifies deployment by using containerization to manage service configurations.

### Quotes Web Application Installation and Usage

#### Setting Up the Project

- **Navigate to the Project Directory:**
```bash
cd ../second_task
```

- **To set up the environment** use the following commands depending on your operating system:
    - Unix/Linux/macOS:
    ```bash
    cp .env.example .env
    ```
    - Windows:
    ```powershell
    copy .env.example .env
    ```

Edit the `.env` file with your settings.

- **Activate the Poetry Environment and Install Dependencies:**
```bash
poetry shell
poetry install --no-root
```

- **Start the PostgreSQL Server** with Docker Compose:
```bash
docker compose up -d
```

#### Database Migration and Data Transfer

- **Navigate further into the Django project directory:**
```bash
cd quotes_project/
```

- **Perform database migrations and data transfers:**
    - Unix/Linux/macOS:
    ```bash
    python3 manage.py migrate
    ```
    - Windows:
    ```powershell
    py manage.py migrate
    ```

- **Transfer data from Atlas MongoDB:**
    - Unix/Linux/macOS:
    ```bash
    python3 -m utils.migration
    ```
    - Windows:
    ```powershell
    py -m utils.migration
    ```

#### Starting the Server

- Once the migrations and data transfer are complete, **launch the Django development server**:
    - Unix/Linux/macOS:
    ```bash
    python3 manage.py runserver
    ```
    - Windows:
    ```powershell
    py manage.py runserver
    ```

#### Accessing the Application

After starting the server, open a web browser and visit the following URL to access the "Quotes" application:

[http://127.0.0.1:8000/quotesapp/](http://127.0.0.1:8000/quotesapp/)

### How to Use the "Quotes" Website

Once you have the "Quotes" website running, here's how you can explore and interact with the site:

#### Viewing Quotes and Authors

- **Browse Quotes:** Upon visiting the main page at [http://127.0.0.1:8000/quotesapp/](http://127.0.0.1:8000/quotesapp/), you'll be greeted with a list of all the quotes uploaded to the site. Each quote is displayed with its content, the author's name, and associated tags.
- **Learn About Authors:** Each author's name is a clickable link. Clicking on an author's name will take you to a dedicated page that includes a biography of the author.

#### Interacting with the Site as a Registered User

After registering and logging in, you gain additional capabilities:

- **Add New Quotes, Authors, and Tags:** Authenticated users can contribute to the site by adding new quotes and the authors who said them. You can also create tags to help categorize quotes, making them easier to find through search or tag-based navigation.
- **Edit and Delete Entries:** If you have added a quote, an author, or a tag, you can also edit or remove these entries. This helps in keeping the information up to date and accurate.
- **Update Your Profile:** Users can update their personal information and profile picture (avatar) from the profile page. This feature allows users to express their personality and preferences.

#### Using the Search Functionality

- **Search by Tags:** The site includes a tag-based search feature, where clicking on a tag from the "Top Ten Tags" section or any tag listed under a quote will display all quotes associated with that tag. This is useful for users interested in specific themes or subjects.

#### Navigation and Accessibility

- **Pagination Controls:** While browsing quotes, you can use the pagination controls at the bottom of the page to navigate between pages of quotes. This makes it easy to browse through large numbers of entries without overwhelming the user.


### Stopping the Server and Exiting

When you are finished using the "Quotes" website, follow these steps to properly shut down the server and exit the development environment:

#### Stop the Application

To stop the Django development server, you simply need to press `CTRL+C` in the terminal window where the server is running. This will terminate the server process.

#### Shut Down the PostgreSQL Server

If you've started the PostgreSQL server using Docker Compose and wish to stop it, you can use the following command:

- **To stop and remove containers, networks, and volumes:**
```bash
docker compose down
```

- **To stop the server without removing resources:**
```bash
docker compose stop
```

#### Exit the Poetry Environment
```bash
exit
```

This command will deactivate the virtual environment and return you to your system's default environment.

<a href="#rest-api-and-django-projects" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; display: inline-block; border-radius: 8px; text-decoration: none;">Back to Top</a>
