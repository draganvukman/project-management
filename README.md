# Project Management and Messaging System

This is a **Django-based web application** for managing projects and sending messages between users. It includes features like user authentication, project management, and a messaging system.

## Features

- **User Authentication**:
  - Registration, login, and profile management.
  - Password reset via email.
- **Project Management**:
  - Create, update, and delete projects.
  - Assign stakeholders to projects.
- **Messaging System**:
  - Send and receive messages between users.
  - Archive messages.

## Technologies Used

- **Backend**: Django
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Deployment**: Render

## Project Structure

```
project-root/
├── core/                  # Django project settings and configurations
├── users/                 # User management app
├── projects/              # Project management app
├── messaging/             # Messaging system app
├── templates/             # HTML templates
├── static/                # Static files (CSS, JS, images)
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
├── Procfile               # Render deployment configuration
└── README.md              # Project documentation
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/draganvukman/project-management.git
cd project-management
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root of your project and add the following variables:

```plaintext
DEBUG=True
SECRET_KEY=your-secret-key
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=5432
```

### 5. Set Up PostgreSQL

1. Install PostgreSQL on your system.
2. Create a database:
   ```sql
   CREATE DATABASE your-db-name;
   CREATE USER your-db-user WITH PASSWORD 'your-db-password';
   GRANT ALL PRIVILEGES ON DATABASE your-db-name TO your-db-user;
   ```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## Deployment on Render

### 1. Prepare for Deployment

1. Freeze dependencies:

   ```bash
   pip freeze > requirements.txt
   ```

2. Create a `Procfile`:

   ```plaintext
   web: gunicorn core.wsgi
   ```

3. Collect static files:

   ```bash
   python manage.py collectstatic
   ```

### 2. Push Code to GitHub

```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### 3. Deploy on Render

1. Go to the [Render Dashboard](https://dashboard.render.com/).
2. Click **New +** and select **Web Service**.
3. Connect your GitHub repository.
4. Configure the web service:
   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     python manage.py migrate
     python manage.py collectstatic --noinput
     ```
   - **Start Command**:
     ```bash
     gunicorn core.wsgi
     ```
5. Add environment variables (e.g., `DB_NAME`, `DB_USER`, `SECRET_KEY`).
6. Click **Create Web Service**.

### 4. Verify Deployment

1. Visit the provided Render URL to test your application.
2. Create a superuser using the Render shell:
   ```bash
   python manage.py createsuperuser
   ```

## Environment Variables

| Variable      | Description                  | Example Value              |
| ------------- | ---------------------------- | -------------------------- |
| `DEBUG`       | Enable/disable debug mode    | `False`                    |
| `SECRET_KEY`  | Django secret key            | `your-secret-key`          |
| `DB_NAME`     | PostgreSQL database name     | `projectdb`                |
| `DB_USER`     | PostgreSQL database user     | `projuser`                 |
| `DB_PASSWORD` | PostgreSQL database password | `projpass`                 |
| `DB_HOST`     | PostgreSQL database host     | `localhost` or Render host |
| `DB_PORT`     | PostgreSQL database port     | `5432`                     |

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact:

- **Name**: Dragan
- **Email**: [dvukman991@gmail.com](mailto:dvukman991@gmail.com)
- **GitHub**: [draganvukman](https://github.com/draganvukman)

---
