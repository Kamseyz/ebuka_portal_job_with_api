# Job Portal Web Application

This is a Django-based job portal that allows **workers** to apply for jobs and **employers** to post, edit, and manage job listings.

## Features

- Worker and Employer registration & login
- Employers can post, update, and delete jobs
- Workers can apply for jobs
- Workers can upload/download their CVs
- Employers can view applicants to their job postings
- User-friendly frontend with HTML templates
- Admin panel access for superuser

## Tech Stack

- **Backend**: Django, Django REST Framework (light use)
- **Frontend**: HTML, CSS (via Django Templates)
- **Database**: SQLite (for development)
- **Other Packages**:
  - `django-allauth` for user authentication
  - `Pillow` for image/CV handling
  - `python-decouple` for `.env` config
  - `django-anymail` (if you integrated email)
  - `Faker` (used for dummy data during development)

## Getting Started

### Prerequisites
Make sure you have Python 3.8+ and pip installed.

### Setup

```bash
git clone https://github.com/yourusername/job-portal.git
cd job-portal
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
pip install -r requirements.txt
