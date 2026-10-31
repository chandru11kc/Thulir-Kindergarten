# THULIR Kindergarten — Django Website

A portfolio/demo kindergarten website built using **Python, Django, HTML, CSS, JavaScript, and SQLite**. THULIR is a fictional school project, not an official school website.

## Features implemented

- Home, About, Programs, Infrastructure, and Gallery pages
- Admission enquiry and application forms
- Contact form and careers application with résumé upload
- User registration and Django authentication login/logout routes
- Django models for enquiries, admission applications, contact messages, and career applications
- Django admin integration and SQLite database for local development

## Tech stack

- **Backend:** Python, Django
- **Frontend:** Django templates, HTML, CSS, JavaScript
- **Database:** SQLite (local development)

## Run locally

Requires Python and Django. From this repository folder:

```bash
python -m venv .venv
```

Activate the environment (Windows PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Install Django:

```bash
pip install "Django>=6.0,<7.0"
```

Set a development secret key, for example in PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = 'replace-with-a-long-random-development-key'
```

Then run:

```bash
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/`.

## Notes

- This is a learning/portfolio project, not a production deployment.
- Uploaded résumés, user data, local database, virtual environment and Git history are intentionally excluded.
- Configure production settings, secrets, allowed hosts, static/media storage, and security before any public deployment.

## Author

[Chandru K](https://github.com/chandru11kc)
