# Django

# Floorplan Grid Editor

This is a Django-based web app that overlays movable, resizable, and non-overlapping grids on a static floor plan.

## Features
- Add grid with customizable size
- Drag to move grids (with overlap prevention)
- Resize grids (with overlap & boundary detection)
- Select and delete grid
- All layout updates saved to database

## Setup

```bash
# Clone the repo
git clone https://github.com/YOUR_NAME/floorplan_project.git
cd floorplan_project

# Create and activate a conda environment
conda create -n floorplanenv python=3.10
conda activate floorplanenv

# Run migrations and start server
python manage.py migrate
python manage.py runserver

## Project Structure:
floorplan_project/
│
├── config/                  # Project configuration and startup settings
│   ├── __init__.py
│   ├── settings.py          # Django settings (database, static files, installed apps, etc.)
│   ├── urls.py              # Global URL routing configuration
│   └── wsgi.py              # WSGI entry point for deployment
│
├── grids/                   # App: handles grid logic and frontend interaction
│   ├── __init__.py
│   ├── models.py            # Grid data model (x, y, width, height)
│   ├── views.py             # View logic: load page, save grids, update position/size, delete grids
│   ├── forms.py             # Form handling (for creating new grids)
│   ├── urls.py              # App-specific URL routing
│   └── templates/grids/index.html   # Main frontend HTML template
│
├── static/                  # Static resources
│   └── image001.png         # Background floor plan image
│
├── db.sqlite3               # SQLite database file (stores grid information)
└── manage.py                # Django management command entry point (e.g., runserver, migrate)
