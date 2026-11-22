# Paw Haven – Pet Adoption System

A small Django learning project, created by the student with AI assistance, where visitors can browse pets, make an account, and send an adoption request. Staff can see a simple dashboard and manage pets and requests through Django admin.

## Run locally

1. Activate the virtual environment.
2. Install the packages with `pip install -r requirements.txt`.
3. Apply database changes with `python manage.py migrate`.
4. Create an administrator with `python manage.py createsuperuser`.
5. Start Django with `python manage.py runserver` and open `http://127.0.0.1:8000/`.

Add pets at `/admin/`. The public pet list only shows pets marked available.

## Main pages

- `/` – available pets and adoption request buttons.
- `/accounts/signup/` and `/accounts/login/` – customer accounts and sign in.
- `/dashboard/` – staff-only overview of pets and adoption requests.
- `/admin/` – staff tools for adding/editing/deleting pets and reviewing requests.

## Roles

- **Admin:** a Django superuser; can manage all records in Django admin.
- **Staff/Manager:** a user marked as staff in Django admin; can open the staff dashboard and admin tools.
- **Customer:** a normal account created through sign up; can browse pets and send adoption requests.

The `AdoptionRequest` record connects one customer to one pet. Django stores these records in the database, and migrations create/update the database tables.

## Database relationship

Each adoption request belongs to one pet and one registered customer. A pet or customer can have more than one request over time. The request stores a short note, a review status, and the date it was created.

## Prepare for GitHub

The `.gitignore` file keeps the virtual environment, local database, and secrets out of the repository. The database itself is not uploaded; the migration files rebuild its tables.

## Deployment setup

The `render.yaml` and `build.sh` files prepare this app for a Render demo deployment. After pushing the project to your own GitHub repository, connect that repository in Render and create a Blueprint from `render.yaml`. Render will build the app, apply migrations, and provide a public URL. Create the online admin account from the Render service Shell with `python manage.py createsuperuser`, then add demo pets through `/admin/`.

Free hosting is suitable for a school demo, not permanent storage. Render's free web service can sleep when idle, and its free PostgreSQL database expires after 30 days. Keep a local copy of the project and database for the presentation.

## Security and learning notes

The local secret key is only a development fallback. Render creates a separate secret key for deployment, and debug mode is off there. Never commit passwords or a real production secret key. The local SQLite database and Django development server are for learning; use the deployment setup for the hosted demo.
