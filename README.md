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
