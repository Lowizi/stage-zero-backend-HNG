# Stage 0: Dynamic Profile Endpoint

## Setup Instructions
1. Clone the repo: `git clone https://github.com/yourusername/stage-zero-backend.git`
2. Install dependencies: `pip install django djangorestframework requests python-decouple tzdata`
3. Create `.env` with EMAIL, NAME, STACK, SECRET_KEY.
4. Run migrations: `python manage.py migrate`
5. Run server: `python manage.py runserver 0.0.0.0:8000`
6. Test: `curl http://localhost:8000/me/?format=json`

## Dependencies
- Django
- Django REST Framework
- Requests
- Python-Decouple
- Tzdata

## Environment Variables
- EMAIL: Your email
- NAME: Your full name
- STACK: e.g., Django/DRF
- SECRET_KEY: Generated secure key

## Tests
- Tested locally with multiple requests; timestamp and fact update dynamically.
