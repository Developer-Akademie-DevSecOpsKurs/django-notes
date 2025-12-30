# Django Fullstack Notes App

## Description

A full-stack notes application built with Django that allows users to create, read, update, and delete personal notes. The application features a RESTful API backend powered by Django and Django REST Framework, with user authentication, note management capabilities, and a clean, responsive user interface.

Key features:
- User authentication and authorization
- Create, edit, and delete notes
- Organize notes with categories or tags
- Search and filter functionality
- Responsive web interface
- RESTful API for programmatic access

## Quickstart

To get the application running quickly:

0. **Clone the repository and navigate to it:**
   ```bash
   git clone kodskokdosaksdao
   ```

1. **Create and activate a virtual environment:**
   ```bash
   python -m venv djnotes-venv
   # Windows
   djnotes-venv\Scripts\activate
   # macOS/Linux
   source djnotes-venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations:**
   ```bash
   cd src
   python manage.py migrate
   ```

4. **Create a superuser (optional but recommended):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Open your browser and navigate to `http://localhost:8000`
   - Admin interface available at `http://localhost:8000/admin`

## Usage

### Configuration

The application can be configured through environment variables or by modifying the `settings.py` file:

- **SECRET_KEY**: Django secret key (set via environment variable in production)
- **DEBUG**: Enable/disable debug mode (default: True for development)
- **ALLOWED_HOSTS**: List of allowed hostnames
- **DATABASE**: Database configuration (default: SQLite)

### Management Commands

Django provides various management commands for the application:

**Database Management:**
```bash
python manage.py makemigrations  # Create new migrations
python manage.py migrate         # Apply database migrations
python manage.py flush           # Clear database
```

**User Management:**
```bash
python manage.py createsuperuser      # Create admin user
python manage.py changepassword <username>  # Change user password
```

**Development:**
```bash
python manage.py runserver        # Start development server
python manage.py runserver 8080   # Start on custom port
python manage.py shell           # Open Django shell
```

**Static Files:**
```bash
python manage.py collectstatic   # Collect static files for production
```

**Testing:**
```bash
python manage.py test            # Run test suite
```

## Contributing

Contributions to this project are welcome! We follow a feature branch workflow that requires maintainer approval before merging changes.

**Contribution Process:**

1. **Fork the repository** to your own GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/django-notes.git
   ```
3. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** and commit them with clear, descriptive messages
5. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** against the upstream repository's `main` branch
7. **Wait for review** - a maintainer will review your changes and provide feedback
8. **Address feedback** if necessary and push updates to your branch
9. Once approved, a maintainer will merge your contribution

**Guidelines:**
- Write clear commit messages
- Follow existing code style and conventions
- Add tests for new features
- Update documentation as needed
- Keep pull requests focused on a single feature or fix
