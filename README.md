# 🚀 POI Application (API)
_This application designed to manage Places of Interests (POIs) with their respective locations and names. The application provides a REST API for handling user authentication, CRUD operations on POIs, and user management._

## Framework Selection

For this project, the backend is built using Django and Django REST Framework (DRF), known for their comprehensive features, including a powerful admin interface, integrated ORM, and efficient API development tools.

## Setup Instructions

1. **Prerequisites:**
   - Make sure you have Python installed on your system. You can download and install Python from the official website: https://www.python.org/
   - Install Postgres on your system. You can download and install Postgres from the official website: https://www.postgresql.org/

2. **Install Geospatial library**
   - make sure library installed and given path in .env, reference: https://docs.djangoproject.com/en/5.0/ref/contrib/gis/install/geolibs/

3.  **PostGIS Extension:**
    - Set up the PostGIS extension with the database to store point geometry data.
    - also change db engine to postgis `"ENGINE": "django.contrib.gis.db.backends.postgis",`

4. **Virtual Environment:**
   - Create a virtual environment to avoid version collisions.

5. **Dependencies Installation:**
   - Install project dependencies using the provided [`requirements.txt`](requirements.txt) file.

6. **Environment Variables:**
   - Create a `.env` file based on the provided `.env.example` to configure local environment variables.

7. **Migration:**
   - Make migrations and apply them to set up the database schema.
     
  
   ```
    python manage.py makemigrations
    python manage.py migrate
   ```
